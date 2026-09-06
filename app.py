import streamlit as st
import sys
import pandas as pd

# Allow Python to find files inside src/
sys.path.append("src")

from predictor import predict_placement


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="AI Career Intelligence System",
    page_icon="🎯",
    layout="wide"
)


# ==================================================
# LOAD ORIGINAL PLACEMENT DATA
# ==================================================

placement_df = pd.read_csv(
    "data/raw/campus_placement_data.csv"
)


# ==================================================
# TITLE
# ==================================================

st.title("🎯 AI-Powered Career Intelligence")
st.subheader("Placement Recommendation System")

st.write(
    "Enter your academic, skill, and experience information "
    "to estimate your placement probability and readiness."
)

st.info(
    "Please enter your actual information wherever possible. "
    "SSC refers to Class 10 and HSC refers to Class 12."
)


# ==================================================
# PERSONAL INFORMATION
# ==================================================

st.header("👤 Personal Information")

col1, col2, col3 = st.columns(3)


with col1:

    gender = st.selectbox(
        "Gender",
        sorted(
            placement_df["gender"]
            .dropna()
            .unique()
            .tolist()
        )
    )


with col2:

    age = st.number_input(
    "Age",
    min_value=18,
    max_value=26,
    value=22
)


with col3:

    city_tier = st.selectbox(
        "City Tier",
        sorted(
            placement_df["city_tier"]
            .dropna()
            .unique()
            .tolist()
        ),
        help="Select the tier of your current city."
    )


# ==================================================
# ACADEMIC INFORMATION
# ==================================================

st.header("🎓 Academic Information")


# --------------------------------------------------
# CLASS 10 / SSC
# --------------------------------------------------

st.subheader("📘 Class 10 (SSC)")

st.caption(
    "SSC = Secondary School Certificate. "
    "Enter the percentage from your Class 10 marksheet."
)

col1, col2 = st.columns(2)


with col1:

    ssc_percentage = st.number_input(
        "Class 10 Percentage",
        min_value=0.0,
        max_value=100.0,
        value=80.0,
        help="Enter your Class 10 overall percentage."
    )


with col2:

    ssc_board = st.selectbox(
        "Class 10 Board",
        sorted(
            placement_df["ssc_board"]
            .dropna()
            .unique()
            .tolist()
        )
    )


# --------------------------------------------------
# CLASS 12 / HSC
# --------------------------------------------------

st.subheader("📗 Class 12 (HSC)")

st.caption(
    "HSC = Higher Secondary Certificate. "
    "Enter the percentage from your Class 12 marksheet."
)

col1, col2 = st.columns(2)


with col1:

    hsc_percentage = st.number_input(
        "Class 12 Percentage",
        min_value=0.0,
        max_value=100.0,
        value=78.0,
        help="Enter your Class 12 overall percentage."
    )


with col2:

    hsc_board = st.selectbox(
        "Class 12 Board",
        sorted(
            placement_df["hsc_board"]
            .dropna()
            .unique()
            .tolist()
        )
    )


hsc_stream = st.selectbox(
    "Class 12 Stream",
    sorted(
        placement_df["hsc_stream"]
        .dropna()
        .unique()
        .tolist()
    )
)


# --------------------------------------------------
# GRADUATION
# --------------------------------------------------

st.subheader("🎓 Graduation")

col1, col2 = st.columns(2)


with col1:

    degree_percentage = st.number_input(
        "Graduation Percentage",
        min_value=0.0,
        max_value=100.0,
        value=82.0,
        help="Enter your overall graduation percentage."
    )


with col2:

    degree_field = st.selectbox(
        "Degree Field",
        sorted(
            placement_df["degree_field"]
            .dropna()
            .unique()
            .tolist()
        )
    )


# --------------------------------------------------
# MBA
# --------------------------------------------------

st.subheader("📚 MBA Information")

has_mba = st.radio(
    "Are you pursuing or have you completed an MBA?",
    ["No", "Yes"],
    horizontal=True
)


mba_percentage = None
specialization = None


