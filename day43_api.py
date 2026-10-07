from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Create FastAPI application
app = FastAPI(
    title="Customer Risk Prediction API",
    description="API for predicting customer risk levels",
    version="1.0"
)

# Load trained model
model = joblib.load("day43_customer_risk_model.pkl")


# Input data structure
class CustomerData(BaseModel):
    Recency_Days: float
    Purchase_Frequency: float
    Estimated_CLV: float


# Prediction endpoint
@app.post("/predict-risk")
def predict_risk(customer: CustomerData):

    input_data = pd.DataFrame([{
        "Recency_Days": customer.Recency_Days,
        "Purchase_Frequency": customer.Purchase_Frequency,
        "Estimated_CLV": customer.Estimated_CLV
    }])

    prediction = model.predict(input_data)[0]

    return {
        "Risk_Level": prediction
    }


# Basic health-check endpoint
@app.get("/")
def home():
    return {
        "message": "Customer Risk Prediction API is running"
    }