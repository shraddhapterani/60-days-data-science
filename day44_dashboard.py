import streamlit as st
import pandas as pd
import plotly.express as px


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Customer Intelligence Dashboard",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# TITLE
# ============================================================

st.title("📊 Customer Intelligence Dashboard")

st.write(
    "Interactive dashboard for monitoring customer performance, "
    "risk, and retention insights."
)


# ============================================================
# DATA UPLOAD
# ============================================================

st.sidebar.header("📂 Data Source")

uploaded_file = st.sidebar.file_uploader(
    "Upload Customer CSV",
    type=["csv"]
)

if uploaded_file is not None:
    customer_data = pd.read_csv(uploaded_file)
    st.sidebar.success("Uploaded CSV loaded successfully.")
else:
    customer_data = pd.read_csv("day41_customer_risk_final.csv")
    st.sidebar.info("Using default customer risk dataset.")


# ============================================================
# REQUIRED COLUMNS CHECK
# ============================================================

required_columns = [
    "Customer ID",
    "Total_Sales",
    "Total_Orders",
    "Last_Order_Date",
    "First_Order_Date",
    "Average_Order_Value",
    "Recency_Days",
    "Estimated_CLV",
    "Risk_Score",
    "Risk_Level",
    "Retention_Strategy"
]

missing_columns = [
    column
    for column in required_columns
    if column not in customer_data.columns
]

if missing_columns:
    st.error(
        "The uploaded CSV is missing required columns: "
        + ", ".join(missing_columns)
    )
    st.stop()


# ============================================================
# DATE CONVERSION
# ============================================================

customer_data["Last_Order_Date"] = pd.to_datetime(
    customer_data["Last_Order_Date"]
)

customer_data["First_Order_Date"] = pd.to_datetime(
    customer_data["First_Order_Date"]
)

st.success("Customer data loaded successfully.")


# ============================================================
# KPI CALCULATIONS
# ============================================================

total_customers = customer_data["Customer ID"].nunique()

total_sales = customer_data["Total_Sales"].sum()

total_orders = customer_data["Total_Orders"].sum()

average_order_value = customer_data["Average_Order_Value"].mean()

high_risk_customers = (
    customer_data["Risk_Level"] == "High Risk"
).sum()


# ============================================================
# KPI CARDS
# ============================================================

st.subheader("📌 Key Business Metrics")

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Total Customers",
    f"{total_customers:,}"
)

col2.metric(
    "Total Sales",
    f"₹{total_sales:,.2f}"
)

col3.metric(
    "Total Orders",
    f"{total_orders:,}"
)

col4.metric(
    "Average Order Value",
    f"₹{average_order_value:,.2f}"
)

col5.metric(
    "High Risk Customers",
    f"{high_risk_customers:,}"
)


# ============================================================
# CUSTOMER RISK DISTRIBUTION
# ============================================================

st.subheader("⚠️ Customer Risk Distribution")

risk_distribution = (
    customer_data["Risk_Level"]
    .value_counts()
    .reset_index()
)

risk_distribution.columns = [
    "Risk_Level",
    "Customer_Count"
]

fig_risk = px.bar(
    risk_distribution,
    x="Risk_Level",
    y="Customer_Count",
    title="Customers by Risk Level",
    text="Customer_Count"
)

fig_risk.update_layout(
    xaxis_title="Risk Level",
    yaxis_title="Number of Customers"
)

st.plotly_chart(
    fig_risk,
    use_container_width=True
)


# ============================================================
# RETENTION STRATEGY ANALYSIS
# ============================================================

st.subheader("🎯 Retention Strategy Analysis")

retention_distribution = (
    customer_data["Retention_Strategy"]
    .value_counts()
    .reset_index()
)

retention_distribution.columns = [
    "Retention_Strategy",
    "Customer_Count"
]

fig_retention = px.bar(
    retention_distribution,
    x="Retention_Strategy",
    y="Customer_Count",
    title="Customers by Retention Strategy",
    text="Customer_Count"
)

fig_retention.update_layout(
    xaxis_title="Retention Strategy",
    yaxis_title="Number of Customers"
)

st.plotly_chart(
    fig_retention,
    use_container_width=True
)


# ============================================================
# INTERACTIVE CUSTOMER FILTERS
# ============================================================

st.subheader("🔎 Customer Filters")

col1, col2 = st.columns(2)

with col1:
    selected_risk = st.multiselect(
        "Select Risk Level",
        options=customer_data["Risk_Level"].unique(),
        default=customer_data["Risk_Level"].unique()
    )

with col2:
    selected_strategy = st.multiselect(
        "Select Retention Strategy",
        options=customer_data["Retention_Strategy"].unique(),
        default=customer_data["Retention_Strategy"].unique()
    )


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_data = customer_data[
    (customer_data["Risk_Level"].isin(selected_risk))
    &
    (customer_data["Retention_Strategy"].isin(selected_strategy))
]


# ============================================================
# FILTERED CUSTOMER COUNT
# ============================================================

st.write(
    f"Showing **{len(filtered_data)} customers** based on your filters."
)


# ============================================================
# CUSTOMER TABLE
# ============================================================

st.dataframe(
    filtered_data[
        [
            "Customer ID",
            "Total_Sales",
            "Total_Orders",
            "Average_Order_Value",
            "Recency_Days",
            "Estimated_CLV",
            "Risk_Score",
            "Risk_Level",
            "Retention_Strategy"
        ]
    ],
    use_container_width=True
)