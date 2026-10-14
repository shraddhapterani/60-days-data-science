# Day 51/60 — API Reliability and Automated Testing

## Objective

Improve the reliability of the Customer Risk Prediction API through safer model loading, input validation, error handling, logging, and automated testing.

## Work Completed

### 1. Reliable Model Loading
- Used `Path(__file__).resolve().parent` to locate the model file relative to `day43_api.py`.
- Added error handling for model-loading failures.
- Recorded model-loading success or failure in the application log.

### 2. Input Validation
- Used Pydantic to validate customer prediction inputs.
- Rejected negative values for `Recency_Days`, `Purchase_Frequency`, and `Estimated_CLV`.
- Verified that requests with missing required fields are rejected.

### 3. API Health Monitoring
- Tested the home endpoint.
- Tested the `/health` endpoint to verify model availability.
- Tested the `/predict-risk` endpoint with valid customer data.

### 4. Error Handling and Logging
- Handled prediction failures with HTTP status code `500`.
- Returned a safe error message to API users.
- Recorded prediction failures and exception details in server-side logs.

### 5. Automated Testing
Created `test_day51_api.py` with six tests:

1. Home endpoint responds successfully.
2. Health endpoint reports model availability.
3. Valid prediction requests work.
4. Negative values are rejected.
5. Missing fields are rejected.
6. Prediction failures return a safe error response.

## Test Results

- **Total tests:** 6
- **Passed:** 6
- **Failed:** 0

Command used:

```powershell
python -m pytest test_day51_api.py -v
```

## Files Used or Created

- `day43_api.py` — Updated Customer Risk Prediction API.
- `test_day51_api.py` — Automated API tests.
- `README_day51.md` — Day 51 documentation.
- `day46_monitoring.log` — Application logging output.

## Key Learning

Reliable machine learning applications need more than an accurate model. They also need input validation, robust error handling, monitoring, and automated tests to ensure the prediction service behaves safely when something goes wrong.

## Important Note

The tests validate the API's current behaviour. They do not establish production readiness, load-handling capacity, or predictive performance on new real-world data.