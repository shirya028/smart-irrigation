import requests
import time
blynk_token = '2JrRjraAg8FjrweN2ftT-OL3TOFicxhb'
blynk_pin = 'v1'
# Define the API endpoint
url = 'http://127.0.0.1:5000/predict'
# Example sensor data
api_url = f'https://blynk.cloud/external/api/get?token={blynk_token}&v0&v4&v2'

while(True) :
    response = requests.get(api_url)
    sensor_data = response.json()
    print(sensor_data)

    # Parse JSON data
    m = float(sensor_data['v0'])  # v0 for moisture
    h = float(sensor_data['v4'])  # v4 for humidity
    t = float(sensor_data['v2'])   
    sensor_data = {
        'moisture': m,
        'temp': t,
        'humidity': h
    }

    # Send the POST request
    response = requests.post(url, json=sensor_data)
    blynk_url = f'https://blynk.cloud/external/api/update?token={blynk_token}&{blynk_pin}={int(response.json())}'
    blynk_response = requests.get(blynk_url)

    # Print the response
    print(response.json())
    time.sleep(2) 
