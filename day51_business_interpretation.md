# Day 51/60 — Explaining Customer Predictions with Explainable AI

## 1. Objective

The objective of this task is to understand why the customer risk classification model predicts Low Risk, Medium Risk, or High Risk. Logistic Regression coefficients are used to explain overall feature importance and individual customer predictions.

## 2. Dataset Overview

- Total customer records: 793
- Input features: 7
- Target variable: `Risk_Level`
- Low Risk: 265 customers
- High Risk: 264 customers
- Medium Risk: 264 customers
- Missing values in selected features: 0

## 3. Model Performance

The tuned Logistic Regression model achieved:

- Cross-validation macro F1-score: 0.9810
- Test accuracy: 97.48%
- Test macro F1-score: 0.9747

## 4. Global Feature Importance

The mean absolute Logistic Regression coefficients produced the following ranking:

1. Recency_Days — 29.3466
2. Purchase_Frequency — 3.0582
3. Average_Order_Value — 1.0050
4. Total_Sales — 0.6710
5. Total_Orders — 0.6593
6. Estimated_CLV — 0.3610
7. Customer_Lifetime_Days — 0.2527

**Key finding:** `Recency_Days` has the largest coefficient magnitude by a substantial margin. The model relies heavily on the time elapsed since a customer's last order.

## 5. Feature Influence by Risk Category

- **High Risk:** `Recency_Days` has a strong positive coefficient of 38.5229.
- **Low Risk:** `Recency_Days` has a strong negative coefficient of -44.0199.
- **Medium Risk:** `Recency_Days` has a positive coefficient of 5.4970.
- `Purchase_Frequency` has a negative coefficient for High Risk (-4.5701) and a positive coefficient for Low Risk (4.5873).

These coefficients describe changes in class scores when standardised features change, holding other features constant. They do not establish causation.

## 6. Individual Customer Explanation

For one test customer, the model predicted **High Risk**.

The customer's `Recency_Days` value was 811 days, contributing approximately +142.0783 to the High Risk class score. This contribution was much larger than those of the other features for this customer.

**Business interpretation:** The long period since the customer's last order strongly influenced the model towards High Risk. A business could consider reviewing such customers for an appropriate re-engagement campaign.

## 7. Business Recommendations

- Prioritise reviewing customers who have not ordered for a long time.
- Consider targeted reminders or personalised offers for inactive customers.
- Monitor purchase frequency alongside recency when planning customer engagement.
- Evaluate campaign results before assuming that a particular intervention reduces risk.

## 8. Limitations

- The model predicts the dataset's existing `Risk_Level` labels; these have not been verified as future churn outcomes.
- Feature importance shows model reliance, not causal relationships.
- Logistic Regression coefficients explain class scores, not probability changes directly.
- Further validation on new data is needed before using predictions for real business decisions.

## 9. Deliverables

- `day51_explainable_ai.ipynb`
- `day51_feature_importance.png`
- `day51_risk_category_coefficients.png`
- `day51_local_explanation.png`
- `day51_business_interpretation.md`

## Conclusion

The Explainable AI analysis identifies `Recency_Days` as the dominant feature influencing customer risk predictions. The coefficient analysis and individual customer explanation make the model's behaviour easier to communicate to business stakeholders.
