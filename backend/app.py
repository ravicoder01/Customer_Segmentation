from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pickle
import numpy as np
import pandas as pd
import os

# Root directory of the project (one level up from backend/)
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND_DIR = os.path.join(ROOT_DIR, "frontend")

app = Flask(__name__, static_folder=FRONTEND_DIR, static_url_path="")
CORS(app)

# Load model from root directory
model_path = os.path.join(ROOT_DIR, "kmeans_model.pkl")
model = pickle.load(open(model_path, "rb"))

@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    income = float(data["income"])
    score = float(data["score"])
    features = np.array([[income, score]])
    prediction = model.predict(features)
    return jsonify({"cluster": int(prediction[0])})

@app.route("/clusters")
def clusters():
    csv_path = os.path.join(ROOT_DIR, "Mall_Customers.csv")
    df = pd.read_csv(csv_path)
    X = df[['Annual Income (k$)', 'Spending Score (1-100)']]
    labels = model.predict(X)
    points = []
    for i in range(len(X)):
        points.append({
            "x": float(X.iloc[i, 0]),
            "y": float(X.iloc[i, 1]),
            "cluster": int(labels[i])
        })
    return jsonify(points)

if __name__ == "__main__":
    app.run(debug=True)