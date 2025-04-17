import paho.mqtt.client as mqtt
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import json

print("🟢 Starting MQTT visualization…")

data = []

def on_message(client, userdata, message):
    payload = message.payload.decode("utf-8")
    # confirm we got MQTT data
    print(f"🔔 MQTT message received: {payload}")

    try:
        obj = json.loads(payload)
    except json.JSONDecodeError as e:
        print("⚠️ JSON parse error:", e)
        return

    data.append((datetime.now(), obj["temperature"], obj["humidity"]))
    if len(data) > 100:
        data.pop(0)

    df = pd.DataFrame(data, columns=["timestamp","temperature","humidity"])
    plt.clf()
    plt.plot(df["timestamp"], df["temperature"], label="Temperature")
    plt.plot(df["timestamp"], df["humidity"],    label="Humidity")
    plt.legend()
    plt.draw()
    plt.pause(0.1)

if __name__ == "__main__":
    client = mqtt.Client()
    client.connect("localhost", 1883)
    client.subscribe("sensor/data")
    client.on_message = on_message

    plt.ion()
    plt.figure()
    client.loop_start()
    plt.show()
