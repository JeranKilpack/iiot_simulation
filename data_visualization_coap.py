import aiocoap
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

data = []

def on_message(payload):
    # CoAP payload should be a dictionary or JSON-like format
    data.append((datetime.now(), payload))
    if len(data) > 100:
        data.pop(0)
    df = pd.DataFrame(data, columns=["timestamp", "sensor_data"])
    df["temperature"] = df["sensor_data"].apply(lambda x: eval(x)["temperature"])
    df["humidity"] = df["sensor_data"].apply(lambda x: eval(x)["humidity"])

    plt.clf()
    plt.plot(df["timestamp"], df["temperature"], label="Temperature")
    plt.plot(df["timestamp"], df["humidity"], label="Humidity")
    plt.legend()
    plt.draw()
    plt.pause(0.1)

async def coap_client():
    context = await aiocoap.Context.create_client_context()
    request = aiocoap.Message(code=aiocoap.GET, uri='coap://localhost:5683/sensor/data')

    while True:
        try:
            response = await context.request(request).response
            payload = str(response.payload.decode('utf-8'))
            on_message(payload)
        except Exception as e:
            print(f"CoAP poll error: {e}")
        await asyncio.sleep(1)

plt.ion()
plt.figure()

import asyncio
asyncio.get_event_loop().run_until_complete(coap_client())
plt.show()

