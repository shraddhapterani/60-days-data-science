# Day 45/60 — Cloud Deployment

## Project: Customer Intelligence Dashboard

### Objective
Deploy the interactive customer analytics dashboard publicly using Streamlit Community Cloud.

### Live Application
[Open Customer Intelligence Dashboard](https://60-days-data-science-hvwa5swhmdsyjzcv5sujis.streamlit.app/)

### Technology Stack
- Python
- Pandas
- Plotly
- Streamlit
- GitHub
- Streamlit Community Cloud

### Deployment Architecture

1. Customer risk data is stored in a CSV file.
2. The dashboard code is maintained in a GitHub repository.
3. The `requirements.txt` file specifies the required Python libraries.
4. Streamlit Community Cloud retrieves the repository and installs the dependencies.
5. Streamlit runs `day44_dashboard.py` in the cloud.
6. Users access the deployed dashboard through a public web URL.

### Dashboard Features
- Customer and sales KPI cards
- Customer risk distribution chart
- Retention strategy visualization
- Customer data table
- Customer risk and retention strategy filters
- CSV upload functionality

### Key Metrics
- Total customers: 793
- Total sales: ₹2,261,536.78
- Total orders: 4,922
- Average order value: ₹459.57
- High-risk customers: 264

### Testing and Validation
- Confirmed the live dashboard loads successfully.
- Verified that the dashboard displays customer data and charts.
- Tested the dashboard filters successfully.

### Challenges and Learnings
- Prepared the dependency file for the cloud environment.
- Connected GitHub with Streamlit Community Cloud.
- Configured the repository, branch, and main Python file.
- Learned how a local Streamlit application can be deployed as a public web application.

### Outcome
Successfully deployed the Customer Intelligence Dashboard and made it accessible through a public URL.

### Key Learning
Cloud deployment makes an application accessible online without requiring every user to install and run the project locally.
