from sklearn.metrics.pairwise import cosine_similarity

def semantic_similarity(jd_emb, resume_emb):
    return float(cosine_similarity([jd_emb], [resume_emb])[0][0])

def final_score(semantic, skill_cov, project_score, quality, penalty):
    return (
        0.4 * semantic +
        0.25 * skill_cov +
        0.15 * project_score +
        0.10 * quality -
        0.10 * penalty
    )
