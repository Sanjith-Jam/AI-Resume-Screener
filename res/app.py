import streamlit as st
from parser import extract_text_from_pdf
from embedder import embed_texts
from scorer import semantic_similarity, final_score
from skills import extract_skills, skill_coverage
from feedback import quality_score, generate_feedback

st.set_page_config(layout="wide")
st.title("Explainable Resume Ranking System")

jd_file = st.file_uploader("Upload Job Description (PDF)", type=["pdf"])
resume_files = st.file_uploader("Upload Resumes (PDF)", type=["pdf"], accept_multiple_files=True)

if jd_file and resume_files:
    jd_text = extract_text_from_pdf(jd_file)
    jd_emb = embed_texts([jd_text])[0]
    jd_skills = extract_skills(jd_text)

    results = []

    for rf in resume_files:
        res_text = extract_text_from_pdf(rf)
        res_emb = embed_texts([res_text])[0]

        semantic = semantic_similarity(jd_emb, res_emb)
        res_skills = extract_skills(res_text)
        matched, missing, coverage = skill_coverage(jd_skills, res_skills)

        quality = quality_score(res_text)
        score = final_score(semantic, coverage, 0.5, quality, 0.0)
        fb = generate_feedback(missing, quality)

        results.append({
            "name": rf.name,
            "score": score,
            "semantic": semantic,
            "matched": matched,
            "missing": missing,
            "quality": quality,
            "feedback": fb
        })

    results.sort(key=lambda x: x["score"], reverse=True)

    for r in results:
        with st.expander(r["name"]):
            st.write("Final Score:", round(r["score"], 3))
            st.write("Semantic Match:", round(r["semantic"], 3))
            st.write("Matched Skills:", r["matched"])
            st.write("Missing Skills:", r["missing"])
            st.write("Quality Score:", round(r["quality"], 2))
            st.write("Feedback:")
            for f in r["feedback"]:
                st.write("- ", f)
