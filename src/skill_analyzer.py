import pandas as pd

# ==========================================
# FILE PATH
# ==========================================

ROLE_SKILLS_FILE = "data/processed/role_skills.csv"


# ==========================================
# LOAD ROLE-SKILLS DATA
# ==========================================

def load_role_skills():

    df = pd.read_csv(
        ROLE_SKILLS_FILE
    )

    return df


# ==========================================
# GET ALL AVAILABLE ROLES
# ==========================================

def get_available_roles():

    df = load_role_skills()

    roles = (
        df["Role"]
        .dropna()
        .unique()
        .tolist()
    )

    return sorted(roles)


# ==========================================
# GET REQUIRED SKILLS FOR A ROLE
# ==========================================

def get_required_skills(role):
    df = load_role_skills()

    # Clean role names
    df["Role"] = (
        df["Role"]
        .astype(str)
        .str.strip()
    )

    # Clean the selected role
    role = str(role).strip()

    role_data = df[
        df["Role"].str.casefold() == role.casefold()
    ]

    required_skills = set(
        role_data["Skill"]
        .dropna()
        .astype(str)
        .str.strip()
        .str.casefold()
    )

    return required_skills


# ==========================================
# ANALYZE STUDENT SKILLS
# ==========================================

def analyze_skill_gap(
    student_skills,
    target_role
):

    # Clean student skills
    student_skills = {
        skill.strip().lower()
        for skill in student_skills
        if skill.strip()
    }

    # Get required skills
    required_skills = get_required_skills(
        target_role
    )

    # Check if role exists
    if not required_skills:

        return {
            "role": target_role,
            "matching_skills": [],
            "missing_skills": [],
            "match_percentage": 0
        }

    # Matching skills
    matching_skills = (
        student_skills
        .intersection(required_skills)
    )

    # Missing skills
    missing_skills = (
        required_skills
        - student_skills
    )

    # Calculate percentage
    match_percentage = (
        len(matching_skills)
        / len(required_skills)
    ) * 100

    return {
        "role": target_role,

        "matching_skills":
            sorted(matching_skills),

        "missing_skills":
            sorted(missing_skills),

        "match_percentage":
            round(match_percentage, 2)
    }