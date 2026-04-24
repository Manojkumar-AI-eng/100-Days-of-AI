"""
Pandas Fundamentals: Data Loading and Structure Manipulation
Author: Manojkumar M
Date: April 2026
"""

import pandas as pd

def main():
    # --- 1. DATA LOADING ---
    # In a real scenario, ensure 'example_dataset.csv' exists in your directory
    try:
        df_csv = pd.read_csv("example_dataset.csv")
        print("📂 CSV DATA PREVIEW:")
        print(df_csv.head()) # .head() shows only the first 5 rows for a cleaner look
        print("-" * 40)
    except FileNotFoundError:
        print("⚠️ Note: 'example_dataset.csv' not found. Skipping file read.\n")

    # --- 2. PANDAS SERIES ---
    # A Series is essentially a single column of data with an index
    age_list = [10, 20, 30, 40, 50]
    age_series = pd.Series(age_list, name="Ages")
    
    print("🔢 PANDAS SERIES:")
    print(age_series)
    print("-" * 40)

    # --- 3. PANDAS DATAFRAME ---
    # A DataFrame is a 2D table-like structure (similar to an Excel sheet)
    student_data = {
        "Name": ["Manoj", "Rajasthan", "Maritha", "Baiju", "Rome"],
        "Age": [20, 10, 30, 40, 50],
        "Marks": [90, 80, 75, 80, 90]
    }

    # Creating DataFrame with custom String-based indexing
    indices = [f"Std:{i}" for i in range(1, 6)]
    df = pd.DataFrame(student_data, index=indices)

    print("📊 STUDENT DATAFRAME (Custom Index):")
    print(df)
    print("-" * 40)

    # --- 4. DATA SLICING & SELECTION ---
    
    # .iloc uses Integer-based Location (positional index)
    print("📍 Selection using .iloc[3] (4th Row):")
    print(df.iloc[3])
    print("-" * 40)

    # .loc uses Label-based Location (index name)
    print("🏷️ Selection using .loc['Std:1':'Std:3']:")
    print(df.loc["Std:1":"Std:3"])
    print("-" * 40)

    # --- 5. QUICK ANALYTICS (Bonus) ---
    print("📈 QUICK STATISTICS:")
    print(df.describe())

if __name__ == "__main__":
    main()