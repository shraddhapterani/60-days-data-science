# Day 21 — Sprint Review & Model Selection

## Objective
Compare Random Forest and XGBoost and select the best model for fraud detection.

## Results

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Random Forest | 92.50% | 90.28% | 89.04% | 89.66% | 91.29% |
| XGBoost | 91.75% | 88.44% | 89.04% | 88.74% | 91.31% |

## Selected Model

**Random Forest**

Random Forest was selected because it achieved higher accuracy, precision, and F1-score while matching XGBoost on recall.

XGBoost had a slightly higher ROC-AUC, but the difference was only 0.000135.

Random Forest also produced fewer false positives (14 vs 17).

## Key Learning

Model selection should be based on business requirements and multiple evaluation metrics, not accuracy alone.

## Files

- `day21_sprint_review_model_selection.ipynb`
- `day21_final_model_comparison.csv`
- `README_day21.md`