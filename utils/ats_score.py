import re
from utils.resume_parser import extract_skills


def calculate_ats_score(resume_text):
    """
    Calculates a simple ATS score out of 100.
    """

    score = 0

    
    words = len(resume_text.split())

    if words >= 300:
        score += 20
    elif words >= 200:
        score += 15
    elif words >= 100:
        score += 10

    
    skills = extract_skills(resume_text)

    if len(skills) >= 15:
        score += 30
    elif len(skills) >= 10:
        score += 25
    elif len(skills) >= 5:
        score += 15
    elif len(skills) >= 1:
        score += 10

    
    text = resume_text.lower()

    
    education_keywords = [
        "b.tech",
        "btech",
        "b.e",
        "bachelor",
        "master",
        "m.tech",
        "mtech",
        "degree",
        "university"
    ]

    education_found = False

    for keyword in education_keywords:
        if keyword in text:
            education_found = True
            break

    if education_found:
        score += 15

    
    experience_keywords = [
        "experience",
        "internship",
        "project",
        "projects"
    ]

    experience_found = False

    for keyword in experience_keywords:
        if keyword in text:
            experience_found = True
            break

    if experience_found:
        score += 15

    
    if "@" in resume_text:
        score += 10

    
    cleaned_text = resume_text.replace("-", "").replace(" ", "").replace("(", "").replace(")", "")
    if re.search(r"\d{10}", cleaned_text):
        score += 10

    
    if score > 100:
        score = 100

    return score