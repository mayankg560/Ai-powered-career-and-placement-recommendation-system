import pandas as pd

df = pd.read_csv(
    "data/processed/role_skills.csv"
)

print("\nFIRST 20 ROWS")
print(df.head(20))

print("\nSHAPE")
print(df.shape)

print("\nUNIQUE ROLES")
print(df["Role"].nunique())

print("\nUNIQUE SKILLS")
print(df["Skill"].nunique())

print("\nROLES")
print(
    df["Role"].unique()
)