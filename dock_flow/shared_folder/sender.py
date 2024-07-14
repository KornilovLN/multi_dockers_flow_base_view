import requests
import time
import random

BASE_URL = 'http://base-container:5000'

def send_data():
    while True:
        data = {"sensor": "temperature", "value": random.uniform(20.0, 30.0)}
        response = requests.post(f'{BASE_URL}/data', json=data)
        print(f"Data sent: {data}")
        time.sleep(5)

if __name__ == '__main__':
    send_data()
