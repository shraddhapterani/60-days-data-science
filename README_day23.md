# Day 23 - Feature Selection

## Objective
Identify important features, remove low-impact variables, and compare model performance before and after feature selection.

## Feature Importance

Random Forest identified the following important features:

- Purchase_Amount: 0.820
- Age: 0.143
- City: 0.015
- Gender: 0.012
- Payment_Method: 0.011

## Selected Features

The selected features were:

- Age
- Purchase_Amount

City, Gender, and Payment_Method were removed because they had very low feature importance.

## Performance Comparison

| Model | Features Before | Features After | Accuracy Before | Accuracy After |
|---|---:|---:|---:|---:|
| Random Forest | 5 | 2 | 100% | 100% |

## Key Learning

Feature selection can reduce the number of input variables while maintaining model performance. In this dataset, reducing the features from 5 to 2 did not change the accuracy.

## Files

- `day23_feature_selection.ipynb`
- `day23_feature_importance.csv`
- `day23_feature_selection_comparison.csv`
- `README_day23.md`