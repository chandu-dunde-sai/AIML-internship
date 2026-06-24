import pandas as pd
import numpy as np

print("--- Day 5: Advanced Data Cleaning Techniques ---")
print("-" * 50)

# 1. Simulating a Raw Dataset with Common Data Anomalies
raw_data = {
    "Student_ID": [101, 102, 103, 101, 104, 105],
    "Name": ["  Ananya ", "Amit", "Rahul", "  Ananya ", "Suresh", "Priya"],
    "Age": ["21", "22", "twenty-three", "21", "22", "21"], # Incorrect data types / formatting
    "Score": [85.0, np.nan, 90.0, 85.0, 250.0, 88.0],     # Missing values & Outlier (250.0)
    "City": ["Mumbai", "mumbai", "Delhi", "Mumbai", "Bangalore", "delhi"] # Inconsistent capitalization
}

df = pd.DataFrame(raw_data)
print("Initial Noisy Dataset:")
print(df)
print("-" * 50)


# 2. Handling Duplicate Records
# Detecting and removing exact duplicate rows based on Student_ID
print("\n[Technique 1] Removing Duplicate Records...")
df = df.drop_duplicates(subset=["Student_ID"]).reset_index(drop=True)
print(df)
print("-" * 50)


# 3. Standardizing Formats & Text Manipulation
print("\n[Technique 2] Fixing Inconsistent Text & Capitalization...")
# Stripping whitespace from names
df["Name"] = df["Name"].str.strip()
# Standardizing city capitalization to Title Case
df["City"] = df["City"].str.title()
print(df)
print("-" * 50)


# 4. Fixing Incorrect Data Types & Structural Errors
print("\n[Technique 3] Fixing Incorrect Data Types...")
# Replacing the text string 'twenty-three' with a numeric string '23'
df["Age"] = df["Age"].replace("twenty-three", "23")
# Converting the Age column from object/string to integer
df["Age"] = df["Age"].astype(int)
print(f"Age column successfully converted. New data type: {df['Age'].dtype}")
print(df)
print("-" * 50)


# 5. Handling Missing Values (Imputation)
print("\n[Technique 4] Handling Missing Values...")
# Filling the missing score using the median value of valid scores
median_score = df["Score"].median()
df["Score"] = df["Score"].fillna(median_score)
print(df)
print("-" * 50)


# 6. Detecting & Treating Outliers
print("\n[Technique 5] Detecting and Handling Outliers...")
# A score of 250 is an invalid outlier (assuming maximum possible score is 100)
# We will cap any score above 100 down to the maximum valid score of 100
df.loc[df["Score"] > 100, "Score"] = 100.0
print("Final Cleaned Dataset:")
print(df)
print("-" * 50)