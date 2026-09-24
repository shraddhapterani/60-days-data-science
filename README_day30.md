# Day 30 — Clustering Optimization

## Objective

Optimize the customer segmentation system by comparing different numbers of clusters using the Elbow Method and Silhouette Score.

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

Selected five numerical customer behavior features:

- Age
- Income
- Purchase_Amount
- Savings
- Credit_Score

### 2. Feature Scaling

Used `StandardScaler` because K-Means is distance-based and the features have different numerical ranges.

### 3. Clustering Optimization

Tested:

- K = 2
- K = 3
- K = 4
- K = 5
- K = 6

For each K, calculated:

- Inertia
- Silhouette Score

## Clustering Quality Results

| K | Inertia | Silhouette Score |
|---|---:|---:|
| 2 | 414.96 | 0.1581 |
| 3 | 354.03 | 0.1679 |
| 4 | 307.60 | 0.1741 |
| 5 | 274.33 | 0.1776 |
| 6 | 241.19 | 0.1964 |

## Optimization Decision

The Elbow Method did not show a very sharp elbow.

The Silhouette Score increased across the tested values and reached its highest value at:

**K = 6**

Therefore, K = 6 was selected as the metric-supported choice among the tested cluster counts.

The Silhouette Score of 0.1964 is relatively low, indicating that the customer groups are not strongly separated. Therefore, K = 6 should not be interpreted as a perfect segmentation.

## Final Customer Segments

| Cluster | Segment | Customers |
|---|---|---:|
| 0 | Older Low-Spending | 14 |
| 1 | Young Moderate-Spending | 18 |
| 2 | Young Strong-Credit | 19 |
| 3 | High-Income High-Spending | 11 |
| 4 | High-Savings High-Spending | 17 |
| 5 | High-Income High-Savings | 21 |

## Business Segmentation Strategy

### Older Low-Spending

Older customers with relatively lower purchase amounts and lower credit scores.

### Young Moderate-Spending

Younger customers with relatively high income and moderate purchase behavior.

### Young Strong-Credit

Younger customers with the highest average credit score among the six segments.

### High-Income High-Spending

Customers with high income and high purchase amounts.

### High-Savings High-Spending

Customers with high savings and high purchase amounts.

### High-Income High-Savings

Customers with the highest average income and strong savings levels.

## Key Learnings

- The number of clusters should be evaluated rather than chosen arbitrarily.
- The Elbow Method helps examine clustering compactness.
- Silhouette Score helps evaluate cluster separation.
- A higher metric does not automatically mean the segmentation is perfect.
- Business interpretation is important when evaluating clustering results.
- ML metrics and business usefulness should both be considered when designing segmentation strategies.

## Output Files

- `day30_clustering_quality_results.csv`
- `day30_segmentation_strategy_report.csv`