
import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
from pathlib import Path

# --------------------------------------------------
# 1. PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="Customer Risk Analytics",
    page_icon="📊",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "day41_customer_risk_final.csv"
MODEL_FILE = BASE_DIR / "day43_customer_risk_model.pkl"

# --------------------------------------------------
# 2. CUSTOM STYLING
# --------------------------------------------------
st.markdown(
    """
    <style>
    .main {
        background-color: #f7f9fc;
    }
    .block-container {
        padding-top: 1.5rem;
    }
    div[data-testid="stMetric"] {
        background-color: white;
        border: 1px solid #e6eaf0;
        padding: 16px;
        border-radius: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# 3. CACHED DATA AND MODEL LOADING
# --------------------------------------------------
@st.cache_data
def load_customer_data(file_path, modified_time):
    return pd.read_csv(file_path)


@st.cache_resource
def load_prediction_model():
    return joblib.load(MODEL_FILE)


# --------------------------------------------------
# 4. SIDEBAR AND DATA UPLOAD
# --------------------------------------------------
st.sidebar.title("📊 Customer Analytics")
st.sidebar.caption("Customer risk and retention dashboard")

uploaded_file = st.sidebar.file_uploader(
    "Upload customer CSV",
    type=["csv"]
)

try:
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
    else:
        if not DATA_FILE.exists():
            st.error(
                f"Dataset not found: {DATA_FILE.name}. "
                "Upload a customer CSV to continue."
            )
            st.stop()

        data = load_customer_data(
            str(DATA_FILE),
            DATA_FILE.stat().st_mtime
        )

except Exception as error:
    st.error(f"Unable to load the dataset: {error}")
    st.stop()


# --------------------------------------------------
# 5. VALIDATE DATASET
# --------------------------------------------------
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
    if column not in data.columns
]

if missing_columns:
    st.error(
        "The uploaded dataset is missing these columns: "
        + ", ".join(missing_columns)
    )
    st.stop()

# Convert date columns safely
for column in ["Last_Order_Date", "First_Order_Date"]:
    data[column] = pd.to_datetime(
        data[column],
        errors="coerce"
    )

# Convert numeric columns safely
numeric_columns = [
    "Total_Sales",
    "Total_Orders",
    "Average_Order_Value",
    "Recency_Days",
    "Estimated_CLV",
    "Risk_Score"
]

for column in numeric_columns:
    data[column] = pd.to_numeric(
        data[column],
        errors="coerce"
    )

data = data.dropna(
    subset=[
        "Recency_Days",
        "Estimated_CLV",
        "Risk_Score"
    ]
)

if data.empty:
    st.error("No usable customer records were found.")
    st.stop()


# --------------------------------------------------
# 6. NAVIGATION
# --------------------------------------------------
page = st.sidebar.radio(
    "Choose a section",
    [
        "Overview",
        "Customer Analysis",
        "Customer Explorer",
        "Live Risk Prediction"
    ],
    label_visibility="collapsed"
)

st.title("Customer Risk Analytics Dashboard")

st.caption(
    "Explore customer behaviour, understand risk categories, "
    "and test individual customer risk predictions."
)


# --------------------------------------------------
# 7. GLOBAL FILTERS
# --------------------------------------------------
st.sidebar.subheader("Dashboard Filters")

risk_options = sorted(
    data["Risk_Level"].dropna().astype(str).unique().tolist()
)

strategy_options = sorted(
    data["Retention_Strategy"].dropna().astype(str).unique().tolist()
)

selected_risks = st.sidebar.multiselect(
    "Risk Level",
    options=risk_options,
    default=risk_options
)

selected_strategies = st.sidebar.multiselect(
    "Retention Strategy",
    options=strategy_options,
    default=strategy_options
)

minimum_recency = float(data["Recency_Days"].min())
maximum_recency = float(data["Recency_Days"].max())

selected_recency = st.sidebar.slider(
    "Days Since Last Order",
    min_value=minimum_recency,
    max_value=maximum_recency,
    value=(minimum_recency, maximum_recency)
)

filtered_data = data[
    data["Risk_Level"].astype(str).isin(selected_risks)
    & data["Retention_Strategy"].astype(str).isin(selected_strategies)
    & data["Recency_Days"].between(
        selected_recency[0],
        selected_recency[1]
    )
].copy()

# Live prediction does not depend on dashboard filters.
if filtered_data.empty and page != "Live Risk Prediction":
    st.warning("No customers match the selected filters.")
    st.stop()


# --------------------------------------------------
# 8. OVERVIEW
# --------------------------------------------------
if page == "Overview":

    st.header("Business Overview")

    total_customers = len(filtered_data)
    total_sales = filtered_data["Total_Sales"].sum()
    average_clv = filtered_data["Estimated_CLV"].mean()

    high_risk_count = (
        filtered_data["Risk_Level"]
        .astype(str)
        .str.contains("high", case=False, na=False)
        .sum()
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Customers", f"{total_customers:,}")
    col2.metric("Total Sales", f"₹{total_sales:,.2f}")
    col3.metric("Average CLV", f"₹{average_clv:,.2f}")
    col4.metric("High-Risk Customers", f"{high_risk_count:,}")

    st.subheader("Customer Risk Distribution")

    risk_counts = (
        filtered_data["Risk_Level"]
        .value_counts()
        .rename_axis("Risk Level")
        .reset_index(name="Customers")
    )

    fig_risk = px.pie(
        risk_counts,
        names="Risk Level",
        values="Customers",
        hole=0.45,
        title="Customers by Risk Level"
    )

    st.plotly_chart(fig_risk, use_container_width=True)

    st.subheader("Retention Strategy Distribution")

    strategy_counts = (
        filtered_data["Retention_Strategy"]
        .value_counts()
        .rename_axis("Retention Strategy")
        .reset_index(name="Customers")
    )

    fig_strategy = px.bar(
        strategy_counts,
        x="Retention Strategy",
        y="Customers",
        color="Retention Strategy",
        title="Customers by Retention Strategy"
    )

    st.plotly_chart(fig_strategy, use_container_width=True)


# --------------------------------------------------
# 9. CUSTOMER ANALYSIS
# --------------------------------------------------
elif page == "Customer Analysis":

    st.header("Customer Behaviour Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Sales by Risk Level")

        fig_sales = px.box(
            filtered_data,
            x="Risk_Level",
            y="Total_Sales",
            color="Risk_Level",
            title="Sales Distribution"
        )

        st.plotly_chart(fig_sales, use_container_width=True)

    with col2:
        st.subheader("Recency by Risk Level")

        fig_recency = px.box(
            filtered_data,
            x="Risk_Level",
            y="Recency_Days",
            color="Risk_Level",
            title="Days Since Last Order"
        )

        st.plotly_chart(fig_recency, use_container_width=True)

    st.subheader("Filtered Customer Records")
    st.dataframe(filtered_data, use_container_width=True)


# --------------------------------------------------
# 10. CUSTOMER EXPLORER
# --------------------------------------------------
elif page == "Customer Explorer":

    st.header("Explore an Individual Customer")

    customer_ids = (
        filtered_data["Customer ID"]
        .dropna()
        .unique()
        .tolist()
    )

    if not customer_ids:
        st.info("No customer IDs are available for these filters.")
    else:
        selected_customer = st.selectbox(
            "Select Customer ID",
            customer_ids
        )

        customer = filtered_data[
            filtered_data["Customer ID"] == selected_customer
        ].iloc[0]

        st.subheader(f"Customer: {selected_customer}")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Total Sales",
            f"₹{customer['Total_Sales']:,.2f}"
        )

        col2.metric(
            "Total Orders",
            f"{customer['Total_Orders']:,.0f}"
        )

        col3.metric(
            "Estimated CLV",
            f"₹{customer['Estimated_CLV']:,.2f}"
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Days Since Last Order",
            f"{customer['Recency_Days']:,.0f}"
        )

        col2.metric(
            "Risk Score",
            f"{customer['Risk_Score']:.3f}"
        )

        col3.metric(
            "Average Order Value",
            f"₹{customer['Average_Order_Value']:,.2f}"
        )

        st.write("**Risk Level:**", customer["Risk_Level"])
        st.write(
            "**Retention Strategy:**",
            customer["Retention_Strategy"]
        )


# --------------------------------------------------
# 11. LIVE RISK PREDICTION
# --------------------------------------------------
elif page == "Live Risk Prediction":

    st.header("🔮 Live Customer Risk Prediction")

    st.write(
        "Enter customer information below to get an instant "
        "prediction from the saved Random Forest model."
    )

    st.info(
        "This demo uses three model inputs: recency, purchase "
        "frequency and estimated customer lifetime value (CLV). "
        "Use actual values only when they are available."
    )

    with st.form("live_risk_prediction_form"):

        st.subheader("Customer Details")

        recency = st.number_input(
            "Days Since Last Order",
            min_value=0.0,
            value=30.0,
            step=1.0,
            help="Number of days since the customer's last purchase."
        )

        purchase_frequency = st.number_input(
            "Purchase Frequency",
            min_value=0.0,
            value=5.0,
            step=1.0,
            help=(
                "Use the same definition and time period "
                "as the model's training data."
            )
        )

        estimated_clv = st.number_input(
            "Estimated Customer Lifetime Value (₹)",
            min_value=0.0,
            value=2500.0,
            step=100.0,
            help="Estimated lifetime value, using the model's training units."
        )

        submitted = st.form_submit_button(
            "Predict Customer Risk",
            use_container_width=True
        )

    if submitted:

        try:
            model = load_prediction_model()

            # Feature names and order must match model training.
            input_data = pd.DataFrame(
                [{
                    "Recency_Days": recency,
                    "Purchase_Frequency": purchase_frequency,
                    "Estimated_CLV": estimated_clv
                }],
                columns=[
                    "Recency_Days",
                    "Purchase_Frequency",
                    "Estimated_CLV"
                ]
            )

            prediction = model.predict(input_data)[0]
            probabilities = model.predict_proba(input_data)[0]
            classes = model.classes_

            st.divider()
            st.subheader("Prediction Result")

            if prediction == "High Risk":
                st.error(f"Predicted Customer Risk: {prediction}")
                st.write(
                    "Possible next step: review recent customer "
                    "activity and consider an appropriate retention offer."
                )

            elif prediction == "Medium Risk":
                st.warning(f"Predicted Customer Risk: {prediction}")
                st.write(
                    "Possible next step: monitor purchase activity "
                    "and consider a suitable engagement campaign."
                )

            else:
                st.success(f"Predicted Customer Risk: {prediction}")
                st.write(
                    "Possible next step: maintain a positive customer "
                    "experience and encourage repeat purchases."
                )

            # Display the model's class probabilities.
            probability_data = pd.DataFrame({
                "Risk Level": classes,
                "Probability": probabilities
            })

            probability_data["Probability (%)"] = (
                probability_data["Probability"] * 100
            ).round(2)

            col1, col2, col3 = st.columns(3)

            for column, risk_name in zip(
                [col1, col2, col3],
                ["High Risk", "Medium Risk", "Low Risk"]
            ):
                matching = probability_data[
                    probability_data["Risk Level"] == risk_name
                ]

                if not matching.empty:
                    column.metric(
                        f"{risk_name} Probability",
                        f"{matching.iloc[0]['Probability (%)']:.2f}%"
                    )

            fig_probabilities = px.bar(
                probability_data,
                x="Risk Level",
                y="Probability",
                color="Risk Level",
                title="Model-Estimated Probability by Risk Category",
                range_y=[0, 1],
                text=probability_data["Probability"].map(
                    lambda value: f"{value:.1%}"
                )
            )

            fig_probabilities.update_layout(
                yaxis_tickformat=".0%",
                yaxis_title="Estimated Probability",
                xaxis_title="Risk Category"
            )

            st.plotly_chart(
                fig_probabilities,
                use_container_width=True
            )

            st.subheader("Inputs Used")

            st.dataframe(input_data, use_container_width=True)

            st.caption(
                "Important: probabilities are model estimates, not "
                "guarantees. Predictions depend on the training data "
                "and the definitions and units of the input features. "
                "The default values are illustrative, not real customer data."
            )

        except FileNotFoundError:
            st.error(
                f"Saved model not found: {MODEL_FILE.name}. "
                "Place the model file in the project folder."
            )

        except Exception as error:
            st.error(f"Prediction failed: {error}")


# --------------------------------------------------
# 12. DOWNLOAD FILTERED DATA
# --------------------------------------------------
if page != "Live Risk Prediction" and not filtered_data.empty:

    st.divider()
    st.subheader("Export Data")

    csv_data = filtered_data.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Filtered Customer Data (CSV)",
        data=csv_data,
        file_name="filtered_customer_data.csv",
        mime="text/csv"
    )


# --------------------------------------------------
# 13. FOOTER
# --------------------------------------------------
st.divider()

st.caption(
    "Customer Risk Analytics | Data Science Challenge | "
    "Predictions are decision-support estimates."
)
