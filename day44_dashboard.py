
import streamlit as st
import pandas as pd
import plotly.express as px

# ============================================================
# 1. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Customer Intelligence Platform",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# 2. PROFESSIONAL UI STYLING
# ============================================================

st.markdown("""
<style>
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
        max-width: 1500px;
    }

    [data-testid="stMetric"] {
        background: #f5f8fc;
        border: 1px solid #e0e7f0;
        padding: 16px;
        border-radius: 12px;
    }

    [data-testid="stMetricLabel"] {
        color: #52627a;
        font-weight: 600;
    }

    h1, h2, h3 {
        color: #17365d;
    }

    .section-note {
        color: #607086;
        font-size: 0.95rem;
    }

    div[data-testid="stDataFrame"] {
        border: 1px solid #e0e7f0;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# 3. SIDEBAR: DATA SOURCE AND NAVIGATION
# ============================================================

st.sidebar.title("📊 Customer Intelligence")
st.sidebar.caption("Customer analytics and risk insights")
st.sidebar.divider()

st.sidebar.subheader("📂 Data Source")

uploaded_file = st.sidebar.file_uploader(
    "Upload customer CSV",
    type=["csv"],
    help="Upload a CSV containing customer risk and retention information."
)

DEFAULT_DATA_PATH = "day41_customer_risk_final.csv"

if uploaded_file is not None:
    try:
        customer_data = pd.read_csv(uploaded_file)
        st.sidebar.success("Uploaded dataset loaded.")
    except Exception as error:
        st.error(f"Could not read the uploaded CSV: {error}")
        st.stop()
else:
    try:
        customer_data = pd.read_csv(DEFAULT_DATA_PATH)
        st.sidebar.info("Using the default customer dataset.")
    except FileNotFoundError:
        st.error(
            f"Dataset not found: {DEFAULT_DATA_PATH}. "
            "Place the CSV in your project folder or upload it using the sidebar."
        )
        st.stop()
    except Exception as error:
        st.error(f"Could not load the default dataset: {error}")
        st.stop()

# ============================================================
# 4. VALIDATE AND PREPARE DATA
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
    column for column in required_columns
    if column not in customer_data.columns
]

if missing_columns:
    st.error(
        "The dataset is missing required columns: "
        + ", ".join(missing_columns)
    )
    st.stop()

customer_data = customer_data.copy()

numeric_columns = [
    "Total_Sales",
    "Total_Orders",
    "Average_Order_Value",
    "Recency_Days",
    "Estimated_CLV",
    "Risk_Score"
]

for column in numeric_columns:
    customer_data[column] = pd.to_numeric(
        customer_data[column], errors="coerce"
    )

for column in ["Last_Order_Date", "First_Order_Date"]:
    customer_data[column] = pd.to_datetime(
        customer_data[column], errors="coerce"
    )

customer_data["Risk_Level"] = (
    customer_data["Risk_Level"].fillna("Unknown").astype(str)
)
customer_data["Retention_Strategy"] = (
    customer_data["Retention_Strategy"].fillna("Unassigned").astype(str)
)

if customer_data.empty:
    st.warning("The dataset contains no customer records.")
    st.stop()

st.sidebar.caption(f"Loaded records: {len(customer_data):,}")

# ============================================================
# 5. NAVIGATION
# ============================================================

st.sidebar.divider()
st.sidebar.subheader("🧭 Navigation")

page = st.sidebar.radio(
    "Choose a section",
    [
        "Overview",
        "Customer Analysis",
        "Customer Explorer"
    ],
    label_visibility="collapsed"
)

st.sidebar.divider()
st.sidebar.caption("Day 52/60 | ABTalks Data Science Challenge")

# ============================================================
# 6. MAIN HEADER
# ============================================================

st.title("📊 Customer Intelligence Platform")
st.markdown(
    '<p class="section-note">'
    'Understand customer performance, risk patterns, and retention opportunities.'
    '</p>',
    unsafe_allow_html=True
)

# ============================================================
# 7. FILTERS
# ============================================================

st.subheader("🔎 Filter Customers")

filter_col1, filter_col2, filter_col3 = st.columns([1, 1, 1.4])

risk_options = sorted(customer_data["Risk_Level"].unique().tolist())
strategy_options = sorted(
    customer_data["Retention_Strategy"].unique().tolist()
)

with filter_col1:
    selected_risks = st.multiselect(
        "Risk level",
        options=risk_options,
        default=risk_options
    )

with filter_col2:
    selected_strategies = st.multiselect(
        "Retention strategy",
        options=strategy_options,
        default=strategy_options
    )

with filter_col3:
    recency_values = customer_data["Recency_Days"].dropna()

    if not recency_values.empty:
        recency_min = int(recency_values.min())
        recency_max = int(recency_values.max())

        selected_recency = st.slider(
            "Days since last order",
            min_value=recency_min,
            max_value=max(recency_min, recency_max),
            value=(recency_min, max(recency_min, recency_max))
        )
    else:
        selected_recency = None
        st.caption("Recency filtering is unavailable for this dataset.")

filtered_data = customer_data[
    customer_data["Risk_Level"].isin(selected_risks)
    & customer_data["Retention_Strategy"].isin(selected_strategies)
].copy()

if selected_recency is not None:
    filtered_data = filtered_data[
        filtered_data["Recency_Days"].between(
            selected_recency[0],
            selected_recency[1]
        )
    ]

st.caption(
    f"Showing {len(filtered_data):,} of "
    f"{len(customer_data):,} customer records after filtering."
)

if filtered_data.empty:
    st.warning("No customers match these filters. Try changing your selections.")
    st.stop()

# ============================================================
# 8. KPI METRICS
# ============================================================

if page == "Overview":
    st.subheader("📌 Key Business Metrics")

    total_customers = filtered_data["Customer ID"].nunique()
    total_sales = filtered_data["Total_Sales"].sum()
    total_orders = filtered_data["Total_Orders"].sum()
    average_order_value = filtered_data["Average_Order_Value"].mean()
    high_risk_customers = (
        filtered_data["Risk_Level"] == "High Risk"
    ).sum()

    kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

    kpi1.metric("Customers", f"{total_customers:,}")
    kpi2.metric("Total Sales", f"₹{total_sales:,.2f}")
    kpi3.metric("Total Orders", f"{total_orders:,.0f}")
    kpi4.metric(
        "Average Order Value",
        f"₹{average_order_value:,.2f}"
        if pd.notna(average_order_value) else "N/A"
    )
    kpi5.metric("High Risk Customers", f"{high_risk_customers:,}")

    st.caption("Metrics reflect the currently selected filters.")

    # --------------------------------------------------------
    # Risk distribution
    # --------------------------------------------------------

    st.divider()
    st.subheader("⚠️ Customer Risk Distribution")
    st.write("Compare the number of customers in each risk category.")

    risk_distribution = (
        filtered_data["Risk_Level"]
        .value_counts()
        .rename_axis("Risk Level")
        .reset_index(name="Customer Count")
    )

    risk_colors = {
        "Low Risk": "#2E8B57",
        "Medium Risk": "#E6A23C",
        "High Risk": "#D9534F",
        "Unknown": "#8A94A6"
    }

    fig_risk = px.bar(
        risk_distribution,
        x="Risk Level",
        y="Customer Count",
        color="Risk Level",
        color_discrete_map=risk_colors,
        text="Customer Count",
        title="Customers by Risk Category",
        template="plotly_white"
    )

    fig_risk.update_traces(
        textposition="outside",
        hovertemplate="<b>%{x}</b><br>Customers: %{y}<extra></extra>"
    )
    fig_risk.update_layout(
        showlegend=False,
        xaxis_title="Risk Category",
        yaxis_title="Number of Customers",
        margin=dict(l=15, r=15, t=60, b=15),
        height=380
    )

    st.plotly_chart(fig_risk, use_container_width=True)

    # --------------------------------------------------------
    # Retention strategy
    # --------------------------------------------------------

    st.divider()
    st.subheader("🎯 Retention Strategy Analysis")
    st.write("Explore the retention strategies assigned to customers.")

    retention_distribution = (
        filtered_data["Retention_Strategy"]
        .value_counts()
        .rename_axis("Retention Strategy")
        .reset_index(name="Customer Count")
    )

    fig_retention = px.bar(
        retention_distribution,
        x="Customer Count",
        y="Retention Strategy",
        orientation="h",
        text="Customer Count",
        title="Customers by Retention Strategy",
        template="plotly_white",
        color_discrete_sequence=["#3478C8"]
    )

    fig_retention.update_traces(
        textposition="outside",
        hovertemplate="<b>%{y}</b><br>Customers: %{x}<extra></extra>"
    )
    fig_retention.update_layout(
        xaxis_title="Number of Customers",
        yaxis_title="Retention Strategy",
        yaxis={"categoryorder": "total ascending"},
        margin=dict(l=15, r=50, t=60, b=15),
        height=420
    )

    st.plotly_chart(fig_retention, use_container_width=True)

# ============================================================
# 9. CUSTOMER ANALYSIS
# ============================================================

elif page == "Customer Analysis":
    st.subheader("📈 Customer Analysis")
    st.write(
        "Explore customer sales, order activity, and recency "
        "using the current filters."
    )

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        sales_data = filtered_data.dropna(
            subset=["Risk_Level", "Total_Sales"]
        )

        fig_sales = px.box(
            sales_data,
            x="Risk_Level",
            y="Total_Sales",
            color="Risk_Level",
            color_discrete_map={
                "Low Risk": "#2E8B57",
                "Medium Risk": "#E6A23C",
                "High Risk": "#D9534F"
            },
            title="Sales Distribution by Risk Level",
            template="plotly_white"
        )

        fig_sales.update_layout(
            xaxis_title="Risk Level",
            yaxis_title="Total Sales",
            showlegend=False,
            height=400
        )
        st.plotly_chart(fig_sales, use_container_width=True)

    with chart_col2:
        recency_data = filtered_data.dropna(
            subset=["Risk_Level", "Recency_Days"]
        )

        fig_recency = px.box(
            recency_data,
            x="Risk_Level",
            y="Recency_Days",
            color="Risk_Level",
            color_discrete_map={
                "Low Risk": "#2E8B57",
                "Medium Risk": "#E6A23C",
                "High Risk": "#D9534F"
            },
            title="Days Since Last Order by Risk Level",
            template="plotly_white"
        )

        fig_recency.update_layout(
            xaxis_title="Risk Level",
            yaxis_title="Days Since Last Order",
            showlegend=False,
            height=400
        )
        st.plotly_chart(fig_recency, use_container_width=True)

    st.divider()
    st.subheader("🧾 Filtered Customer Records")

    analysis_columns = [
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

    st.dataframe(
        filtered_data[analysis_columns],
        use_container_width=True,
        hide_index=True
    )

# ============================================================
# 10. CUSTOMER EXPLORER
# ============================================================

elif page == "Customer Explorer":
    st.subheader("👤 Customer Explorer")
    st.write(
        "Search for a customer to inspect their performance and risk details."
    )

    customer_ids = (
        filtered_data["Customer ID"]
        .dropna()
        .astype(str)
        .sort_values()
        .unique()
        .tolist()
    )

    if not customer_ids:
        st.info("No customers with a valid Customer ID match these filters.")
    else:
        selected_customer_id = st.selectbox(
            "Search or select Customer ID",
            options=customer_ids
        )

        customer_matches = filtered_data[
            filtered_data["Customer ID"].astype(str)
            == selected_customer_id
        ]

        if not customer_matches.empty:
            customer = customer_matches.iloc[0]

            st.divider()
            st.markdown(f"### Customer {selected_customer_id}")

            detail1, detail2, detail3, detail4 = st.columns(4)

            detail1.metric(
                "Total Sales",
                f"₹{customer['Total_Sales']:,.2f}"
                if pd.notna(customer["Total_Sales"]) else "N/A"
            )
            detail2.metric(
                "Total Orders",
                f"{customer['Total_Orders']:,.0f}"
                if pd.notna(customer["Total_Orders"]) else "N/A"
            )
            detail3.metric(
                "Days Since Last Order",
                f"{customer['Recency_Days']:,.0f}"
                if pd.notna(customer["Recency_Days"]) else "N/A"
            )
            detail4.metric(
                "Estimated CLV",
                f"₹{customer['Estimated_CLV']:,.2f}"
                if pd.notna(customer["Estimated_CLV"]) else "N/A"
            )

            info_col1, info_col2 = st.columns(2)

            with info_col1:
                st.markdown("#### Risk Information")
                st.write(f"**Risk Level:** {customer['Risk_Level']}")
                st.write(
                    "**Risk Score:** "
                    + (
                        f"{customer['Risk_Score']:.3f}"
                        if pd.notna(customer["Risk_Score"])
                        else "N/A"
                    )
                )

            with info_col2:
                st.markdown("#### Retention Information")
                st.write(
                    f"**Suggested Strategy:** {customer['Retention_Strategy']}"
                )
                st.write(
                    "**Average Order Value:** "
                    + (
                        f"₹{customer['Average_Order_Value']:,.2f}"
                        if pd.notna(customer["Average_Order_Value"])
                        else "N/A"
                    )
                )

            with st.expander("View complete customer record"):
                st.dataframe(
                    customer_matches,
                    use_container_width=True,
                    hide_index=True
                )

# ============================================================
# 11. DOWNLOAD FILTERED DATA
# ============================================================

st.divider()
st.subheader("⬇️ Export Customer Data")

csv_data = filtered_data.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download filtered customers as CSV",
    data=csv_data,
    file_name="day52_filtered_customer_data.csv",
    mime="text/csv"
)

# ============================================================
# 12. FOOTER
# ============================================================

st.divider()
st.caption(
    "Customer Intelligence Platform | Day 52/60 — ABTalks Data Science Challenge"
)
st.caption(
    "Risk classifications and retention strategies are based on the supplied dataset. "
    "Review business context before making customer decisions."
)
