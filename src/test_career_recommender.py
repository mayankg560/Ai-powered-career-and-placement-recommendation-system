from career_recommender import recommend_careers


student_skills = [
    "Python",
    "SQL",
    "Pandas",
    "Machine Learning"
]


recommendations = recommend_careers(
    student_skills,
    top_n=3
)


print("\n" + "=" * 60)
print("TOP CAREER RECOMMENDATIONS")
print("=" * 60)


for i, recommendation in enumerate(recommendations, start=1):

    print(f"\n{i}. {recommendation['role']}")

    print(
        f"Match Percentage: "
        f"{recommendation['match_percentage']}%"
    )

    print(
        "Matching Skills:",
        recommendation["matching_skills"]
    )

    print(
        "Missing Skills:",
        recommendation["missing_skills"]
    )

print("\n" + "=" * 60)