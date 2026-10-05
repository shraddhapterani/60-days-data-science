# Day 41 — Predictive Customer Risk Analysis

## Phase
Predictive Business Analytics

## Objective

Build a predictive customer risk system by combining customer behavior, recency, purchase frequency, estimated Customer Lifetime Value (CLV), and risk scoring to identify customers who may require retention actions.

## Dataset

The analysis uses the Superstore sales dataset.

Customer-level metrics were created from transaction data, including:

- Total Sales
- Total Orders
- Average Order Value
- First Order Date
- Last Order Date
- Customer Lifetime Days
- Recency Days
- Purchase Frequency
- Estimated CLV

## Risk Analysis

Customers were classified into three risk levels:

- Low Risk — 265 customers
- Medium Risk — 264 customers
- High Risk — 264 customers

## Retention Strategy

Retention strategies were assigned based on customer risk and estimated CLV.

| Retention Strategy | Customers |
|---|---:|
| Maintain Relationship | 265 |
| Engagement Campaign | 264 |
| Targeted Re-engagement | 254 |
| Immediate Retention Campaign | 10 |

## Key Business Insight

The analysis identified 10 customers requiring an Immediate Retention Campaign. These customers combine high customer risk with high estimated CLV and should receive the highest retention priority.

## Recommendations

1. Prioritize high-risk, high-value customers for immediate retention campaigns.
2. Use targeted re-engagement campaigns for other high-risk customers.
3. Use engagement campaigns to prevent medium-risk customers from becoming high risk.
4. Continue relationship-building activities for low-risk customers.
5. Regularly monitor customer risk scores to support proactive retention decisions.

## Output Files

- `day41_predictive_customer_risk.ipynb`
- `day41_customer_risk_scores.csv`
- `day41_customer_risk_final.csv`

## Business Impact

This predictive customer risk system helps businesses move from reactive churn management toward proactive customer retention by combining behavioral signals, risk scoring, and customer lifetime value.

## Key Learning

Day 41 demonstrated how multiple customer analytics signals can be integrated into a predictive business system that helps organizations prioritize retention efforts and make data-driven decisions.

#ABTalks #DataScience #PredictiveAnalytics #CustomerRetention #BusinessAnalytics