# Week 4 Reflection — ML Optimization

## What I Worked On

During Week 4, I explored different techniques for improving and evaluating machine learning models.

I worked with:

- Feature engineering
- Cross-validation
- Hyperparameter tuning
- Bias-variance analysis
- Complete ML pipelines

## Day 28 Sprint Review

For Day 28, I combined these ideas into a single optimized machine learning pipeline.

The pipeline included:

1. Feature engineering
2. Missing-value preprocessing
3. Random Forest classification
4. Cross-validation
5. Hyperparameter tuning using GridSearchCV

## Performance Comparison

| Model | CV Accuracy |
|---|---:|
| Random Forest (Day 25) | 98.00% |
| Tuned Random Forest (Day 26) | 98.00% |
| Optimized ML Pipeline (Day 28) | 96.25% |

The optimized pipeline achieved **100% accuracy on the held-out test set**.

## Engineering Tradeoff

The optimized pipeline did not achieve a higher cross-validation score than the earlier Random Forest models.

However, the main benefit was the engineering workflow. Feature engineering, preprocessing, model training, validation, and tuning were combined into one reproducible pipeline.

This makes the workflow easier to maintain and reuse compared with performing each step manually.

## Key Learnings

- High model performance is not only about increasing accuracy.
- Cross-validation gives a better view of model generalization.
- Pipelines make machine learning workflows more reproducible.
- Hyperparameter tuning should be based on measured results rather than assumptions.
- Production-oriented ML requires both model performance and good engineering practices.

## Week 4 Takeaway

Week 4 helped me understand that building a good ML system involves more than training a model. A reliable system combines preprocessing, feature engineering, validation, optimization, and reproducible workflows.