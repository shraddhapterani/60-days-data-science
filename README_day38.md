# Day 38 – Customer Retention & Lifetime Value Analysis

## ABTalks 60 Days Data Science Challenge

### 📌 Project Overview

Day 38 focuses on **Customer Retention Analytics** and **Customer Lifetime Value (CLV)**.

The goal is to understand customer purchasing behavior, identify valuable customers, measure retention status, and generate business recommendations for improving long-term customer value.

---

## 🎯 Objectives

- Calculate customer retention metrics
- Estimate Customer Lifetime Value (CLV)
- Identify high-value customers
- Analyze customer retention status
- Visualize CLV and retention patterns
- Generate business-oriented retention recommendations

---

## 📊 Dataset Overview

The analysis was performed using customer order and sales data.

| Metric | Value |
|---|---:|
| Unique Customers | 793 |
| Total Orders | 4,922 |
| Total Sales | 2,261,536.78 |
| Date Range | 2015-01-03 to 2018-12-30 |
| Missing Customer IDs | 0 |
| Missing Order Dates | 0 |
| Missing Sales Values | 0 |

---

## 🔍 Customer Metrics

For each customer, the following metrics were calculated:

- First Purchase
- Last Purchase
- Total Orders
- Total Sales
- Recency Days
- Customer Lifetime Days
- Purchase Frequency
- Average Order Value
- Estimated CLV
- Retention Status

---

## 💰 Customer Lifetime Value

Customer Lifetime Value was estimated using:

**Estimated CLV = Average Order Value × Purchase Frequency × Expected Lifetime**

Purchase frequency was calculated using customer lifetime while preventing unusually high frequency values for customers with very short observed lifetimes.

This provides an estimate of the potential long-term revenue associated with each customer.

---

## 🏆 Top Customers by Estimated CLV

The analysis identified the following customers among the highest estimated CLV group:

| Customer ID | Estimated CLV |
|---|---:|
| RB-19360 | 30,541.49 |
| TC-20980 | 27,816.24 |
| CJ-12010 | 25,956.79 |
| CC-12370 | 24,459.18 |
| SM-20320 | 21,029.25 |
| PF-19120 | 19,808.06 |
| AB-10105 | 14,881.28 |
| BS-11365 | 14,780.60 |
| SC-20095 | 14,499.86 |
| BM-11140 | 14,312.24 |

---

## 🔄 Customer Retention Analysis

Customers were categorized into three retention groups:

| Retention Status | Customers |
|---|---:|
| Active | 434 |
| Inactive | 202 |
| At Risk | 157 |

This shows that the dataset contains customers at different stages of engagement, allowing targeted retention strategies.

---

## 📈 CLV by Retention Status

Average estimated CLV by retention status:

| Retention Status | Average Estimated CLV |
|---|---:|
| Active | 3,187.55 |
| At Risk | 3,226.21 |
| Inactive | 3,298.97 |

The analysis shows that average estimated CLV is relatively close across the three retention groups. Therefore, retention status and customer value should be considered together when planning customer retention campaigns.

---

## 📊 Visualizations

The analysis includes:

1. Top 10 Customers by Estimated Lifetime Value
2. Customer Retention Status Distribution
3. Average Estimated CLV by Retention Status

These visualizations help communicate customer value and retention patterns clearly.

---

## 💡 Business Recommendations

### 1. Active Customers
- Reward loyal customers with personalized offers.
- Encourage repeat purchases through loyalty programs.

### 2. At-Risk Customers
- Send targeted offers and reminders.
- Prioritize high-CLV customers for retention campaigns.

### 3. Inactive Customers
- Run re-engagement campaigns.
- Offer personalized discounts to encourage return purchases.

### 4. High-Value Customers
- Provide loyalty benefits and personalized recommendations.
- Focus retention efforts on customers with high Estimated CLV.

---

## 🧠 Key Learnings

- Customer retention analytics helps businesses understand long-term customer behavior.
- CLV can be used to identify customers with greater potential long-term value.
- Recency, purchase frequency, and order value provide useful customer-level insights.
- Combining retention status with CLV can help businesses create more targeted retention strategies.
- Data analytics can transform customer transaction data into actionable business decisions.

---

## 🛠️ Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

---

## 📁 Project Files

```text
day38_customer_retention_clv.ipynb
README_day38.md
```

---

## 🚀 Outcome

Day 38 strengthened my understanding of **customer retention analytics, Customer Lifetime Value, customer segmentation, and data-driven business decision-making**.

The analysis demonstrates how customer transaction data can be transformed into meaningful insights that support retention and long-term customer value strategies.

---

### #ABTalks #DataScience #CustomerAnalytics #CLV #CustomerRetention #Python #DataAnalytics