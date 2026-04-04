import pdfplumber

def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

SKILLS_DB = {
    "django": ["python", "django", "rest api", "sql"],
    "data_scientist": ["python", "machine learning", "pandas", "numpy"],
    "frontend": ["html", "css", "javascript", "react"]
}

def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill_list in SKILLS_DB.values():
        for skill in skill_list:
            if skill in text:
                found_skills.append(skill)

    return list(set(found_skills))


def calculate_score(found_skills, job_role):
    required = SKILLS_DB.get(job_role, [])
    
    matched = len(set(found_skills) & set(required))
    total = len(required)

    if total == 0:
        return 0, []

    score = int((matched / total) * 100)
    missing = list(set(required) - set(found_skills))

    return score, missing