import asyncio
import random
import logging
from aiocoap import Message, Context, POST

# turn on debug logging for aiocoap
logging.basicConfig(level=logging.DEBUG)

async def simulate_sensor_data():
    protocol = await Context.create_client_context()

    while True:
        # Generate two‐decimal sensor readings
        temperature = round(random.uniform(20.0, 25.0), 2)
        humidity    = round(random.uniform(30.0, 50.0), 2)
        payload     = f'{{"temperature": {temperature}, "humidity": {humidity}}}'.encode('utf-8')

        # Build the POST request with URI in constructor
        request = Message(
            code=POST,
            uri='coap://127.0.0.1:5684/sensor/data',
            payload=payload
        )

        logging.debug(f"→ Sending payload: {payload}")

        try:
            response = await protocol.request(request).response
            logging.debug(f"← Got response: {response.code} {response.payload}")
            print(f"Posted temp={temperature}, hum={humidity} → {response.code.name} {response.payload.decode()}")
        except Exception as e:
            logging.error("✖ Error sending request", exc_info=e)
            print("Error sending request:", e)

        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(simulate_sensor_data())