if has_mba == "Yes":

    st.caption(
        "Enter your MBA percentage and specialization."
    )

    col1, col2 = st.columns(2)

    with col1:

        mba_percentage = st.number_input(
            "MBA Percentage",
            min_value=0.0,
            max_value=100.0,
            value=70.0
        )

    with col2:

        specialization = st.selectbox(
            "MBA Specialization",
            sorted(
                placement_df["specialization"]
                .dropna()
                .unique()
                .tolist()
            )
        )

else:

    st.caption(
        "MBA information is not required."
    )


# ==================================================
# SKILLS & PERFORMANCE
# ==================================================

st.header("📊 Skills & Performance")


st.caption(
    "Technical Skills, Soft Skills and Communication are rated "
    "from 1–10. Aptitude is rated from 0–100."
)

col1, col2 = st.columns(2)


with col1:

  technical_skills_score = st.number_input(
    "Technical Skills Score",
    min_value=1.0,
    max_value=10.0,
    value=6.0,
    step=0.5,
    help="Rate your technical skills from 1 to 10."
)
soft_skills_score = st.number_input(
    "Soft Skills Score",
    min_value=1.0,
    max_value=10.0,
    value=6.5,
    step=0.5,
    help="Rate your soft skills from 1 to 10."
)


with col2:

 aptitude_score = st.number_input(
    "Aptitude Score",
    min_value=0,
    max_value=100,
    value=60,
    help="Enter your aptitude score from 0 to 100."
)

communication_score = st.number_input(
    "Communication Score",
    min_value=1.0,
    max_value=10.0,
    value=6.5,
    step=0.5,
    help="Rate your communication skills from 1 to 10."
)


# ==================================================
# EXPERIENCE & ACTIVITIES
# ==================================================

st.header("💼 Experience & Activities")

col1, col2, col3, col4 = st.columns(4)


with col1:

    internships_count = st.number_input(
    "Internships",
    min_value=0,
    max_value=5,
    value=1
)


with col2:

    projects_count = st.number_input(
        "Projects",
        min_value=0,
        max_value=10,
        value=3
    )


with col3:

    certifications_count = st.number_input(
        "Certifications",
        min_value=0,
        max_value=8,
        value=2
    )


with col4:

    work_experience_months = st.number_input(
        "Work Experience (Months)",
        min_value=0,
        max_value=36,
        value=6
    )


col1, col2, col3 = st.columns(3)


with col1:

    leadership_roles = st.number_input(
        "Leadership Roles",
        min_value=0,
        max_value=5,
        value=1
    )


with col2:

    extracurricular_activities = st.number_input(
        "Extracurricular Activities",
        min_value=0,
        max_value=10,
        value=2
    )


with col3:

    backlogs = st.number_input(
        "Backlogs",
        min_value=0,
        max_value=10,
        value=0
    )


st.divider()

predict_button = st.button(
    "🔮 Predict Placement",
    type="primary",
    use_container_width=True
)

if predict_button:

    student_data = {

        "gender": gender,
        "age": age,
        "city_tier": city_tier,

        "ssc_percentage": ssc_percentage,
        "ssc_board": ssc_board,

        "hsc_percentage": hsc_percentage,
        "hsc_board": hsc_board,
        "hsc_stream": hsc_stream,

        "degree_percentage": degree_percentage,
        "degree_field": degree_field,

        "mba_percentage": mba_percentage,
        "specialization": specialization,

        "internships_count": internships_count,
        "projects_count": projects_count,
        "certifications_count": certifications_count,

        "technical_skills_score": technical_skills_score,
        "soft_skills_score": soft_skills_score,
        "aptitude_score": aptitude_score,
        "communication_score": communication_score,

        "work_experience_months": work_experience_months,
        "leadership_roles": leadership_roles,
        "extracurricular_activities": extracurricular_activities,
        "backlogs": backlogs
    }

    try:

        result = predict_placement(student_data)

        st.header("📈 Placement Prediction")

        col1, col2, col3 = st.columns(3)


        with col1:

            if result["prediction"] == 1:
                st.success("✅ PLACED")
            else:
                st.error("❌ NOT PLACED")


        with col2:

            st.metric(
                "Placement Probability",
                f"{result['placement_probability']}%"
            )


        with col3:

            st.metric(
                "Readiness Level",
                result["readiness"]
            )


        st.progress(
            result["placement_probability"] / 100
        )

        st.caption(
            "This probability is an estimate generated by the "
            "trained machine-learning model and is not a guarantee."
        )


    except Exception as e:

        st.error(
            "An error occurred while making the prediction."
        )

        st.exception(e)

        # ==================================================
