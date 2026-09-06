import pandas as pd
df=pd.read_csv('data/raw/campus_placement_data.csv')
print("="*60)
print("Campus Placement Data Analysis")
print('='*60)
print("\n first five rows of the dataset are:")
print(df.head())
print("\n Dataset Shape:")
print(f"Rows: {df.shape[0]}")
print(f'Columns: {df.shape[1]}')
print("\nCOLUMN NAMES:")
for column in df.columns:
    print("-", column)

# Data types
print("\nDATA TYPES:")
print(df.dtypes)

# Missing values
print("\nMISSING VALUES:")
print(df.isnull().sum())

# Duplicates
print("\nDUPLICATE ROWS:")
print(df.duplicated().sum())

# Statistics
print("\nNUMERICAL STATISTICS:")
print(df.describe())

# Target distribution
print("\nPLACEMENT DISTRIBUTION:")
print(df["placed"].value_counts())

print("\nPLACEMENT PERCENTAGE:")
print(df["placed"].value_counts(normalize=True) * 100)