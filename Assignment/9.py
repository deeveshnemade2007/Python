import numpy as np
import pandas as pd
from scipy import stats

# 1. Create a sample dataset
data = {
    'Study_Hours': [2, 3, 5, 7, 9, 6, 8, 10, 1],
    'Exam_Score': [55, 60, 72, 81, 93, 65, 88, 76, 50]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

# 2. Individual Statistics using Pandas and NumPy
x = df['Study_Hours']

mean_val = np.mean(x)
median_val = np.median(x)

# ddof=1 calculates sample variance/std dev (n-1)
variance_val = np.var(x, ddof=1)
std_dev_val = np.std(x, ddof=1)

print(f"\nMean: {mean_val}")
print(f"Median: {median_val}")
print(f"Sample Variance: {variance_val:.2f}")
print(f"Sample Std Dev: {std_dev_val:.2f}")

# 3. Correlation (Pearson and Spearman)

# Pearson correlation coefficient and p-value
pearson_corr, p_val = stats.pearsonr(
    df['Study_Hours'],
    df['Exam_Score']
)

print(f"\nPearson Correlation: {pearson_corr:.4f}")
print(f"P-value: {p_val:.4e}")

# Spearman correlation
spearman_corr, spearman_p = stats.spearmanr(
    df['Study_Hours'],
    df['Exam_Score']
)

print(f"Spearman Correlation: {spearman_corr:.4f}")
print(f"Spearman P-value: {spearman_p:.4e}")

# 4. Summary Matrix using Pandas
# Pandas calculates summary statistics for all numeric columns automatically

print("\n--- Pandas Summary Statistics ---")
print(df.describe())

print("\n--- Correlation Matrix ---")
print(df.corr())