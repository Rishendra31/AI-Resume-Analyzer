import streamlit as st
from utils.pdf_reader import read_pdf
from utils.resume_parser import extract_skills
from utils.ats_score import calculate_ats_score
from utils.similarity import calculate_similarity, find_missing_skills
from utils.llm import get_ai_feedback

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and compare it with a Job Description.")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=250
)

if uploaded_file:

    if st.button("Analyze Resume"):

        resume_text = read_pdf(uploaded_file)

        st.subheader("Resume Text")
        st.text_area(
            "",
            resume_text,
            height=250
        )

        skills = extract_skills(resume_text)

        ats_score = calculate_ats_score(resume_text)

        st.subheader("ATS Score")
        st.metric("Score", f"{ats_score}/100")

        st.subheader("Skills Found")

        if skills:
            st.write(", ".join(skills))
        else:
            st.warning("No skills detected.")

        if job_description.strip():

            similarity = calculate_similarity(
                resume_text,
                job_description
            )

            missing_skills = find_missing_skills(
                skills,
                job_description
            )

            st.subheader("Job Match")

            st.metric(
                "Match Percentage",
                f"{similarity:.2f}%"
            )

            st.subheader("Missing Skills")

            if missing_skills:
                for skill in missing_skills:
                    st.write(f"• {skill}")
            else:
                st.success("No important skills are missing.")

            st.subheader("AI Feedback")

            feedback = get_ai_feedback(
                resume_text,
                job_description,
                ats_score,
                similarity,
                missing_skills
            )

            st.write(feedback)