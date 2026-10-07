# Day 43 – Machine Learning Deployment with FastAPI

## Objective

Deploy a customer risk prediction machine learning model as a REST API using FastAPI.

## Model Used

Random Forest Classifier

### Input Features

- Recency_Days
- Purchase_Frequency
- Estimated_CLV

### Target

Risk_Level

The model achieved approximately **94.97% accuracy** on the test data.

## API Endpoint

### GET /

Checks whether the API is running.

Example response:

```json
{
  "message": "Customer Risk Prediction API is running"
}