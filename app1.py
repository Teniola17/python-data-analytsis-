from fastapi import FastAPI
import pandas as pd
import joblib

# load trained pipeline
model = joblib.load("best_svc_obesity_model.pkl")

app = FastAPI(title="Obesity Prediction API")

@app.get("/")
def home():
    return {"message": "Obesity prediction API is running"}

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return {"prediction": prediction}

