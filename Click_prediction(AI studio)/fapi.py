import joblib
import pandas as pd
import uvicorn
from fastapi import FastAPI
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model
from classes import CountrytoContinent,MonthHour,DropColumns,Encoding

fapi = FastAPI()
model = load_model("model.h5")
print("Model loaded")
feature_transformer = joblib.load("data_transformer.joblib")
encoding_transformer = joblib.load("encoding_transformer.joblib")
scaling_transformer = joblib.load("scaler_transformer.joblib")
print("Transformer loaded")

@fapi.get('/')
def index():
    return {"message":"LOL"}

@fapi.post('/predict')
def predict():
    data = request.json
    df = pd.DataFrame(data, index=[0])
    feature_transformer.transform(df)
    df=encoding_transformer.transform(df)
    df=scaling_transformer.transform(df)
    pred=(model.predict(df)>0.5).astype("int32")
    if pred==1:
        return jsonify({"Click Prediction": "Clicked"})
    else:
        return jsonify({"Click Prediction": "Not Clicked"})

if __name__ == "__main__":
    uvicorn.run(fapi, host='127.0.0.1', port=8000)