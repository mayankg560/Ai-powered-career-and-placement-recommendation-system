import pandas as pd


df = pd.read_csv(
    "data/raw/campus_placement_data.csv"
)


numerical_columns = [
    "age",
    "ssc_percentage",
    "hsc_percentage",
    "degree_percentage",
    "mba_percentage",
    "internships_count",
    "projects_count",
    "certifications_count",
    "technical_skills_score",
    "soft_skills_score",
    "aptitude_score",
    "communication_score",
    "work_experience_months",
    "leadership_roles",
    "extracurricular_activities",
    "backlogs"
]


print("\n" + "=" * 80)
print("DATASET VALUE RANGES")
print("=" * 80)


for column in numerical_columns:

    print(f"\n{column}")

    print(
        "Minimum:",
        df[column].min()
    )

    print(
        "Maximum:",
        df[column].max()
    )

    print(
        "Mean:",
        round(df[column].mean(), 2)
    )

    print(
        "Median:",
        round(df[column].median(), 2)
    )


print("\n" + "=" * 80)


# Placement distribution

print("\nPLACEMENT DISTRIBUTION")

print(
    df["placed"].value_counts()
)

print("\nPLACEMENT PERCENTAGES")

print(
    df["placed"]
    .value_counts(normalize=True)
    * 100
)