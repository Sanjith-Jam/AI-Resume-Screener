import re

def extract_sections(text: str):
    text = text.lower()
    sections = {"skills": "", "experience": "", "projects": "", "education": ""}

    for key in sections:
        pattern = rf"{key}[:\n](.*?)(\n[A-Z][a-z]+:|\Z)"
        m = re.search(pattern, text, re.S)
        if m:
            sections[key] = m.group(1).strip()

    return sections
