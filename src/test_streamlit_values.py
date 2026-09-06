from predictor import predict_placement


# ==========================================
# PROFILE 1 - STRONG STUDENT
# ==========================================

strong_student = {

    "gender": "Male",
    "age": 22,
    "city_tier": "Tier 1",

    "ssc_percentage": 95,
    "ssc_board": "CBSE",

    "hsc_percentage": 94,
    "hsc_board": "CBSE",
    "hsc_stream": "Science",

    "degree_percentage": 92,
    "degree_field": "Engineering",

    "mba_percentage": None,
    "specialization": None,

    "internships_count": 3,
    "projects_count": 5,
    "certifications_count": 5,

    "technical_skills_score": 95,
    "soft_skills_score": 90,
    "aptitude_score": 95,
    "communication_score": 90,

    "work_experience_months": 12,
    "leadership_roles": 3,
    "extracurricular_activities": 5,
    "backlogs": 0
}


# ==========================================
# PROFILE 2 - WEAK STUDENT
# ==========================================

weak_student = {

    "gender": "Male",
    "age": 22,
    "city_tier": "Tier 3",

    "ssc_percentage": 45,
    "ssc_board": "State",

    "hsc_percentage": 48,
    "hsc_board": "State",
    "hsc_stream": "Arts",

    "degree_percentage": 50,
    "degree_field": "Other",

    "mba_percentage": None,
    "specialization": None,

    "internships_count": 0,
    "projects_count": 0,
    "certifications_count": 0,

    "technical_skills_score": 30,
    "soft_skills_score": 35,
    "aptitude_score": 30,
    "communication_score": 35,

    "work_experience_months": 0,
    "leadership_roles": 0,
    "extracurricular_activities": 0,
    "backlogs": 5
}


# ==========================================
# PREDICT BOTH
# ==========================================

strong_result = predict_placement(strong_student)
weak_result = predict_placement(weak_student)


# ==========================================
# DISPLAY RESULTS
# ==========================================

print("\n" + "=" * 60)
print("STRONG STUDENT")
print("=" * 60)

print("Prediction:",
      "PLACED" if strong_result["prediction"] == 1
      else "NOT PLACED")

print(
    "Probability:",
    strong_result["placement_probability"],
    "%"
)

print(
    "Readiness:",
    strong_result["readiness"]
)


print("\n" + "=" * 60)
print("WEAK STUDENT")
print("=" * 60)

print("Prediction:",
      "PLACED" if weak_result["prediction"] == 1
      else "NOT PLACED")

print(
    "Probability:",
    weak_result["placement_probability"],
    "%"
)

print(
    "Readiness:",
    weak_result["readiness"]
)

print("\n" + "=" * 60)