
import logging
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# Save application logs in a file
logging.basicConfig(
    filename="day46_monitoring.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    force=True
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Customer Risk Prediction API",
    description="Monitored customer risk prediction API",
    version="2.0"
)

# Load the model safely
try:
    model = joblib.load("day43_customer_risk_model.pkl")
    logger.info("Model loaded successfully")
except Exception:
    model = None
    logger.exception("Model loading failed")


class CustomerData(BaseModel):
    Recency_Days: float = Field(ge=0)
    Purchase_Frequency: float = Field(ge=0)
    Estimated_CLV: float = Field(ge=0)


@app.get("/")
def home():
    return {"message": "Customer Risk Prediction API is running"}


@app.get("/health")
def health():
    if model is None:
        raise HTTPException(
            status_code=503,
            detail="Prediction model is unavailable"
        )
    return {"status": "healthy", "model_loaded": True}


@app.post("/predict-risk")
def predict_risk(customer: CustomerData):
    logger.info("Prediction request received")

    if model is None:
        logger.error("Prediction rejected: model unavailable")
        raise HTTPException(
            status_code=503,
            detail="Prediction service is unavailable"
        )

    try:
        input_data = pd.DataFrame([{
            "Recency_Days": customer.Recency_Days,
            "Purchase_Frequency": customer.Purchase_Frequency,
            "Estimated_CLV": customer.Estimated_CLV
        }])

        prediction = str(model.predict(input_data)[0])

        logger.info("Prediction completed: risk_level=%s", prediction)
        return {"Risk_Level": prediction}

    except Exception:
        logger.exception("Prediction failed")
        raise HTTPException(
            status_code=500,
            detail="Prediction failed. Please try again later."
        )
