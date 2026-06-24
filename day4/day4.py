import pandas as pd
import numpy as np

print("--- 1. Creating Core Pandas Data Structures ---")
# A Series is a 1D labeled array (like a single column)
sports_series = pd.Series(["Cricket", "Football", "Tennis"], name="Sports")
print("Pandas Series Example:")
print(sports_series)
print("-" * 40)

# A DataFrame is a 2D tabular data structure with rows and columns (like an Excel sheet)
raw_data = {
    "Name": ["Aryan", "Harsh", "Kunal", "Aryan"],
    "Age": [25, np.nan, 30, 25],
    "Salary_Amount": [5000, 5000, 7000, 5000]
}
df = pd.DataFrame(raw_data)
print("Initial Raw DataFrame:")
print(df)
print("-" * 40)


print("\n--- 2. Data Preprocessing: Handling Missing Values (.fillna) ---")
# Filling missing (NaN) values in the 'Age' column using the average age
df['Age'] = df['Age'].fillna(df['Age'].mean())
print("DataFrame after filling missing values in 'Age':")
print(df)
print("-" * 40)


print("\n--- 3. Data Cleaning: Removing Duplicates & Renaming Columns ---")
# Removing duplicate rows
df = df.drop_duplicates()

# Renaming columns for consistency (changing 'Salary_Amount' to 'Salary')
df = df.rename(columns={"Salary_Amount": "Salary"})

print("Cleaned DataFrame (No duplicates & renamed columns):")
print(df)
print("-" * 40)


print("\n--- 4. Data Transformation: Filtering and Sorting Data ---")
# Setting up sample product data for transformation showcase
product_data = {
    "Product": ["Laptop", "Hoodie", "Smartphone", "Jeans"],
    "Category": ["Electronics", "Clothing", "Electronics", "Clothing"],
    "Price": [800, 200, 500, 40]
}
product_df = pd.DataFrame(product_data)

# Filtering for 'Electronics' and sorting by 'Price' in ascending order
filtered_sorted_df = product_df.query("Category == 'Electronics'").sort_values(by="Price")

print("Transformed Data (Filtered by Electronics & Sorted by Price):")
print(filtered_sorted_df)
print("-" * 40)