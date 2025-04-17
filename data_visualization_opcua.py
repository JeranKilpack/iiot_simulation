import opcua
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

data = []

def on_message(temperature, humidity):
    data.append((datetime.now(), {"temperature": temperature, "humidity": humidity}))
    if len(data) > 100:
        data.pop(0)
    df = pd.DataFrame(data, columns=["timestamp", "sensor_data"])
    df["temperature"] = df["sensor_data"].apply(lambda x: x["temperature"])
    df["humidity"] = df["sensor_data"].apply(lambda x: x["humidity"])

    plt.clf()
    plt.plot(df["timestamp"], df["temperature"], label="Temperature")
    plt.plot(df["timestamp"], df["humidity"], label="Humidity")
    plt.legend()
    plt.draw()
    plt.pause(0.1)

def opcua_client():
    client = opcua.Client("opc.tcp://localhost:4840/freeopcua/server")
    client.connect()

    try:
        while True:
            # Assuming that temperature and humidity are nodes in the OPC UA server
            temperature = client.get_node("ns=2;i=2").get_value()
            humidity = client.get_node("ns=2;i=3").get_value()
            on_message(temperature, humidity)
    except KeyboardInterrupt:
        client.disconnect()

plt.ion()
plt.figure()

opcua_client()
plt.show()
