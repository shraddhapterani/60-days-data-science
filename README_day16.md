# Day 16 - Movie Recommendation Using KNN

## Objective
Build a similarity-based movie recommendation system using the K-Nearest Neighbors algorithm.

## Dataset
MovieLens Small Dataset

- Ratings: 100836
- Movies: 9742
- Filtered ratings: 67898
- User-Movie Matrix: 610 users × 1297 movies

## Model
K-Nearest Neighbors (KNN)

## K Values Tested
- K = 3
- K = 5
- K = 10
- K = 15

## K Comparison

| K | Average Distance | Average Similarity |
|---|---:|---:|
| 3 | 0.478984 | 0.521016 |
| 5 | 0.495427 | 0.504573 |
| 10 | 0.519769 | 0.480231 |
| 15 | 0.534797 | 0.465203 |

## Best K
**K = 3**

K = 3 produced the highest average similarity of **0.521016** among the tested values.

## Example Recommendation

For **Toy Story (1995)** using K = 3:

- Jurassic Park (1993)
- Independence Day (a.k.a. ID4) (1996)
- Toy Story 2 (1999)

## Key Learning

KNN can generate recommendations by finding items with similar user-rating patterns. The choice of K affects recommendation quality, and smaller K performed better in this experiment.

## Files

- `day16_knn_movie_recommendation.ipynb`
- `day16_knn_k_comparison.csv`
- `day16_movie_recommendations.csv`
- `README_day16.md`