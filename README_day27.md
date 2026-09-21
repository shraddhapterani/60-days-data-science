# File name: README_day27.md

readme_content = """
# Day 27 - Bias-Variance Analysis

## Objective
Understand model generalization by comparing training and validation
performance and analyzing learning behavior.

## Model Used
Decision Tree Classifier

## Model Complexity Analysis

Different tree depths were tested:

- Max Depth 1: Training Accuracy = 0.975, Validation Accuracy = 1.00
- Max Depth 3: Training Accuracy = 1.00, Validation Accuracy = 1.00
- Max Depth 5: Training Accuracy = 1.00, Validation Accuracy = 1.00
- Max Depth 10: Training Accuracy = 1.00, Validation Accuracy = 1.00

## Learning Curve Analysis

Training accuracy remained at 1.00 across all training sizes.

Validation accuracy improved as more training samples were used:

- 8 samples: 0.65
- 26 samples: 0.96
- 44 samples: 0.97
- 62 samples: 0.99
- 80 samples: 1.00

## Bias-Variance Observation

The model did not show a clear overfitting pattern in the
model-complexity experiment because validation accuracy remained high.

The learning curve showed that validation performance improved
substantially as the number of training samples increased.

## Generalization Observation

The results demonstrate that model performance on unseen data can
improve as more representative training data becomes available.

## Visualizations

- Training vs Validation Accuracy by Tree Depth
- Learning Curve for Decision Tree

## Files

- day27_bias_variance_analysis.ipynb
- day27_learning_curve_results.csv
- day27_model_complexity_comparison.csv
- README_day27.md

## Tools

Python, Pandas, NumPy, Scikit-learn, Matplotlib
"""

with open("README_day27.md", "w") as file:
    file.write(readme_content)

print("README_day27.md created successfully!")