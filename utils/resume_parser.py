import re

# Common technical skills
SKILLS = [
    "python",
    "java",
    "c",
    "c++",
    "javascript",
    "typescript",
    "html",
    "css",
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "sqlite",
    "react",
    "angular",
    "vue",
    "node.js",
    "nodejs",
    "express",
    "django",
    "flask",
    "fastapi",
    "streamlit",
    "git",
    "github",
    "docker",
    "kubernetes",
    "aws",
    "azure",
    "gcp",
    "linux",
    "tensorflow",
    "pytorch",
    "keras",
    "scikit-learn",
    "pandas",
    "numpy",
    "matplotlib",
    "opencv",
    "langchain",
    "huggingface",
    "faiss",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "generative ai",
    "rag",
    "llm",
    "nlp",
    "power bi",
    "excel"
]


def extract_skills(resume_text):
    """
    Extract skills from resume text.
    Returns a sorted list of detected skills.
    """

    text = resume_text.lower()

    found_skills = set()

    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):
            found_skills.add(skill.title())

    return sorted(found_skills)