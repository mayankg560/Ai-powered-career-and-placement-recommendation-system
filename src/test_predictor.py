from predictor import predict_placement


student_data = {
    "gender": "Male",
    "age": 22,
    "city_tier": 1,

    "ssc_percentage": 80,
    "ssc_board": "Central",

    "hsc_percentage": 78,
    "hsc_board": "Central",
    "hsc_stream": "Science",

    "degree_percentage": 82,
    "degree_field": "Engineering",

    "mba_percentage": 70,
    "specialization": "Marketing",

    "internships_count": 2,
    "projects_count": 3,
    "certifications_count": 2,

    "technical_skills_score": 80,
    "soft_skills_score": 75,
    "aptitude_score": 82,
    "communication_score": 78,

    "work_experience_months": 6,
    "leadership_roles": 1,
    "extracurricular_activities": 2,
    "backlogs": 0
}


result = predict_placement(student_data)


print("\n" + "=" * 60)
print("PLACEMENT PREDICTION")
print("=" * 60)

print(
    "Prediction:",
    "PLACED" if result["prediction"] == 1
    else "NOT PLACED"
)

print(
    "Placement Probability:",
    result["placement_probability"],
    "%"
)

print(
    "Readiness:",
    result["readiness"]
)

print("=" * 60)