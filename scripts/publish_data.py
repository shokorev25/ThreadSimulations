import paho.mqtt.client as mqtt
import os
import time

MQTT_BROKER = 'localhost'
MQTT_PORT = 1883
MQTT_TOPIC = 'gnss_data'

def publish_data():
    client = mqtt.Client()
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    
    # Обработка данных (пример)
    for filename in os.listdir('data/converted'):
        if filename.endswith('.rnx'):
            with open(os.path.join('data/converted', filename), 'r') as file:
                data = file.read()
                client.publish(MQTT_TOPIC, data)
    
    client.disconnect()

if __name__ == "__main__":
    while True:
        publish_data()
        time.sleep(30)
