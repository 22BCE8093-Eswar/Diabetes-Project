from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load model and scaler
model = joblib.load('models/diabetes_model.pkl')
scaler = joblib.load('models/scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    final_features = np.array(data).reshape(1, -1)
    final_features = scaler.transform(final_features)
    prediction = model.predict(final_features)[0]
    result = 'Diabetic' if prediction == 1 else 'Non-Diabetic'
    return render_template('index.html', prediction_text=f'Prediction: {result}')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

