# Day 22 - Feature Encoding

## Objective
Convert categorical variables into numerical representations that machine learning models can understand.

## Dataset
E-commerce customer dataset with 100 records.

Categorical columns:
- Gender
- City
- Payment_Method

## Encoding Techniques

### Label Encoding
Categorical values were converted into numerical labels.

Dataset shape:
100 rows × 6 columns

### One-Hot Encoding
Each category was converted into a separate binary column.

Dataset shape:
100 rows × 11 columns

## Model Performance

| Encoding Method | Accuracy |
|---|---:|
| Label Encoding | 95% |
| One-Hot Encoding | 95% |

## Key Learning
Both encoding methods produced the same accuracy on this dataset. This shows that preprocessing and feature encoding can affect the structure of a dataset, while the impact on model performance depends on the data and the model being used.

## Files
- `day22_feature_encoding.ipynb`
- `day22_label_encoded_dataset.csv`
- `day22_onehot_encoded_dataset.csv`
- `day22_encoding_performance.csv`