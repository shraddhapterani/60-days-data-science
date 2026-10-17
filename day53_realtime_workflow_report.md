# Day 53 — Real-Time Customer Prediction Workflows

## Objective
To integrate an interactive customer risk prediction workflow into the Customer Risk Analytics Dashboard.

## Features Implemented
- Added a Live Risk Prediction section to the Streamlit dashboard.
- Created an interactive form to accept customer inputs.
- Integrated the saved Random Forest classification model.
- Displayed instant customer risk predictions.
- Visualized model-estimated probabilities for High Risk, Medium Risk, and Low Risk.
- Added input validation and error handling for prediction failures.

## Model Inputs
1. Recency_Days — days since the customer's last order.
2. Purchase_Frequency — purchase frequency.
3. Estimated_CLV — estimated customer lifetime value.

## Sample Prediction
- Recency_Days: 30
- Purchase_Frequency: 5
- Estimated_CLV: 2500
- Predicted Risk: Low Risk
- High Risk Probability: 3%
- Medium Risk Probability: 3%
- Low Risk Probability: 94%

*Note: The values above are illustrative demo inputs, not real customer records. Probabilities are model estimates, not guarantees.*

## Workflow
1. The user opens the Live Risk Prediction section.
2. The user enters customer details.
3. The application prepares the three model features.
4. The saved Random Forest model predicts the risk category.
5. The application displays the predicted category and class probabilities.
6. The user reviews the results to support customer-retention decisions.

## Technologies Used
- Python
- Streamlit
- Pandas
- Plotly
- Scikit-learn
- Joblib

## Outcome
The dashboard now supports interactive customer risk predictions alongside its existing analytics and visualizations.

## Limitation
Prediction quality depends on the model's training data and on using input features with the same definitions and units used during training. The output should support, not replace, business judgement.