# CAREER RECOMMENDATION
# ==================================================

st.divider()

st.header("💼 Career Recommendation")

st.write(
    "Enter your current technical and professional skills "
    "to find the career roles that best match your profile."
)

st.caption(
    "Enter skills separated by commas. "
    "Example: Python, SQL, Pandas, Machine Learning"
)


# --------------------------------------------------
# IMPORT CAREER RECOMMENDER
# --------------------------------------------------

from career_recommender import recommend_careers


student_skills_input = st.text_area(
    "Your Skills",
    placeholder=(
        "Example: Python, SQL, Pandas, "
        "Machine Learning, Excel"
    ),
    height=100
)


recommend_button = st.button(
    "🎯 Recommend Careers",
    type="primary",
    use_container_width=True
)


# --------------------------------------------------
# CAREER RECOMMENDATION
# --------------------------------------------------

if recommend_button:

    if not student_skills_input.strip():

        st.warning(
            "Please enter at least one skill."
        )

    else:

        # Convert comma-separated skills into a list
        student_skills = [
            skill.strip()
            for skill in student_skills_input.split(",")
            if skill.strip()
        ]

        try:

            recommendations = recommend_careers(
                student_skills,
                top_n=3
            )

            st.subheader("🏆 Top Career Recommendations")


            # Display top 3 careers
            for i, recommendation in enumerate(
                recommendations,
                start=1
            ):

                role = recommendation["role"]
                percentage = recommendation["match_percentage"]

                st.markdown(
                    f"### {i}. {role}"
                )

                st.progress(
                    percentage / 100
                )

                st.write(
                    f"**Skill Match: {percentage}%**"
                )

                st.write(
                    "**Matching Skills:** "
                    + (
                        ", ".join(
                            recommendation["matching_skills"]
                        )
                        if recommendation["matching_skills"]
                        else "None"
                    )
                )

                st.write(
                    "**Missing Skills:** "
                    + (
                        ", ".join(
                            recommendation["missing_skills"]
                        )
                        if recommendation["missing_skills"]
                        else "None"
                    )
                )

                st.divider()


        except Exception as e:

            st.error(
                "An error occurred while generating career recommendations."
            )

            st.exception(e)

# ==================================================
# SKILL GAP ANALYSIS
# ==================================================

st.divider()

st.header("📚 Skill Gap Analysis")

st.write(
    "Select a career role to see which skills you already "
    "have and which skills you need to develop."
)


from skill_analyzer import (
    get_available_roles,
    analyze_skill_gap
)


available_roles = get_available_roles()


selected_role = st.selectbox(
    "Select Target Career",
    available_roles
)


analyze_button = st.button(
    "🔍 Analyze Skill Gap",
    use_container_width=True
)


if analyze_button:

    if not student_skills_input.strip():

        st.warning(
            "Please enter your skills above first."
        )

    else:

        student_skills = [
            skill.strip()
            for skill in student_skills_input.split(",")
            if skill.strip()
        ]

        try:

            result = analyze_skill_gap(
                student_skills,
                selected_role
            )


            st.subheader(
                f"📊 Skill Analysis — {selected_role}"
            )


            # Match percentage
            st.metric(
                "Skill Match",
                f"{result['match_percentage']}%"
            )


            col1, col2 = st.columns(2)


            # Matching skills
            with col1:

                st.markdown(
                    "### ✅ Matching Skills"
                )

                if result["matching_skills"]:

                    for skill in result["matching_skills"]:

                        st.write(
                            f"✓ {skill.title()}"
                        )

                else:

                    st.write(
                        "No matching skills found."
                    )


            # Missing skills
            with col2:

                st.markdown(
                    "### ❌ Missing Skills"
                )

                if result["missing_skills"]:

                    for skill in result["missing_skills"]:

                        st.write(
                            f"○ {skill.title()}"
                        )

                else:

                    st.write(
                        "You have all required skills!"
                    )


        except Exception as e:

            st.error(
                "An error occurred during skill gap analysis."
            )

            st.exception(e)