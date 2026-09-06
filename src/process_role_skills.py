import pandas as pd
import os



INPUT_FILE = "data/raw/job_dataset.csv"
OUTPUT_FILE = "data/processed/role_skills.csv"



print("Loading role-skills dataset...")

df = pd.read_csv(INPUT_FILE)

print("Original shape:", df.shape)

print("\nOriginal columns:")
print(df.columns.tolist())
def normalize_role(role):
    role = str(role).strip()

    role_lower = role.lower()

    if "data scientist" in role_lower:
        return "Data Scientist"

    return role



df = df[
    [
        "Title",
        "Skills",
        "Keywords"
    ]
]



df = df.drop_duplicates()



df["Title"] = df["Title"].fillna("Unknown")



df["Skills"] = df[
    "Skills"
].fillna("")

df["Keywords"] = df[
    "Keywords"
].fillna("")



skill_data = []


for _, row in df.iterrows():

    role = normalize_role(row["Title"])

    skills = str(row["Skills"]).split(";")

    for skill in skills:

        skill = skill.strip()

        if skill:

            skill_data.append({

                "Role": role,

                "Skill": skill

})



role_skills_df = pd.DataFrame(
    skill_data
)




role_skills_df = role_skills_df.drop_duplicates(
    subset=["Role", "Skill"]
)



os.makedirs(
    "data/processed",
    exist_ok=True
)



role_skills_df.to_csv(
    OUTPUT_FILE,
    index=False
)



print("\nProcessed dataset shape:")
print(role_skills_df.shape)

print("\nFirst 20 rows:")
print(role_skills_df.head(20))

print("\nNumber of unique roles:")
print(
    role_skills_df["Role"].nunique()
)

print("\nNumber of unique skills:")
print(
    role_skills_df["Skill"].nunique()
)

print(
    f"\nProcessed dataset saved to: "
    f"{OUTPUT_FILE}"
)