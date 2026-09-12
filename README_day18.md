@"
# Day 18 - Fraud Detection Using Random Forest

## Objective
Build a Random Forest classifier for fraud detection and compare it with a Decision Tree.

## Dataset
Synthetic fraud detection dataset with 2000 transactions and 5 input features:
- Transaction Amount
- Transaction Frequency
- Account Age
- International Transaction
- Failed Attempts

## Models
- Decision Tree Classifier
- Random Forest Classifier with 100 trees

## Results
- Decision Tree Accuracy: 91.75%
- Random Forest Accuracy: 92.50%
- Improvement: 0.75%
- Mean Cross-Validation Accuracy: 93.95%
- Cross-Validation Standard Deviation: 1.30%

## Feature Importance
The most important feature was:
- Transaction Frequency: 0.283

## Robustness
The Random Forest achieved a mean cross-validation accuracy of 93.95% with a standard deviation of 1.3%, indicating stable performance across the folds.

## Key Learning
Random Forest combines multiple decision trees to improve stability and reduce the risk of overfitting compared with a single decision tree. Fraud detection also requires careful handling of false positives and false negatives.

## Files
- day18_random_forest_fraud_detection.ipynb
- day18_feature_importance.csv
- README_day18.md
"@ | Set-Content -Encoding UTF8 README_day18.md