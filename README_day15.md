# Day 15 - Customer Churn Classification

## Objective
Build a classification model to predict whether a customer will churn.

## Dataset
Telco Customer Churn Dataset

- Rows after cleaning: 7032
- Features used: 18
- Target: Churn

## Model
Logistic Regression

## Train-Test Split
- Training rows: 5625
- Testing rows: 1407
- Split: 80/20

## Results

| Metric | Result |
|---|---:|
| Accuracy | 80.24% |
| True Negatives | 919 |
| False Positives | 114 |
| False Negatives | 164 |
| True Positives | 210 |

## Business Impact

### False Positive
114 customers were predicted to churn but actually stayed.

The company may spend unnecessary money on retention offers.

### False Negative
164 customers actually churned but were predicted to stay.

The company may miss the opportunity to retain these customers and lose potential revenue.

## Key Learning
Classification models support real-world business decisions, and different prediction errors can have different business costs.

## Files
- `day15_customer_churn.ipynb`
- `day15_churn_predictions.csv`
- `README_day15.md`