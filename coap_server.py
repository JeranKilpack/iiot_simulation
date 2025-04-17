import asyncio
from aiocoap import Context, Message, CHANGED
from aiocoap.resource import Resource, Site

class SensorResource(Resource):
    async def render_post(self, request):
        print(f"Received POST with payload: {request.payload.decode()}")
        return Message(code=CHANGED, payload=b"OK")

async def main():
    root = Site()
    root.add_resource(['sensor', 'data'], SensorResource())

    await Context.create_server_context(root, bind=('127.0.0.1', 5684))
    print("CoAP server is running on 127.0.0.1:5684 and handling POST /sensor/data")

    await asyncio.get_event_loop().create_future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
