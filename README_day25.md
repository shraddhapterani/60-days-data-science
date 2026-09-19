# Day 25/60 — Model Validation with Cross-Validation

## Objective

To understand how Cross-Validation helps evaluate the reliability and consistency of Machine Learning models across multiple data splits.

## Dataset

The dataset contains 100 e-commerce customer records with:

- Age
- Income
- Purchase Amount
- Savings
- Credit Score
- Purchased

## Validation Methods

### 1. Train-Test Split

A single 80/20 train-test split was used.

Accuracy:

**100%**

### 2. 5-Fold Cross-Validation

The dataset was divided into 5 folds. Each fold was used once as validation data while the remaining folds were used for training.

Random Forest CV Scores:

**[0.95, 1.00, 1.00, 1.00, 0.95]**

Mean Accuracy:

**98%**

Standard Deviation:

**0.0245**

## Model Comparison

| Model | Mean CV Accuracy | Standard Deviation | Min Score | Max Score |
|---|---:|---:|---:|---:|
| Random Forest | 98% | 0.0245 | 95% | 100% |
| Logistic Regression | 95% | 0.0316 | 90% | 100% |

## Key Observations

- A single train-test split produced 100% accuracy.
- 5-fold cross-validation gave a more detailed view of model performance across different data splits.
- Random Forest achieved a mean CV accuracy of 98%.
- Logistic Regression achieved a mean CV accuracy of 95%.
- The CV scores show that model performance can vary depending on the data split.
- Standard deviation helps measure the consistency of performance across folds.

## Learning Outcome

This experiment demonstrated why model validation is important before trusting a Machine Learning model on unseen data. Cross-validation provides multiple evaluation results instead of relying on a single train-test split.

## Files

- `day25_cross_validation.ipynb`
- `day25_cross_validation_comparison.csv`
- `day25_model_cv_comparison.csv`

## Tools Used

Python, Pandas, NumPy, Scikit-learn, Matplotlib