
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------
# Day 54: Executive Business Visualizations
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "day41_customer_risk_final.csv"
OUTPUT_DIR = BASE_DIR / "day54_visualizations"

OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_FILE)

required_columns = [
    "Customer ID",
    "Risk_Level",
    "Retention_Strategy",
    "Total_Sales",
    "Estimated_CLV",
    "Recency_Days",
    "Total_Orders",
]

missing = [col for col in required_columns if col not in df.columns]

if missing:
    raise ValueError(f"Missing required columns: {missing}")

# Ensure numerical columns are numeric.
numeric_columns = [
    "Total_Sales",
    "Estimated_CLV",
    "Recency_Days",
    "Total_Orders",
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.dropna(subset=numeric_columns + ["Risk_Level"])

# --------------------------------------------------
# 1. Executive KPI summary
# --------------------------------------------------

summary = df.groupby("Risk_Level").agg(
    Customers=("Customer ID", "count"),
    Total_Sales=("Total_Sales", "sum"),
    Average_Sales=("Total_Sales", "mean"),
    Total_Estimated_CLV=("Estimated_CLV", "sum"),
    Average_CLV=("Estimated_CLV", "mean"),
    Average_Recency_Days=("Recency_Days", "mean"),
    Average_Orders=("Total_Orders", "mean"),
)

summary["Sales_Share_Percent"] = (
    summary["Total_Sales"] / df["Total_Sales"].sum() * 100
)

summary["CLV_Share_Percent"] = (
    summary["Total_Estimated_CLV"]
    / df["Estimated_CLV"].sum()
    * 100
)

summary = summary.round(2)

print("\nEXECUTIVE SUMMARY BY RISK")
print(summary.to_string())

summary.to_csv(OUTPUT_DIR / "day54_risk_summary.csv")

# --------------------------------------------------
# 2. Risk distribution
# --------------------------------------------------

risk_counts = df["Risk_Level"].value_counts()

fig, ax = plt.subplots(figsize=(8, 5))
risk_counts.plot(kind="bar", ax=ax)

ax.set_title("Customer Distribution by Risk Level")
ax.set_xlabel("Risk Level")
ax.set_ylabel("Number of Customers")
ax.tick_params(axis="x", rotation=0)

fig.tight_layout()
fig.savefig(
    OUTPUT_DIR / "day54_risk_distribution.png",
    dpi=200,
    bbox_inches="tight",
)
plt.close(fig)

# --------------------------------------------------
# 3. Sales contribution by risk
# --------------------------------------------------

sales_by_risk = df.groupby("Risk_Level")["Total_Sales"].sum()

fig, ax = plt.subplots(figsize=(8, 5))
sales_by_risk.plot(kind="bar", ax=ax)

ax.set_title("Total Sales by Customer Risk Level")
ax.set_xlabel("Risk Level")
ax.set_ylabel("Total Sales (₹)")
ax.tick_params(axis="x", rotation=0)

fig.tight_layout()
fig.savefig(
    OUTPUT_DIR / "day54_sales_by_risk.png",
    dpi=200,
    bbox_inches="tight",
)
plt.close(fig)

# --------------------------------------------------
# 4. Customer recency by risk
# --------------------------------------------------

fig, ax = plt.subplots(figsize=(8, 5))

risk_order = ["Low Risk", "Medium Risk", "High Risk"]
available_risks = [r for r in risk_order if r in df["Risk_Level"].unique()]

boxplot_data = [
    df.loc[df["Risk_Level"] == risk, "Recency_Days"].dropna()
    for risk in available_risks
]

ax.boxplot(boxplot_data, tick_labels=available_risks)

ax.set_title("Days Since Last Order by Risk Level")
ax.set_xlabel("Risk Level")
ax.set_ylabel("Days Since Last Order")

fig.tight_layout()
fig.savefig(
    OUTPUT_DIR / "day54_recency_by_risk.png",
    dpi=200,
    bbox_inches="tight",
)
plt.close(fig)

# --------------------------------------------------
# 5. Retention strategy distribution
# --------------------------------------------------

strategy_counts = df["Retention_Strategy"].value_counts()

fig, ax = plt.subplots(figsize=(10, 5))
strategy_counts.sort_values().plot(kind="barh", ax=ax)

ax.set_title("Customers by Retention Strategy")
ax.set_xlabel("Number of Customers")
ax.set_ylabel("Retention Strategy")

fig.tight_layout()
fig.savefig(
    OUTPUT_DIR / "day54_retention_strategies.png",
    dpi=200,
    bbox_inches="tight",
)
plt.close(fig)

print(f"\nCharts and summary saved to: {OUTPUT_DIR}")
