# Day 20 — Model Evaluation

## ABTalks 60-Day Data Science Challenge

### Phase
Model Evaluation

## Objective

The objective of Day 20 was to evaluate Machine Learning classification models using multiple performance metrics instead of relying only on accuracy.

The models evaluated were:

- Random Forest
- XGBoost

The evaluation included precision, recall, F1-score, ROC-AUC, and confusion matrices.

---

## Dataset

A synthetic fraud-detection dataset containing 2,000 transactions was used.

### Features

- transaction_amount
- transaction_frequency
- account_age_days
- international
- failed_attempts

### Target

- `0` → Not Fraud
- `1` → Fraud

Class distribution:

- Not Fraud: 1,269
- Fraud: 731

The dataset was divided into:

- Training set: 1,600 samples
- Testing set: 400 samples

---

## Evaluation Metrics

### Accuracy

Measures the percentage of total predictions that are correct.

### Precision

Measures how many transactions predicted as fraud were actually fraudulent.

### Recall

Measures how many actual fraud transactions were successfully detected.

### F1-Score

Provides a balance between precision and recall.

### ROC-AUC

Measures how well the model distinguishes between fraud and non-fraud across different classification thresholds.

---

## Model Performance

| Metric | Random Forest | XGBoost |
|---|---:|---:|
| Accuracy | 92.50% | 91.75% |
| Precision | 90.28% | 88.44% |
| Recall | 89.04% | 89.04% |
| F1-Score | 89.66% | 88.74% |
| ROC-AUC | 91.29% | 91.31% |

### Analysis

Random Forest performed better in:

- Accuracy
- Precision
- F1-score

Both models achieved the same recall of 89.04%.

XGBoost achieved a slightly higher ROC-AUC:

- XGBoost: 91.31%
- Random Forest: 91.29%

The ROC-AUC difference was extremely small.

---

## Confusion Matrix Analysis

### Random Forest

```text
[[240, 14],
 [ 16, 130]]