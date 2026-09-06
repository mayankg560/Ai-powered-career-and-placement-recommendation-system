from skill_analyzer import (
    get_available_roles,
    analyze_skill_gap
)


def recommend_careers(student_skills, top_n=3):

    roles = get_available_roles()

    recommendations = []

    for role in roles:

        result = analyze_skill_gap(
            student_skills,
            role
        )

        recommendations.append({
            "role": result["role"],
            "match_percentage": result["match_percentage"],
            "matching_skills": result["matching_skills"],
            "missing_skills": result["missing_skills"]
        })

    # Sort according to match percentage
    recommendations.sort(
        key=lambda x: x["match_percentage"],
        reverse=True
    )

    return recommendations[:top_n]