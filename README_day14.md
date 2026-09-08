# Day 14 - Sprint Review & Real-World Thinking

## ABTalks 60-Day Data Science Challenge

### Objective

Test how a machine learning model adapts when an important feature is removed.

### What I Did

- Used Linear Regression as the best-performing model from Day 13.
- Removed the `Sub-Category` feature.
- Retrained the model.
- Compared performance before and after feature removal.
- Analyzed the impact of the missing feature.
- Documented the Sprint 2 reflection.

### Performance Comparison

| Model | Test MAE | Test R² |
|---|---:|---:|
| Original Linear Regression | 238.77 | 0.179 |
| Without Sub-Category | 274.62 | 0.041 |

### Observations

After removing `Sub-Category`:

- Test MAE increased by 35.85.
- Test R² decreased by 0.1374.

The model was still able to make predictions, but its performance became weaker.

### Sprint 2 Reflection

This experiment showed that machine learning systems can depend heavily on important features. When an important feature disappears, the model may continue working but with reduced accuracy.

This helped me understand feature dependency, adaptability, and the importance of designing ML systems that can handle changing real-world constraints.

### Key Learning

Real-world ML systems must adapt when data and requirements change. A strong engineering system should not depend blindly on a single important feature.