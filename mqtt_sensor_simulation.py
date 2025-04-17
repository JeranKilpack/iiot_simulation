import paho.mqtt.client as mqtt
import random
import time

broker = "localhost"  # The Mosquitto broker is running on the same machine
port = 1883
topic = "sensor/data"

def simulate_sensor_data():
    try:
        while True:
            # Simulate random sensor data (temperature and humidity)
            temperature = random.uniform(20.0, 25.0)
            humidity = random.uniform(30.0, 50.0)

            # Create the payload as a JSON-like string
            payload = f'{{"temperature": {temperature}, "humidity": {humidity}}}'

            # Publish the data to the MQTT broker
            client.publish(topic, payload)

            # Wait for 1 second before publishing again
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nSimulation stopped by user.")
        client.disconnect()

# Create MQTT client instance
client = mqtt.Client(protocol=mqtt.MQTTv5)  # Updated protocol

# Connect to the broker
client.connect(broker, port)

# Start publishing sensor data
simulate_sensor_data()

