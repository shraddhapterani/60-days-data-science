@"
# Day 17 - Loan Approval Prediction Using Decision Trees

## Objective
Build a Decision Tree classifier to predict loan approval and understand how the model makes decisions.

## Dataset
Synthetic loan dataset with 1000 records and 5 input features:
- Income
- Credit Score
- Loan Amount
- Debt Ratio
- Employment Years

## Model
Decision Tree Classifier with max_depth=4.

## Results
- Training Accuracy: 92.75%
- Testing Accuracy: 89.00%
- Accuracy Difference: 3.75%
- Most Important Feature: Credit Score
- Feature Importance: 0.4447
- No major overfitting detected

## Key Learning
Decision Trees make predictions using branching conditions. Feature importance helps identify which features contribute most to predictions. Limiting tree depth helps control overfitting.

## Files
- day17_decision_tree_loan_approval.ipynb
- day17_feature_importance.csv
- README_day17.md
"@ | Set-Content -Encoding UTF8 README_day17.md