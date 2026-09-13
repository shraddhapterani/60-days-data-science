# Day 19 — XGBoost Boosting Model

## ABTalks 60-Day Data Science Challenge

### Phase
Advanced Ensemble Systems

### Objective

The objective of Day 19 was to understand Gradient Boosting and train an XGBoost model for fraud detection. The XGBoost model was compared with Random Forest to evaluate their predictive performance.

---

## Dataset

A synthetic fraud-detection dataset containing 2,000 transactions was created.

### Features

- transaction_amount
- transaction_frequency
- account_age_days
- international
- failed_attempts

### Target

- `0` → Not Fraud
- `1` → Fraud

Dataset shape:

- 2,000 rows
- 5 input features
- 1 target variable

The data was split into:

- Training set: 1,600 samples
- Testing set: 400 samples

---

## XGBoost Model

The XGBoost classifier was configured with:

- Number of estimators: 100
- Maximum tree depth: 4
- Learning rate: 0.1
- Subsample: 0.8
- Column sampling: 0.8
- Random state: 42

### XGBoost Performance

Accuracy:

**91.75%**

Confusion Matrix:

```text
[[237, 17],
 [ 16, 130]]