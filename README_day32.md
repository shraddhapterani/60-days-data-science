# Day 32 – Personalized Recommendation System

## Objective

Build a similarity-based recommendation engine to personalize product suggestions.

## Dataset

* 6 customers
* 6 products
* 16 customer-product ratings

## Tasks Completed

1. Created a customer-product matrix.
2. Calculated customer similarity using cosine similarity.
3. Built a customer-based recommendation engine.
4. Generated personalized product recommendations.
5. Evaluated relevance using a hidden-rating test.

## Evaluation

* Metric: Hit Rate
* Test cases: 1
* Hit Rate: 100% (1 out of 1)

This is a preliminary result based on one test case and does not represent general recommendation accuracy.

## Files

* day32_recommendation_system.ipynb
* day32_recommendation_outputs.csv
* day32_similarity_analysis.csv
* day32_recommendation_evaluation.csv

## Limitations

The dataset is small and synthetic. The evaluation uses only one hidden-rating test case. Larger real-world datasets and multiple test cases are needed for reliable evaluation.

## Tools

Python, Pandas, NumPy, Matplotlib, Scikit-learn, Cosine Similarity
