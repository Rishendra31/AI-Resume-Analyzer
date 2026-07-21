import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from utils.resume_parser import extract_skills


def calculate_similarity(resume_text, job_description):
    """
    Calculates similarity percentage between
    resume and job description using TF-IDF + Cosine Similarity.
    """

    documents = [resume_text, job_description]

    vectorizer = TfidfVectorizer(stop_words="english")

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )[0][0]

    return similarity * 100


def find_missing_skills(resume_skills, job_description):
    """
    Finds skills that are present in the
    job description but missing from the resume.
    """

    jd_text = job_description.lower()

    jd_skills = set()

    for skill in extract_skills(job_description):
        jd_skills.add(skill)

    resume_skills = set(resume_skills)

    missing_skills = sorted(jd_skills - resume_skills)

    return missing_skills