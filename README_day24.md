# Day 24 - PCA Dimensionality Reduction

## Objective
Apply Principal Component Analysis (PCA) to reduce the number of features while analyzing how much information is retained.

## Dataset
The dataset contains 100 customer records with 5 input features:

- Age
- Income
- Purchase_Amount
- Savings
- Credit_Score

## PCA
The original 5 features were reduced to 2 principal components:

- PC1
- PC2

## Explained Variance

| Component | Variance |
|---|---:|
| PC1 | 25.08% |
| PC2 | 21.78% |
| Total | 46.86% |

The two components retained 46.86% of the total variance.

## Model Performance

| Feature Representation | Features | Accuracy |
|---|---:|---:|
| Original Features | 5 | 100% |
| PCA Components | 2 | 65% |

## Key Learning
PCA can simplify high-dimensional datasets and make visualization easier. However, reducing the number of components too much can remove useful information and affect model performance.

In this experiment, reducing 5 features to 2 components reduced accuracy from 100% to 65%.

## Files

- `day24_pca_dimensionality_reduction.ipynb`
- `day24_pca_performance_comparison.csv`
- `day24_pca_variance_analysis.csv`
- `README_day24.md`