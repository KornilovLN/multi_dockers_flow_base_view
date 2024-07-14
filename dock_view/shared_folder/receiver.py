import requests
import time

BASE_URL = 'http://base-container:5000'

def get_data():
    while True:
        response = requests.get(f'{BASE_URL}/data')
        if response.status_code == 200:
            print(f"Received data: {response.json()}")
        else:
            print("Failed to retrieve data")
        time.sleep(10)

if __name__ == '__main__':
    get_data()


