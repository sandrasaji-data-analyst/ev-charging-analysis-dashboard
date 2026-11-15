
# ==========================================
# EV CHARGING ANALYSIS
# DATA CLEANING AND PREPROCESSING
# ==========================================

# 1. Import Libraries

import pandas as pd
import numpy as np
from pathlib import Path

# ==========================================
# 2. Load Dataset
# ==========================================

file_path = Path(
    r"C:\Users\SANDRA SAJI\OneDrive\Desktop\EV_Charging_Pattern.xlsx"
)

df = pd.read_excel(file_path)

print("\nOriginal Dataset:")
print(df.head())

print("\nOriginal Dataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

# ==========================================
# 3. Create Dataset Copy
# ==========================================

df_clean = df.copy()

# ==========================================
# 4. Clean Column Names
# ==========================================

df_clean.columns = df_clean.columns.str.strip()

# Correct temperature column encoding, if present
df_clean = df_clean.rename(
    columns={"Temperature (Â°C)": "Temperature (°C)"}
)

# ==========================================
# 5. Remove Duplicate Records
# ==========================================

duplicate_count = df_clean.duplicated().sum()

print("\nDuplicate Records:", duplicate_count)

df_clean = df_clean.drop_duplicates()

# ==========================================
# 6. Remove Unnecessary Spaces
# ==========================================

for column in df_clean.select_dtypes(include="str").columns:
    df_clean[column] = df_clean[column].str.strip()

# ==========================================
# 7. Handle Blank Values
# ==========================================

df_clean = df_clean.replace(r"^\s*$", np.nan, regex=True)

# ==========================================
# 8. Convert Date Columns
# ==========================================

date_columns = [
    column for column in df_clean.columns
    if "date" in column.lower() or "time" in column.lower()
]

for column in date_columns:
    df_clean[column] = pd.to_datetime(
        df_clean[column],
        errors="coerce"
    )

# ==========================================
# 9. Handle Infinite Values
# ==========================================

numeric_columns = df_clean.select_dtypes(
    include=np.number
).columns

df_clean[numeric_columns] = df_clean[numeric_columns].replace(
    [np.inf, -np.inf],
    np.nan
)

# ==========================================
# 10. Check Missing Values
# ==========================================

print("\nMissing Values:")
print(df_clean.isnull().sum())

print("\nTotal Missing Values:")
print(df_clean.isnull().sum().sum())

# ==========================================
# 11. Dataset Information
# ==========================================

print("\nCleaned Dataset Information:")
df_clean.info()

print("\nCleaned Dataset Shape:")
print(df_clean.shape)

# ==========================================
# 12. Statistical Summary
# ==========================================

print("\nStatistical Summary:")
print(df_clean.describe(include="all"))

# ==========================================
# 13. Export Cleaned Dataset
# ==========================================

output_folder = file_path.parent

csv_path = output_folder / "EV_Charging_Cleaned.csv"
excel_path = output_folder / "EV_Charging_Cleaned.xlsx"

df_clean.to_csv(csv_path, index=False)
df_clean.to_excel(excel_path, index=False)

# ==========================================
# 14. Final Verification
# ==========================================

df_check = pd.read_csv(csv_path)

print("\n========== FINAL VERIFICATION ==========")

print("Original Rows:", len(df))
print("Cleaned Rows:", len(df_clean))
print("Duplicate Rows Removed:", duplicate_count)
print("Final Rows Saved:", len(df_check))
print("Total Columns:", len(df_clean.columns))

print("\nFinal Missing Values:")
print(df_clean.isnull().sum())

print("\nCleaned Files Saved Successfully!")

print("CSV File:", csv_path)
print("Excel File:", excel_path)

print("\nEV Charging Data Cleaning Completed!")
