# Day 49/60 — Customer Intelligence Platform: Baseline Prototype

## 1. Objective

Build the first working capstone prototype by integrating preprocessed sales data, existing customer-risk outputs, and customer-growth forecasts into a Streamlit dashboard.

## 2. Integrated Components

- **Data preprocessing:** `day48_superstore_sales_cleaned.csv`
- **Customer risk analysis:** `day41_customer_risk_final.csv`
- **Customer growth forecast:** `day36_customer_growth_forecast.csv`
- **Dashboard:** `day49_capstone_prototype.py`

## 3. Prototype Results

- Sales records: 9,800
- Total sales: $2,261,536.78
- Unique customers in risk dataset: 793
- Low-risk customers: 265
- Medium-risk customers: 264
- High-risk customers: 264

## 4. Features

- Sales summary KPIs
- Sales by product category
- Customer risk distribution
- Customer retention recommendations
- Customer growth forecast visualization

## 5. Validation

The risk counts were verified against the source dataset. The three risk categories contain 793 customers in total, matching the number of unique customer IDs.

## 6. Strengths

- Integrates existing analytics outputs into one interface.
- Uses reusable preprocessing work from Day 48.
- Provides business-oriented sales and retention insights.
- Includes basic input-file and column validation.

## 7. Limitations

- The prototype displays existing predictions rather than retraining models.
- The segmentation report uses a different feature schema and is not integrated.
- Forecasts are existing estimates and may not represent future actual results.
- Additional automated tests and end-to-end validation are needed.

## 8. Next Improvements

- Improve dashboard layout and readability.
- Add integration tests and data-quality checks.
- Investigate compatibility of the segmentation module.
- Improve model evaluation and forecasting validation.
- Prepare the final capstone demonstration.

## 9. Key Learning

A baseline prototype helps identify integration issues early and provides a foundation for iterative improvements.
