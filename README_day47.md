# Day 47/60 — Customer Intelligence Platform Capstone

## 1. Project Overview
The Customer Intelligence Platform is an end-to-end Data Science project that helps businesses understand customer behaviour, identify customers at risk, forecast sales, and make data-driven decisions.

## 2. Business Problem
Businesses collect large amounts of sales data but may struggle to identify valuable customers, understand purchasing patterns, anticipate future sales, and decide which customers need retention campaigns.

## 3. Proposed Solution
Build an integrated analytics platform that processes sales data, performs customer analysis, generates forecasts and risk indicators, and presents actionable insights through an interactive dashboard.

## 4. Dataset
**Primary dataset:** `superstore_sales.csv`

- Records: 9,800
- Columns: 18
- Important fields: Order Date, Customer ID, Segment, Region, Category, Sub-Category, and Sales.

Supporting files from previous challenge days may be reused after checking their structure and compatibility.

## 5. Business Objectives
- Analyse customer purchasing behaviour and value.
- Segment customers into meaningful groups.
- Identify customers with elevated risk indicators.
- Forecast future sales or customer activity.
- Recommend retention strategies.
- Present business KPIs and insights in a dashboard.

## 6. Planned System Modules
1. Data ingestion and validation
2. Data cleaning and feature engineering
3. Exploratory data analysis
4. Customer segmentation
5. Customer risk analysis
6. Sales or customer activity forecasting
7. Recommendations and retention strategies
8. Interactive business intelligence dashboard
9. API integration and production monitoring
10. Testing, documentation, and deployment

## 7. System Architecture
Sales CSV → Data Processing → Analytics Engine → Business Intelligence → Streamlit Dashboard

Architecture diagram: `day47_customer_intelligence_architecture.drawio`

## 8. Technology Stack
- Python
- Pandas and NumPy
- Scikit-learn
- Plotly
- Streamlit
- FastAPI
- Git and GitHub
- Streamlit Community Cloud

## 9. Project Roadmap: Days 47–60

| Day | Planned work |
|---|---|
| 47 | Define business problem, proposal, architecture, and roadmap |
| 48 | Audit dataset, inspect existing modules, and plan integration |
| 49 | Build a clean project structure and data validation pipeline |
| 50 | Implement customer-level analytics and feature generation |
| 51 | Integrate customer segmentation |
| 52 | Evaluate segments and prepare customer insights |
| 53 | Integrate customer risk analysis |
| 54 | Evaluate risk outputs and define retention recommendations |
| 55 | Integrate sales or customer activity forecasting |
| 56 | Combine analytics modules into a common workflow |
| 57 | Integrate modules into the dashboard |
| 58 | Test API integration, error handling, and reliability |
| 59 | Perform end-to-end testing and complete documentation |
| 60 | Final demonstration, project summary, and presentation |

*The roadmap is provisional and may be adjusted based on dataset suitability, integration results, and evaluation findings.*

## 10. Success Criteria
- Data processing and validation work correctly.
- Analytics modules produce reproducible results.
- Predictions and forecasts are evaluated appropriately.
- Dashboard metrics agree with the underlying data.
- Invalid API inputs are handled safely.
- Documentation explains architecture, results, and limitations.

## 11. Expected Outcome
A documented, integrated Customer Intelligence Platform that transforms sales records into customer insights, risk indicators, forecasts, and business recommendations.

## 12. Key Learning
End-to-end Data Science requires more than building individual models. It requires connecting data processing, analytics, evaluation, visualisation, and reliable application workflows.
