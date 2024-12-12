import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import requests
from flask import Flask, request, jsonify

# Load data from CSV file and train the model
data = pd.read_csv('Grapes.csv')
X = data[['moisture', 'temp', 'humidity']]
y = data['pump']

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Define Blynk API token and virtual pin
# blynk_token = '2JrRjraAg8FjrweN2ftT-OL3TOFicxhb'
# blynk_pin = 'v1'

# Create Flask app
app = Flask(__name__)

# Define the API endpoint to predict pump status
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse incoming JSON data
        data = request.get_json()
        moisture = data['moisture']
        temp = data['temp']
        humidity = data['humidity']

        # Prepare data for prediction
        input_data = np.array([[moisture, temp, humidity]])
        prediction = model.predict(input_data)

        # Convert NumPy type to native Python type
        response = {'prediction': int(prediction[0])}
        print(response['prediction'])
        return jsonify(response['prediction'])

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)