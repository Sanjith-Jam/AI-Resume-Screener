SKILL_SET = [
    "python", "java", "c++", "sql", "docker", "kubernetes",
    "react", "node", "flask", "django", "ml", "api", "aws"
]

def extract_skills(text: str):
    text = text.lower()
    return [s for s in SKILL_SET if s in text]

def skill_coverage(jd_skills, resume_skills):
    matched = list(set(jd_skills) & set(resume_skills))
    missing = list(set(jd_skills) - set(resume_skills))
    coverage = len(matched) / max(len(jd_skills), 1)
    return matched, missing, coverage
