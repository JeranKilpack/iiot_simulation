import asyncio
import random
from asyncua import ua, Server

async def main():
    # Set up OPC UA server
    server = Server()
    await server.init()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server")
    uri = "http://examples.freeopcua.github.io"
    idx = await server.register_namespace(uri)

    # Create an object and two variables (Temperature & Humidity)
    objects = server.nodes.objects
    myobj = await objects.add_object(idx, "MyObject")
    temperature = await myobj.add_variable(idx, "Temperature", 0.0)
    humidity    = await myobj.add_variable(idx, "Humidity", 0.0)

    # Allow the server to write to these variables
    await temperature.set_writable()
    await humidity.set_writable()

    print("OPC UA server running at opc.tcp://0.0.0.0:4840/freeopcua/server")

    # Start the server and update values every second
    async with server:
        while True:
            temp_value = round(random.uniform(20.0, 25.0), 2)
            hum_value  = round(random.uniform(30.0, 50.0), 2)
            await temperature.write_value(temp_value)
            await humidity.write_value(hum_value)
            print(f"Temperature: {temp_value}, Humidity: {hum_value}")
            await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
