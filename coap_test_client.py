import asyncio
import logging
from aiocoap import *

# turn on debug logging for aiocoap
logging.basicConfig(level=logging.DEBUG)

async def test_coap_get():
    protocol = await Context.create_client_context()

    # simple GET to the same endpoint
    request = Message(code=GET, uri='coap://127.0.0.1:5684/sensor/data')
    try:
        response = await protocol.request(request).response
        print("GET Response:", response.code, response.payload.decode())
    except Exception as e:
        print("GET Error:", e)

async def test_coap_post():
    protocol = await Context.create_client_context()

    # simple POST with a tiny payload
    payload = b'{"test": 1}'
    request = Message(code=POST, uri='coap://127.0.0.1:5684/sensor/data', payload=payload)
    try:
        response = await protocol.request(request).response
        print("POST Response:", response.code, response.payload.decode())
    except Exception as e:
        print("POST Error:", e)

if __name__ == "__main__":
    asyncio.run(test_coap_get())
    asyncio.run(test_coap_post())
