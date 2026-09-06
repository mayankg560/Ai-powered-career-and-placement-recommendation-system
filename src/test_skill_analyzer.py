from skill_analyzer import (
    get_available_roles,
    get_required_skills,
    analyze_skill_gap
)

roles = get_available_roles()

print("\nTOTAL ROLES:", len(roles))

print("\nDATA SCIENTIST EXISTS:")

for role in roles:
    if "data scientist" in role.lower():
        print(repr(role))

print("\nREQUIRED SKILLS:")

skills = get_required_skills("Data Scientist")

print(skills)

print("\nNUMBER OF REQUIRED SKILLS:", len(skills))


student_skills = ["Python", "SQL", "Pandas"]

result = analyze_skill_gap(
    student_skills,
    "Data Scientist"
)

print("\n" + "=" * 50)
print("ROLE:", result["role"])
print("MATCHING:", result["matching_skills"])
print("MISSING:", result["missing_skills"])
print("MATCH %:", result["match_percentage"])
print("=" * 50)