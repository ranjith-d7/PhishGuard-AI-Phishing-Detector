# server/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app) # Allow the browser extension to talk to us

# Load the brain we just trained
model = joblib.load("phishing_model.pkl")

def get_features(url):
    # Must match the function in train.py exactly!
    return np.array([
        len(url), 
        url.count('.'), 
        1 if '@' in url else 0, 
        url.count('/'), 
        1 if not url.startswith('https') else 0
    ]).reshape(1, -1)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    url = data.get('url', '')
    
    # Ask the AI
    features = get_features(url)
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]
    
    result = "PHISHING" if prediction == 1 else "SAFE"
    
    return jsonify({
        "result": result,
        "risk": round(probability * 100, 2)
    })

if __name__ == '__main__':
    print("Server running on port 5000...")
    app.run(port=5000)