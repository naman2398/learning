import joblib
import pandas as pd
from flask import Flask, jsonify, request
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model
from classes import CountrytoContinent,MonthHour,DropColumns,Encoding

app = Flask(__name__)
#print("app")
model = load_model("best_model.h5")
print("Model loaded")
feature_transformer = joblib.load("data_transformer.joblib")
encoding_transformer = joblib.load("encoding_transformer.joblib")
scaling_transformer = joblib.load("scaler_transformer.joblib")
print("Transformer loaded")

@app.route("/", methods=["POST"])
def index():
    data = request.json
    df = pd.DataFrame(data, index=[0])
    feature_transformer.transform(df)
    df=encoding_transformer.transform(df)
    df=scaling_transformer.transform(df)
    pred=int(model.predict(df)>0.5)
    if pred==1:
        return jsonify({"Click Prediction": "Clicked"})
    else:
        return jsonify({"Click Prediction": "Not Clicked"})

if __name__ == "__main__":
    app.run(debug=True)