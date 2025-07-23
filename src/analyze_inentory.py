import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load cleaned inventory data
df = pd.read_csv("data/clean_inventory.csv")

# Create output folder
os.makedirs("output", exist_ok=True)

# --- Summary Statistics ---
summary = df.describe(include='all')
summary.to_csv("output/summary_statistics.csv")
print("Summary statistics saved to output/summary_statistics.csv")

# --- Missing Value Heatmap ---
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Values Heatmap")
plt.tight_layout()
plt.savefig("output/missing_values_heatmap.png")
plt.close()

# --- Count Plot for Categorical Columns ---
categorical_cols = df.select_dtypes(include='object').columns

for col in categorical_cols:
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x=col, order=df[col].value_counts().index)
    plt.xticks(rotation=45)
    plt.title(f"Count Plot for {col}")
    plt.tight_layout()
    plt.savefig(f"output/{col}_countplot.png")
    plt.close()

# --- Histogram for Numerical Columns ---
numerical_cols = df.select_dtypes(include='number').columns

for col in numerical_cols:
    plt.figure(figsize=(8, 5))
    sns.histplot(df[col], kde=True, bins=30)
    plt.title(f"Distribution of {col}")
    plt.tight_layout()
    plt.savefig(f"output/{col}_histogram.png")
    plt.close()

print("Charts saved to 'output/' folder.")
