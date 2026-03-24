from flask_cors import CORS
from flask import Flask, request, jsonify,send_from_directory
import pickle
import numpy as np
import os

app = Flask(__name__, static_folder="../frontend")
CORS(app)

model_path= os.path.join(os.path.dirname(__file__), "../kmeans_model.pkl")
model = pickle.load(open(model_path,"rb"))

@app.route("/")
def home():
    return send_from_directory(app.static_folder,"index.html")

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    income = float(data["income"])
    score = float(data["score"])

    features = np.array([[income, score]])

    prediction = model.predict(features)

    return jsonify({
        "cluster": int(prediction[0])
    })
@app.route("/clusters")
def clusters():

    import pandas as pd

    df = pd.read_csv("../Mall_Customers.csv")

    X = df[['Annual Income (k$)','Spending Score (1-100)']]

    labels = model.predict(X)

    points = []

    for i in range(len(X)):

        points.append({
            "x": float(X.iloc[i,0]),
            "y": float(X.iloc[i,1]),
            "cluster": int(labels[i])
        })

    return jsonify(points)

if __name__ == "__main__":
    app.run(debug=True)