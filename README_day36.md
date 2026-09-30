# Day 36/60 – Time Series Forecasting

## Project Overview

Day 36 focused on time series analytics and forecasting customer growth using historical business transaction data.

## Dataset

The project uses the Superstore historical sales dataset.

The `Order Date` and `Customer ID` columns were used to identify each customer's first purchase and construct a daily customer-growth time series.

## Analysis Performed

- Converted transaction dates into datetime format.
- Identified each customer's first purchase date.
- Calculated daily new-customer acquisition.
- Created cumulative customer growth.
- Converted the data into a continuous daily time series.
- Visualized historical customer growth.
- Analyzed monthly customer acquisition patterns.
- Evaluated baseline forecasting approaches.
- Generated a 30-day customer growth forecast.

## Key Results

- Historical customer count: 793
- Historical period: January 2015 to November 2018
- Forecast horizon: 30 days
- Recent 30-day average model MAE: 0.75
- Linear trend model MAE: 165.85
- Predicted customer count after 30 days: approximately 794
- Expected additional customers: approximately 1

## Model Comparison

| Model | MAE | Observation |
|---|---:|---|
| Linear Trend | 165.85 | Overestimated recent growth |
| Recent 30-Day Average | 0.75 | Better performance on the holdout period |

The recent 30-day average was selected as the baseline forecasting approach because it performed better on the held-out 30-day period.

## Business Insights

Customer growth was stronger during the earlier part of the historical period and slowed considerably toward the end.

Monthly customer acquisition also varied across months, with March showing the highest average and February showing the lowest average in the analysis.

The final forecast indicates very slow near-term customer growth based on recent acquisition activity.

## Forecasting Risks

- The model is a simple baseline and does not capture complex patterns.
- Marketing campaigns and promotions are not included.
- Holidays and external market conditions are not modeled.
- The historical growth rate changed significantly over time.
- The forecast should be treated as a planning estimate rather than a guaranteed outcome.

## Key Learning

Time series forecasting helps businesses use historical patterns to estimate future behavior.

I learned that selecting a forecasting model should depend not only on the historical trend but also on how well the model performs on unseen data.

## Output

`day36_customer_growth_forecast.csv`