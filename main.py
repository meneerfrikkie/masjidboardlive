import os
import requests
from bs4 import BeautifulSoup
import paho.mqtt.client as mqtt
import time

# Environment variables
MQTT_BROKER = os.getenv('MQTT_BROKER')
MQTT_PORT = int(os.getenv('MQTT_PORT'))
MQTT_USER = os.getenv('MQTT_USER')
MQTT_PASSWORD = os.getenv('MQTT_PASSWORD')
MQTT_TOPIC_PREFIX = os.getenv('MQTT_TOPIC_PREFIX', 'homeassistant/sensor/salaah')
MASJID_BOARD_URL = os.getenv('MASJID_BOARD_URL')

# Dictionary to hold prayer names and their corresponding IDs
PRAYERS = {
    'Fajr': 'fajr',
    'Zuhr': 'zuhr',
    'Asr': 'asr',
    'Maghrib': 'maghrib',
    'Isha': 'esha'
}

# Function to scrape salaah times
def get_salaah_times():
    response = requests.get(MASJID_BOARD_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    salaah_times = {}

    for prayer, prayer_id in PRAYERS.items():
        athan_time = soup.find('h5', id=f'{prayer_id}Athan').text.strip()
        jamaah_time = soup.find('h5', id=f'{prayer_id}Jamaah').text.strip()
        salaah_times[prayer] = {'Adhan': athan_time, 'Jamaah': jamaah_time}

    return salaah_times

# MQTT connection setup
def connect_mqtt():
    client = mqtt.Client()
    client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
    client.connect(MQTT_BROKER, MQTT_PORT)
    return client

# Publish salaah times to MQTT
def publish_salaah_times(client, salaah_times):
    for prayer, times in salaah_times.items():
        client.publish(f"{MQTT_TOPIC_PREFIX}/{prayer}/adhan", times['Adhan'])
        client.publish(f"{MQTT_TOPIC_PREFIX}/{prayer}/jamaah", times['Jamaah'])

# Main function to scrape, connect, and publish data
def main():
    client = connect_mqtt()
    client.loop_start()

    while True:
        salaah_times = get_salaah_times()
        publish_salaah_times(client, salaah_times)
        print("Published Salaah times to MQTT")
        time.sleep(int(os.getenv('POLL_INTERVAL', 600)))  # Default polling interval is 10 minutes

if __name__ == '__main__':
    main()