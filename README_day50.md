# Day 50/60 — Capstone Model Optimization

## Objective

Optimize the customer-risk classification component of the Customer Intelligence Platform by comparing machine-learning algorithms, tuning hyperparameters, and evaluating generalization.

## Dataset

- **Source:** `day41_customer_risk_scores.csv`
- **Records:** 793 customers
- **Columns:** 12
- **Missing values:** None found in the initial inspection
- **Target:** `Risk_Level`
- **Features:** Total sales, total orders, average order value, customer lifetime, recency, purchase frequency, and estimated customer lifetime value.

The target distribution is balanced across Low Risk, Medium Risk, and High Risk.

## Methodology

1. Loaded and inspected the customer-risk dataset.
2. Selected seven numerical features and excluded Customer ID, raw date columns, and Risk Score.
3. Split the data into training and testing sets using an 80/20 stratified split.
4. Trained a baseline Random Forest classifier.
5. Compared Logistic Regression, Decision Tree, and Random Forest.
6. Tuned Logistic Regression using GridSearchCV with five-fold stratified cross-validation and macro F1-score.
7. Compared training and testing performance to investigate overfitting.

## Model Comparison

| Model | Training Accuracy | Test Accuracy | Test Macro F1 |
|---|---:|---:|---:|
| Logistic Regression | 95.43% | 94.97% | 0.9499 |
| Random Forest | 100.00% | 92.45% | 0.9245 |
| Decision Tree | 100.00% | 91.19% | 0.9110 |

Logistic Regression achieved the best test performance among the three initial models.

## Hyperparameter Tuning

The best Logistic Regression configuration found by GridSearchCV was:

- `C`: 100
- `class_weight`: None
- `solver`: `lbfgs`

The best cross-validation macro F1-score was **0.9810**.

### Baseline vs Tuned Logistic Regression

| Metric | Baseline | Tuned |
|---|---:|---:|
| Test Accuracy | 94.97% | 97.48% |
| Test Macro F1 | 0.9499 | 0.9747 |

Test accuracy improved by approximately **2.51 percentage points** after tuning.

## Generalization Analysis

- Tuned training accuracy: 99.37%
- Tuned test accuracy: 97.48%
- Train-test accuracy gap: approximately 1.88 percentage points

The small gap is encouraging for this particular split, but further validation is required before making production claims.

## Deliverables

- `day50_capstone_model_optimization.ipynb`
- `day50_model_comparison_report.csv`
- `day50_baseline_vs_tuned.csv`
- `day50_model_performance_comparison.png`

## Engineering Trade-offs

- Logistic Regression achieved stronger test performance with lower model complexity than the tree-based alternatives in this experiment.
- Grid search required additional computation to compare hyperparameter configurations.
- A single train/test split provides limited evidence about performance on future data.
- The target represents existing risk labels. High classification performance does not prove that the model predicts actual future churn.
- The risk-label generation logic should be reviewed to rule out target leakage or circular evaluation before deployment.

## Key Learning

Model optimization is not simply about increasing accuracy. It involves comparing algorithms, selecting suitable metrics, tuning hyperparameters, checking generalization, and understanding the limitations of the available labels.

**Day 50 outcome:** Compared three classification algorithms, tuned Logistic Regression, and documented the resulting performance improvement.