import streamlit as st
import re

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("🤖 AI-Powered Resume Analyzer")
st.write("Analyze your resume against a job description and discover your skill match.")

# Skill database
skills = [
    "python", "java", "sql", "mysql", "pandas", "numpy",
    "machine learning", "data analysis", "data visualization",
    "excel", "power bi", "tableau", "aws", "cloud computing",
    "html", "css", "javascript", "streamlit", "git", "github"
]

# User inputs
col1, col2 = st.columns(2)

with col1:
    resume_text = st.text_area(
        "📄 Paste your Resume",
        height=350,
        placeholder="Paste your resume content here..."
    )

with col2:
    job_description = st.text_area(
        "💼 Paste the Job Description",
        height=350,
        placeholder="Paste the job description here..."
    )

if st.button("🔍 Analyze Resume", use_container_width=True):

    if not resume_text or not job_description:
        st.warning("Please enter both your resume and the job description.")

    else:
        resume_lower = resume_text.lower()
        job_lower = job_description.lower()

        # Find skills in resume and job description
        resume_skills = [
            skill for skill in skills
            if re.search(r"\b" + re.escape(skill) + r"\b", resume_lower)
        ]

        job_skills = [
            skill for skill in skills
            if re.search(r"\b" + re.escape(skill) + r"\b", job_lower)
        ]

        matched_skills = list(set(resume_skills) & set(job_skills))
        missing_skills = list(set(job_skills) - set(resume_skills))

        # Calculate match score
        if job_skills:
            match_score = round(
                (len(matched_skills) / len(job_skills)) * 100
            )
        else:
            match_score = 0

        st.divider()
        st.subheader("📊 Analysis Results")

        metric1, metric2, metric3 = st.columns(3)

        metric1.metric("Match Score", f"{match_score}%")
        metric2.metric("Matched Skills", len(matched_skills))
        metric3.metric("Missing Skills", len(missing_skills))

        st.progress(match_score)

        col3, col4 = st.columns(2)

        with col3:
            st.subheader("✅ Matched Skills")

            if matched_skills:
                for skill in sorted(matched_skills):
                    st.success(skill.title())
            else:
                st.info("No matching skills found.")

        with col4:
            st.subheader("⚠️ Skills to Improve")

            if missing_skills:
                for skill in sorted(missing_skills):
                    st.warning(skill.title())
            else:
                st.success("Great! No important skills are missing.")

        # Suggestions
        st.subheader("💡 Suggestions")

        if match_score >= 80:
            st.success(
                "Excellent match! Your resume aligns well with this job."
            )
        elif match_score >= 50:
            st.info(
                "Good match. Consider adding more relevant skills and projects."
            )
        else:
            st.error(
                "Low match. Review the job description and highlight relevant skills."
            )
