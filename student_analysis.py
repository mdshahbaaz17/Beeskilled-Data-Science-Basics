import numpy as np
import pandas as pd

# 1. Load the Dataset
# Replace 'StudentsPerformance.csv' with the actual filename you downloaded from Kaggle
try:
    df = pd.read_csv("StudentsPerformance.csv")
    print("Dataset loaded successfully!\n")
except FileNotFoundError:
    print(
        "CSV file not found. Creating a sample DataFrame for demonstration..."
    )
    # Creating simulated data reflecting your Kaggle column structure
    data = {
        "gender": ["female", "male", "female", "male", "female", np.nan],
        "race/ethnicity": ["group B", "group C", "group B", "group A", np.nan, "group C"],
        "parental level of education": [
            "bachelor's degree",
            "some college",
            "master's degree",
            np.nan,
            "some high school",
            "associate's degree",
        ],
        "test preparation course": ["none", "completed", "none", "none", "completed", "none"],
        "math score": [72, 69, 90, 47, np.nan, 71],
        "reading score": [72, 90, 95, 57, 78, np.nan],
        "writing score": [74, 88, 93, 44, 75, 78],
    }
    df = pd.DataFrame(data)

print("--- Original Data Preview ---")
print(df.head())
print("\n" + "=" * 50 + "\n")

# ==========================================
# TASK 1: Clean Missing Data
# ==========================================

# Using Pandas to check for missing values
print("Missing values per column before cleaning:")
print(df.isnull().sum())
print("\n")

# Handling Missing Categorical Values: Fill with Mode (Most frequent value) or 'Unknown'
categorical_cols = [
    "gender",
    "race/ethnicity",
    "parental level of education",
    "test preparation course",
]
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# Handling Missing Numerical Values: Fill with the Mean score using NumPy/Pandas
numerical_cols = ["math score", "reading score", "writing score"]
for col in numerical_cols:
    df[col] = df[col].fillna(df[col].mean())

print("--- Cleaned Data Preview ---")
print(df.head())
print("\n" + "=" * 50 + "\n")

# ==========================================
# TASK 2 & 3: Calculate & Display Average, Max, Min Scores
# ==========================================

print("--- Statistical Summary of Scores ---")
# Using Pandas describe() or manual aggregations for precision
metrics = pd.DataFrame(
    {
        "Average (Mean)": df[numerical_cols].mean(),
        "Maximum": df[numerical_cols].max(),
        "Minimum": df[numerical_cols].min(),
    }
)

print(metrics.round(2))