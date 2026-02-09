def quality_score(text: str):
    score = 1.0
    if len(text.split()) < 200:
        score -= 0.3
    if sum(c.isdigit() for c in text) < 5:
        score -= 0.2
    if "github" not in text.lower():
        score -= 0.2
    return max(score, 0.0)

def generate_feedback(missing_skills, quality):
    fb = []
    if missing_skills:
        fb.append(f"Add experience or projects using: {', '.join(missing_skills)}.")
    if quality < 0.7:
        fb.append("Quantify achievements using metrics (percentages, counts, latency, throughput).")
    return fb
