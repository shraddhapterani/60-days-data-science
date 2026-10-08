# Day 44 – Interactive Customer Intelligence Dashboard

## Objective

Build an interactive business intelligence dashboard using Streamlit to monitor customer performance, risk, and retention insights.

## Dashboard Architecture

The dashboard follows this workflow:

Customer CSV Data
        ↓
Data Loading & Validation
        ↓
Data Preparation
        ↓
KPI Calculation
        ↓
Risk & Retention Analytics
        ↓
Interactive Filters
        ↓
Customer-Level Insights
        ↓
Business Decision Making

## Main Components

### 1. Data Source

Users can upload a customer CSV file through the Streamlit sidebar.

If no file is uploaded, the dashboard automatically uses:

`day41_customer_risk_final.csv`

The dashboard also validates that the required customer columns are available.

### 2. KPI Monitoring

The dashboard displays:

- Total Customers
- Total Sales
- Total Orders
- Average Order Value
- High Risk Customers

### 3. Customer Risk Analytics

Customers are divided into:

- Low Risk
- Medium Risk
- High Risk

An interactive Plotly chart displays the customer distribution across risk levels.

### 4. Retention Strategy Analytics

The dashboard displays recommended customer retention strategies:

- Maintain Relationship
- Engagement Campaign
- Targeted Re-engagement
- Immediate Retention Campaign

### 5. Interactive Filtering

Users can filter customers by:

- Risk Level
- Retention Strategy

The customer table updates automatically based on the selected filters.

### 6. Customer-Level Insights

The dashboard displays:

- Customer ID
- Total Sales
- Total Orders
- Average Order Value
- Recency
- Estimated CLV
- Risk Score
- Risk Level
- Retention Strategy

## Technologies Used

- Python
- Pandas
- Streamlit
- Plotly

## Business Value

The dashboard converts customer analytics into an interactive decision-support system.

Business users can identify high-risk customers, understand recommended retention actions, filter customer segments, and inspect individual customer information.

## Day 44 Outcome

Successfully built and tested an interactive customer intelligence dashboard with:

- KPI cards
- Risk analytics
- Retention analytics
- CSV upload
- Interactive filters
- Customer-level data exploration