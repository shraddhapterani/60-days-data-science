# Day 33/60 – Anomaly Detection

## Project Objective
Identify unusual customer behavior using Isolation Forest.

## Dataset
- 200 synthetic customer records
- 4 behavioral features
- 8 deliberately injected anomalies

## Techniques Used
- Exploratory Data Analysis
- Isolation Forest
- Scatter plots and distribution visualization
- Business risk analysis

## Key Findings
- Detected 8 suspicious customer records.
- Suspicious records showed unusually high spending.
- High transaction frequency and repeated failed transactions
  were observed among flagged customers.
- Compared normal and suspicious customer behavior.

## Business Risks
- Potential financial fraud
- Unusual account activity
- Repeated transaction failures
- Possible account security risks

## Business Recommendation
Flag unusual activity for further investigation.
Do not automatically classify a customer as fraudulent based
only on an anomaly detection result.

## Tools
Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn

## Limitation
The dataset is synthetic and contains deliberately injected
anomalies. Results do not represent real-world fraud detection
accuracy.

## Files
- day33_anomaly_detection.ipynb
- day33_anomaly_detection_results.csv
- day33_business_risk_analysis.csv
- day33_behavior_comparison.csv
