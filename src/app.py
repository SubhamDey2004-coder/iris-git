from pathlib import Path
import joblib
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="Iris Prediction API")

MODEL_PATH = Path("models/iris_model.joblib")
model = joblib.load(MODEL_PATH)


class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.get("/")
def root():
    return {"message": "Iris Prediction API is running"}


@app.post("/predict")
def predict(data: IrisInput):
    features = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width,
    ]]

    prediction = model.predict(features)[0]

    return {"prediction": int(prediction)}