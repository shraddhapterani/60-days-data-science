# Day 12 – Regression Modeling 🚀

## Objective
Built and evaluated Linear Regression models to predict continuous Sales values using the Superstore dataset.

## What I Did
- Selected input features and Sales as the target
- Built a baseline Linear Regression model
- Generated predictions on test data
- Calculated prediction errors
- Interpreted model coefficients
- Visualized regression predictions and errors
- Built an improved regression model using multiple features
- Compared baseline and improved model performance

## Baseline Model
Feature used:
- Shipping Days

Mean Absolute Error:
- 303.06

## Improved Model
Features used:
- Shipping Days
- Order Year
- Category
- Sub-Category
- Region
- Ship Mode
- Segment

After One-Hot Encoding:
- 33 features

Mean Absolute Error:
- 238.77

## Model Improvement
The improved model reduced MAE from 303.06 to 238.77.

Improvement:
- 21.21%

## Visualizations
- Regression line
- Prediction errors
- Actual vs Predicted Sales
- Perfect prediction reference line

## Key Learning
Regression models learn relationships between input features and a continuous numerical target.

Using more meaningful features improved prediction performance compared with using Shipping Days alone.

## Output
Prediction results were saved as:

`day12_regression_predictions.csv`