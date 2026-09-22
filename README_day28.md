# Day 28 — Optimized ML Pipeline

## Objective

Build a complete machine learning pipeline by combining feature engineering, preprocessing, validation, and hyperparameter tuning.

## Dataset

The dataset contains 100 customer records with:

- Age
- Income
- Purchase_Amount
- Savings
- Credit_Score
- Purchased

## Feature Engineering

Created:

`Income_per_Age = Income / Age`

Final feature count: **6**

## ML Pipeline

The pipeline combines:

1. Missing-value preprocessing using median imputation
2. Random Forest classification
3. 5-fold cross-validation
4. Hyperparameter tuning using GridSearchCV

## Best Parameters

- `n_estimators = 100`
- `max_depth = 3`

## Results

| Model | CV Accuracy |
|---|---:|
| Random Forest (Day 25) | 98.00% |
| Tuned Random Forest (Day 26) | 98.00% |
| Optimized ML Pipeline (Day 28) | 96.25% |

### Test Performance

Optimized ML Pipeline Test Accuracy: **100%**

## Key Finding

The optimized pipeline did not improve the cross-validation score compared with the earlier Random Forest models.

However, it successfully combined preprocessing, feature engineering, validation, and tuning into one reproducible workflow.

## Engineering Tradeoff

The main improvement was in **workflow design and reproducibility**, rather than CV accuracy.

This demonstrates that production-oriented machine learning involves both model performance and reliable engineering practices.

## Key Learnings

- Feature engineering can improve the information available to a model.
- Cross-validation helps evaluate generalization.
- GridSearchCV automates hyperparameter selection.
- Pipelines combine multiple ML steps into one reproducible workflow.
- Model improvements should be based on measured results.
- A production ML system should be maintainable and reproducible.