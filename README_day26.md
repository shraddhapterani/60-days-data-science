# File name: README_day26.md

readme_content = """
# Day 26 - Hyperparameter Tuning

## Objective
Optimize a Random Forest model using hyperparameter tuning and compare it with the baseline model.

## Model Used
Random Forest Classifier

## Baseline Performance
- Mean 5-Fold CV Accuracy: 0.98
- Standard Deviation: 0.0245
- n_estimators: 100

## Hyperparameter Tuning
GridSearchCV was used with 5-fold cross-validation.

Parameters tested:
- n_estimators: 50, 100, 200
- max_depth: 3, 5, 10, None

## Best Parameters
- n_estimators: 50
- max_depth: 3
- Best CV Accuracy: 0.98

## Performance Comparison
- Baseline Random Forest: 0.98
- Tuned Random Forest: 0.98

## Key Observation
Hyperparameter tuning did not increase the measured CV accuracy.
However, GridSearchCV identified a simpler Random Forest configuration
with the same accuracy.

## Optimization Tradeoff
A smaller number of trees and limited tree depth can reduce model
complexity while maintaining the same measured performance on this dataset.

## Files
- day26_hyperparameter_tuning.ipynb
- day26_performance_comparison.csv
- day26_best_parameters.csv
- README_day26.md

## Tools
Python, Pandas, NumPy, Scikit-learn, Matplotlib
"""

with open("README_day26.md", "w") as file:
    file.write(readme_content)

print("README_day26.md created successfully!")