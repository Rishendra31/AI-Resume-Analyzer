from utils.resume_parser import extract_skills


def calculate_ats_score(resume_text):
    """
    Calculates a simple ATS score out of 100.
    """

    score = 0

    # Resume Length
    words = len(resume_text.split())

    if words >= 300:
        score += 20
    elif words >= 200:
        score += 15
    elif words >= 100:
        score += 10

    # Skills
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

    # Education
    education_keywords = [
        "b.tech",
        "btech",
        "b.e",
        "be",
        "bachelor",
        "master",
        "m.tech",
        "mtech",
        "degree",
        "university"
    ]

    if any(keyword in text for keyword in education_keywords):
        score += 15

    # Experience / Projects
    experience_keywords = [
        "experience",
        "internship",
        "project",
        "projects"
    ]

    if any(keyword in text for keyword in experience_keywords):
        score += 15

    # Contact Information
    if "@" in resume_text:
        score += 10

    # Phone Number (simple check)
    digits = sum(char.isdigit() for char in resume_text)

    if digits >= 10:
        score += 10

    return min(score, 100)