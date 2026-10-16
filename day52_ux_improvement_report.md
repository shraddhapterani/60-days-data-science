# Day 52/60 — Customer Intelligence Platform: UX Improvement Report

## 1. Objective

The objective of Day 52 was to improve the usability, visual quality, and interaction experience of the Customer Intelligence Platform. The goal was to make customer analytics easier for business users to understand and explore.

## 2. Technologies Used

- **Programming Language:** Python
- **Dashboard Framework:** Streamlit
- **Data Processing:** Pandas
- **Data Visualisation:** Plotly
- **Development Environment:** Visual Studio Code

## 3. UI/UX Improvements Implemented

### 3.1 Professional Dashboard Layout

- Added a clear dashboard title and descriptive subtitle.
- Improved spacing and section separation.
- Introduced consistent styling for metric cards.
- Used a wide layout to make better use of screen space.

### 3.2 Navigation

Added three navigation sections:

- **Overview:** Displays business metrics, customer risk distribution, and retention strategy analysis.
- **Customer Analysis:** Shows sales distribution and recency patterns across customer risk categories.
- **Customer Explorer:** Allows users to select a customer and inspect individual customer information.

### 3.3 Key Performance Indicators

The Overview page displays five key business metrics:

- Total Customers
- Total Sales
- Total Orders
- Average Order Value
- High Risk Customers

These metrics update according to the selected filters.

### 3.4 Improved Visualisations

- Added colour-coded customer risk categories.
- Improved chart titles, axis labels, and data labels.
- Used horizontal bars for retention strategy comparisons.
- Added interactive Plotly charts with hover information.
- Added box plots to compare sales and recency across risk categories.

### 3.5 Interactive Filters

Users can filter customer records using:

- Risk Level
- Retention Strategy
- Days Since Last Order

The dashboard displays the number of customer records matching the selected filters.

### 3.6 Customer Explorer

The Customer Explorer provides a customer selection workflow. Users can inspect:

- Total Sales
- Total Orders
- Days Since Last Order
- Estimated Customer Lifetime Value (CLV)
- Risk Level and Risk Score
- Suggested Retention Strategy
- Average Order Value

A complete customer record can also be expanded for additional details.

### 3.7 Data Upload and Export

- Added CSV upload functionality.
- Preserved the default customer dataset option.
- Added required-column validation.
- Added a download button to export filtered customer records as CSV.

## 4. UX Design Decisions

| Design Decision | Business Benefit |
|---|---|
| Separate navigation sections | Helps users find information quickly |
| KPI cards | Makes important business metrics easy to scan |
| Colour-coded risk categories | Improves visual comparison |
| Interactive charts | Allows users to explore data details |
| Customer-level explorer | Supports individual customer investigation |
| Filters | Helps users focus on relevant customer segments |
| CSV export | Supports further analysis and reporting |
| Input validation | Helps identify incompatible uploaded datasets |

## 5. Testing and Validation

The following dashboard sections were tested in the local Streamlit application:

- Overview page
- Customer Analysis page
- Customer Explorer page
- Customer selection and detail display
- Risk and retention filters
- Customer data display
- Filtered CSV download control

The three main navigation sections displayed their expected content during testing.

## 6. Business Value

The improved dashboard helps business users explore customer behaviour, compare risk categories, and identify customers who may require retention attention.

For example, a business analyst can filter customers by risk level, inspect their order recency, and review their assigned retention strategy. This can support more focused customer engagement planning.

The dashboard provides analytical insights, but business decisions should also consider data quality, context, and validation.

## 7. Limitations and Future Improvements

Potential future enhancements include:

- Add date-range filtering.
- Improve accessibility and mobile responsiveness.
- Add automated data-quality summaries.
- Provide clearer explanations for risk scores.
- Add more advanced customer segmentation.
- Introduce authentication and role-based access if deployed for multiple users.
- Test with larger and more varied datasets.

## 8. Conclusion

Day 52 focused on making the Customer Intelligence Platform more usable and business-friendly. The improved dashboard includes navigation, KPI cards, interactive charts, customer filters, individual customer details, and filtered CSV export.

This work demonstrates the importance of combining data analysis with thoughtful UI/UX design to make analytical results easier to explore and communicate.

## 9. Project Repository

GitHub: https://github.com/shraddhapterani/60-days-data-science

**Challenge:** ABTalks 60-Day Data Science Challenge — Day 52/60