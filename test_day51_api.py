
from fastapi.testclient import TestClient

import day43_api
from day43_api import app

# Create a test client for the API
client = TestClient(app)


# Test 1: Home endpoint
def test_home_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert "running" in response.json()["message"].lower()


# Test 2: Health endpoint
def test_health_endpoint():
    response = client.get("/health")

    if day43_api.model is None:
        assert response.status_code == 503
    else:
        assert response.status_code == 200
        assert response.json()["model_loaded"] is True


# Test 3: Prediction with valid input
def test_prediction_with_valid_input():
    if day43_api.model is None:
        return

    payload = {
        "Recency_Days": 30,
        "Purchase_Frequency": 5,
        "Estimated_CLV": 2500
    }

    response = client.post("/predict-risk", json=payload)

    assert response.status_code == 200
    assert "Risk_Level" in response.json()


# Test 4: Reject negative values
def test_prediction_rejects_negative_values():
    payload = {
        "Recency_Days": -1,
        "Purchase_Frequency": 5,
        "Estimated_CLV": 2500
    }

    response = client.post("/predict-risk", json=payload)

    assert response.status_code == 422


# Test 5: Reject missing fields
def test_prediction_rejects_missing_fields():
    payload = {
        "Recency_Days": 30
    }

    response = client.post("/predict-risk", json=payload)

    assert response.status_code == 422


# Test 6: Return a safe error when prediction fails
def test_prediction_failure_returns_safe_error(monkeypatch):
    class BrokenModel:
        def predict(self, input_data):
            raise RuntimeError("Internal model details")

    # Temporarily replace the real model with a failing model
    monkeypatch.setattr(day43_api, "model", BrokenModel())

    payload = {
        "Recency_Days": 30,
        "Purchase_Frequency": 5,
        "Estimated_CLV": 2500
    }

    response = client.post("/predict-risk", json=payload)

    assert response.status_code == 500

    assert response.json()["detail"] == (
        "Prediction failed. Please try again later."
    )

    # Internal error details must not be exposed to the API user
    assert "Internal model details" not in response.text
