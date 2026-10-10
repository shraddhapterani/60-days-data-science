# Day 46/60 — Production Monitoring

## Project
Customer Risk Prediction API

## Objective
Improve API reliability through logging, input validation, exception handling, and health monitoring.

## Improvements Implemented
- Added application logging to `day46_monitoring.log`.
- Added Pydantic validation to reject negative input values.
- Added exception handling for model loading and prediction failures.
- Added a `/health` endpoint to check model availability.
- Recorded successful prediction requests and risk outputs.

## Testing Results

### Successful Prediction
Input:
- Recency Days: 184
- Purchase Frequency: 1.54
- Estimated CLV: 5136.68

Output: `High Risk`

Status: Passed.

### Invalid Input
Input: `Recency_Days = -10`

Result: Rejected by FastAPI validation with HTTP 422.

Status: Passed.

### Monitoring Log
The log recorded:
- Successful model loading.
- Prediction request received.
- Prediction completed with risk level `High Risk`.

## Key Learnings
- Logging helps investigate application behaviour.
- Input validation prevents unreasonable data from reaching the model.
- Exception handling improves failure responses.
- Health checks help determine whether the prediction service is ready.

## Outcome
Improved the local Customer Risk Prediction API with monitoring and reliability safeguards.

Note: Invalid inputs rejected by FastAPI's automatic validation are not currently recorded in the application log.
