# Day 40 — A/B Testing and Experiment Analysis

## Overview

Day 40 of the ABTalks 60 Days Data Science Challenge focused on **A/B Testing and experimentation**.

The goal was to compare a **Control group** with an **Experiment group**, measure conversion performance, and determine whether the observed improvement was statistically significant.

## Objective

- Compare Control and Experiment groups
- Calculate conversion rates
- Measure absolute and relative improvement
- Perform statistical significance testing
- Make a business recommendation based on the results

## Dataset

The experiment contained two groups:

| Group | Users |
|---|---:|
| Control | 5,013 |
| Experiment | 4,987 |

Converted users:

| Group | Converted Users |
|---|---:|
| Control | 503 |
| Experiment | 592 |

## Conversion Rate

The conversion rates were calculated as:

**Conversion Rate = Converted Users / Total Users × 100**

Results:

| Group | Conversion Rate |
|---|---:|
| Control | 10.03% |
| Experiment | 11.87% |

The Experiment group achieved a higher conversion rate than the Control group.

## A/B Test Improvement

### Absolute Improvement

The experiment improved conversion by:

**1.84 percentage points**

### Relative Improvement

The Experiment group achieved:

**18.31% relative improvement**

compared with the Control group.

## Statistical Significance

A statistical significance test was performed to determine whether the difference between the two conversion rates was likely to be caused by random variation.

### Results

- **Z-statistic:** -2.9413
- **P-value:** 0.0033
- **Significance level:** 0.05

Since:

**0.0033 < 0.05**

the result is **statistically significant**.

Therefore, the observed difference between the Control and Experiment groups is unlikely to be due to random chance.

## Business Insight

The Experiment group performed better than the Control group.

The conversion rate increased from **10.03% to 11.87%**, representing an **18.31% relative improvement**.

Because the result is statistically significant, the experiment provides evidence that the experimental version can improve conversion performance.

## Business Recommendation

The business can consider adopting the experimental version because it produced a statistically significant improvement in conversion rate.

After rollout, the business should continue monitoring conversion and other important business metrics to ensure that the improvement remains consistent.

## Key Learnings

- A/B testing helps businesses compare two alternatives scientifically.
- Conversion rate is an important metric for evaluating experiments.
- Statistical significance helps determine whether an observed difference is meaningful.
- A low p-value provides evidence against the assumption that the groups perform the same.
- Data-driven experimentation reduces guesswork in business decisions.

## Conclusion

Day 40 improved my understanding of how businesses use **A/B testing, conversion analysis, and statistical significance** to make evidence-based decisions.

The experiment showed a **1.84 percentage-point increase** and an **18.31% relative improvement** in conversion, with a **p-value of 0.0033**, indicating a statistically significant result.

**Outcome:** The Experiment group performed significantly better than the Control group.