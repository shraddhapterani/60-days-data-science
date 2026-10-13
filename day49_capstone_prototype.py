
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="Customer Intelligence Platform",
    page_icon="📊",
    layout="wide"
)

st.title("Customer Intelligence Platform")
st.caption("Day 49 | Baseline Capstone Prototype")

# --------------------------------------------------
# 1. Load preprocessed sales data
# --------------------------------------------------
sales_path = Path("day48_superstore_sales_cleaned.csv")
risk_path = Path("day41_customer_risk_final.csv")
forecast_path = Path("day36_customer_growth_forecast.csv")

if not sales_path.exists() or not risk_path.exists():
    st.error("Required sales or customer-risk dataset is missing.")
    st.stop()

sales = pd.read_csv(sales_path, parse_dates=["Order Date", "Ship Date"])
risk = pd.read_csv(risk_path)

st.success("Sales preprocessing and customer-risk outputs loaded.")

# --------------------------------------------------
# 2. KPI summary
# --------------------------------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Sales Records", f"{len(sales):,}")
col2.metric("Total Sales", f"${sales['Sales'].sum():,.2f}")
col3.metric("Customers at Risk", f"{(risk['Risk_Level'] == 'High Risk').sum():,}")
col4.metric("Unique Customers", f"{risk['Customer ID'].nunique():,}")

# --------------------------------------------------
# 3. Sales analytics
# --------------------------------------------------
st.header("Sales Analytics")

sales_by_category = (
    sales.groupby("Category", as_index=False)["Sales"]
    .sum()
    .sort_values("Sales", ascending=False)
)

fig_sales = px.bar(
    sales_by_category,
    x="Category",
    y="Sales",
    title="Sales by Product Category",
    text_auto=".2s"
)
st.plotly_chart(fig_sales, use_container_width=True)

# --------------------------------------------------
# 4. Customer risk analysis
# --------------------------------------------------
st.header("Customer Risk Analysis")

risk_counts = (
    risk["Risk_Level"]
    .value_counts()
    .rename_axis("Risk Level")
    .reset_index(name="Customers")
)

fig_risk = px.bar(
    risk_counts,
    x="Risk Level",
    y="Customers",
    color="Risk Level",
    title="Customers by Risk Level"
)
st.plotly_chart(fig_risk, use_container_width=True)

st.subheader("Customer Retention Recommendations")

st.dataframe(
    risk[
        [
            "Customer ID",
            "Total_Sales",
            "Recency_Days",
            "Risk_Score",
            "Risk_Level",
            "Retention_Strategy"
        ]
    ].sort_values("Risk_Score", ascending=False),
    use_container_width=True
)

# --------------------------------------------------
# 5. Forecast output
# --------------------------------------------------
st.header("Customer Growth Forecast")

if forecast_path.exists():
    forecast = pd.read_csv(forecast_path, parse_dates=["Date"])

    if {"Date", "Predicted Cumulative Customers"}.issubset(forecast.columns):
        fig_forecast = px.line(
            forecast,
            x="Date",
            y="Predicted Cumulative Customers",
            title="Predicted Cumulative Customers"
        )
        st.plotly_chart(fig_forecast, use_container_width=True)
    else:
        st.warning("Forecast file does not contain the expected columns.")
else:
    st.warning("Customer growth forecast file was not found.")

# --------------------------------------------------
# 6. Prototype limitations
# --------------------------------------------------
st.header("Baseline Prototype: Limitations")

st.write(
    "- This prototype displays existing analytics outputs; "
    "it does not retrain prediction models.\n"
    "- The segmentation report uses a different feature schema "
    "and is not merged into this dashboard.\n"
    "- Forecast values are existing predictions, not guaranteed outcomes.\n"
    "- Further validation and integration testing are required."
)
