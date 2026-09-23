# Day 29 — Customer Segmentation with K-Means

## Objective

Use unsupervised learning to discover hidden customer groups and understand their business characteristics.

## Dataset

The dataset contains 100 customers with:

- Age
- Income
- Purchase_Amount
- Savings
- Credit_Score

The `Purchased` column was not used for clustering because K-Means is an unsupervised learning algorithm.

## Methodology

### 1. Feature Selection

Selected five customer-related numerical features:

- Age
- Income
- Purchase_Amount
- Savings
- Credit_Score

### 2. Feature Scaling

Used `StandardScaler` because K-Means is distance-based and the features have different numerical ranges.

### 3. K-Means Clustering

Tested different numbers of clusters:

K = 2, 3, 4, 5, 6

### 4. Elbow Method

The inertia values were:

| K | Inertia |
|---|---:|
| 2 | 414.96 |
| 3 | 354.03 |
| 4 | 307.60 |
| 5 | 274.33 |
| 6 | 241.19 |

There was no extremely sharp elbow, so K = 3 was selected for practical interpretability.

## Customer Segments

| Cluster | Segment | Customers | Avg Income | Avg Purchase |
|---|---|---:|---:|---:|
| 0 | Younger High-Spending | 29 | 47,448.24 | 3,762.97 |
| 1 | Higher-Income | 43 | 78,063.02 | 2,668.40 |
| 2 | Older Lower-Spending | 28 | 52,114.29 | 1,908.00 |

## Business Insights

### Cluster 0 — Younger High-Spending

This segment contains relatively younger customers with the highest average purchase amount and savings.

### Cluster 1 — Higher-Income

This is the largest segment. It has the highest average income and credit score.

### Cluster 2 — Older Lower-Spending

This segment has the highest average age and the lowest average purchase amount, savings, and credit score.

These interpretations are based on the synthetic dataset used in this project.

## Key Learnings

- K-Means can discover customer groups without predefined labels.
- Feature scaling is important for distance-based algorithms.
- The Elbow Method can help select a suitable number of clusters.
- Clustering results need business interpretation, not just model output.
- Unsupervised learning can reveal patterns that are not explicitly labeled.

## Output

Business insight report:

`day29_business_insight_report.csv`
