import pandas as pd

df = pd.read_csv(
    "data/raw/campus_placement_data.csv"
)

categorical_columns = [
    "gender",
    "city_tier",
    "ssc_board",
    "hsc_board",
    "hsc_stream",
    "degree_field",
    "specialization"
]

for column in categorical_columns:

    print("\n" + "=" * 50)
    print(column)
    print("=" * 50)

    values = df[column].dropna().unique()

    for value in sorted(values, key=str):
        print(repr(value))