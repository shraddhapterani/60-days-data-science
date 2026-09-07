# Day 13 - Overfitting and Regularization

## ABTalks 60-Day Data Science Challenge

### Objective

The goal of Day 13 was to understand overfitting and regularization by comparing Linear Regression, Ridge Regression, and Lasso Regression.

### What I Did

- Prepared the Superstore Sales dataset.
- Selected features related to sales prediction.
- Applied one-hot encoding to categorical features.
- Split the data into training and testing sets.
- Trained a baseline Linear Regression model.
- Trained Ridge Regression.
- Trained Lasso Regression.
- Compared training and testing performance.
- Analyzed the train-test R² gap to identify overfitting.
- Checked how Lasso reduced some feature coefficients to zero.

### Dataset

- Rows: 9,800
- Features used: 33 after encoding
- Training data: 7,840 rows
- Testing data: 1,960 rows

### Model Comparison

| Model | Train MAE | Test MAE | Train R² | Test R² |
|---|---:|---:|---:|---:|
| Linear Regression | 198.79 | 238.77 | 0.205 | 0.179 |
| Ridge | 198.77 | 238.78 | 0.205 | 0.178 |
| Lasso | 199.17 | 239.68 | 0.203 | 0.172 |

### Overfitting Analysis

The train-test R² gaps were small:

- Linear Regression: 0.026
- Ridge: 0.026
- Lasso: 0.031

Therefore, there was no strong evidence of overfitting in this experiment.

### Lasso Feature Selection

Lasso reduced 14 out of 33 feature coefficients to approximately zero.

This demonstrates how Lasso can perform feature selection by reducing the importance of less useful features.

### Key Learnings

- Overfitting occurs when a model learns training data too closely and performs poorly on unseen data.
- Training performance alone is not enough to judge a model.
- Ridge reduces the influence of large coefficients.
- Lasso can reduce coefficients to zero and perform feature selection.
- Regularization does not always improve test performance.
- In this experiment, Linear Regression achieved the best test performance.

### Outcome

This experiment helped me understand the difference between memorization and generalization and how Ridge and Lasso regularization affect regression models.