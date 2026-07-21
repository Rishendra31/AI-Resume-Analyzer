import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)


def get_ai_feedback(
    resume_text,
    job_description,
    ats_score,
    similarity,
    missing_skills
):
    prompt = f"""
You are an expert ATS Resume Reviewer.

Analyze the resume and provide professional feedback.

Resume:
{resume_text}

Job Description:
{job_description}

ATS Score:
{ats_score}/100

Job Match:
{similarity:.2f}%

Missing Skills:
{', '.join(missing_skills) if missing_skills else 'None'}

Provide the response in this format:

1. Overall Review
2. Strengths
3. Weaknesses
4. Missing Skills
5. Suggestions to Improve
6. Final Verdict
"""

    try:
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        return f"Error generating AI feedback: {e}"