st.set_page_config(page_title="AI Resume Screener", layout="wide")
st.title("📄 AI Resume Ranking System")
st.markdown("---")

# 2. The Sidebar (Where you put the Job Description)
with st.sidebar:
    st.header("Job Settings")
    jd_input = st.text_area("Paste Job Description here:", height=300)
    st.info("The AI will use this to rank the resumes.")

# 3. Main Area (File Upload)
st.subheader("Upload Candidate Resumes")
uploaded_files = st.file_uploader(
    "Choose PDF files", 
    type="pdf", 
    accept_multiple_files=True
)

# 4. The Action Button
if st.button("🚀 Start Ranking"):
    if not uploaded_files:
        st.error("Please upload some resumes first!")
    elif not jd_input:
        st.warning("Please provide a Job Description.")
    else:
        st.success(f"Processing {len(uploaded_files)} resumes...")
        # This is where you will call your Step 2 logic!


