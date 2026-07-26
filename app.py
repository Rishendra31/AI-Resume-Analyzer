import streamlit as st
from utils.pdf_reader import read_pdf
from utils.resume_parser import extract_skills
from utils.ats_score import calculate_ats_score
from utils.similarity import calculate_similarity, find_missing_skills
from utils.llm import get_ai_feedback

# ── Mobile-friendly page config ──
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered",  # ← KEY FIX: "wide" breaks mobile layout
    initial_sidebar_state="collapsed"
)

# ── Session State Init ──
if "resume_text" not in st.session_state:
    st.session_state.resume_text = ""
if "skills" not in st.session_state:
    st.session_state.skills = []
if "ats_score" not in st.session_state:
    st.session_state.ats_score = 0
if "similarity" not in st.session_state:
    st.session_state.similarity = 0.0
if "missing_skills" not in st.session_state:
    st.session_state.missing_skills = []
if "feedback" not in st.session_state:
    st.session_state.feedback = ""
if "analyzed" not in st.session_state:
    st.session_state.analyzed = False

# ── UI ──
st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and compare it with a Job Description.")

# ── Form: Prevents rerun on every mobile interaction ──
with st.form("resume_form", clear_on_submit=False):
    uploaded_file = st.file_uploader(
        "Upload Resume (PDF)",
        type=["pdf"],
        accept_multiple_files=False,
        help="Select a PDF from your device. If the picker doesn't show PDFs, choose 'Browse'."
    )
    
    job_description = st.text_area(
        "Paste Job Description",
        height=200,  # ← Reduced for mobile screens
        placeholder="Paste the job description here..."
    )
    
    # Use columns so buttons don't stack awkwardly on mobile
    col1, col2 = st.columns(2)
    with col1:
        analyze_btn = st.form_submit_button(
            "🔍 Analyze Resume",
            use_container_width=True,
            type="primary"
        )
    with col2:
        clear_btn = st.form_submit_button(
            "🗑️ Clear",
            use_container_width=True
        )

# ── Clear Logic ──
if clear_btn:
    for key in ["resume_text", "skills", "ats_score", "similarity", "missing_skills", "feedback", "analyzed"]:
        st.session_state[key] = "" if key == "resume_text" else ([] if key in ["skills", "missing_skills"] else (0 if key == "ats_score" else (0.0 if key == "similarity" else False)))
    if "feedback" in st.session_state:
        st.session_state.feedback = ""
    st.rerun()

# ── Analysis Logic ──
if analyze_btn:
    if not uploaded_file:
        st.error("⚠️ Please upload a PDF resume first.")
    elif not job_description.strip():
        st.warning("⚠️ Please paste a job description for full analysis.")
    else:
        with st.spinner("📖 Reading PDF... (this may take a moment on mobile)"):
            try:
                resume_text = read_pdf(uploaded_file)
                if not resume_text or len(resume_text.strip()) < 50:
                    st.error("⚠️ Could not extract text from this PDF. It might be a scanned image. Try a text-based PDF.")
                    st.stop()
            except Exception as e:
                st.error(f"❌ Error reading PDF: {e}")
                st.stop()

        # Store everything in session state so it survives reruns
        st.session_state.resume_text = resume_text
        st.session_state.skills = extract_skills(resume_text)
        st.session_state.ats_score = calculate_ats_score(resume_text)
        
        if job_description.strip():
            st.session_state.similarity = calculate_similarity(resume_text, job_description)
            st.session_state.missing_skills = find_missing_skills(
                st.session_state.skills,
                job_description
            )
            
            with st.spinner("🤖 Generating AI feedback... (may take 5-10s on mobile data)"):
                try:
                    st.session_state.feedback = get_ai_feedback(
                        resume_text,
                        job_description,
                        st.session_state.ats_score,
                        st.session_state.similarity,
                        st.session_state.missing_skills
                    )
                except Exception as e:
                    st.session_state.feedback = f"Error generating AI feedback: {e}"
        else:
            st.session_state.similarity = 0.0
            st.session_state.missing_skills = []
            st.session_state.feedback = "Paste a job description to get AI feedback and skill gap analysis."
        
        st.session_state.analyzed = True
        st.rerun()

# ── Display Results (persists after rerun thanks to session_state) ──
if st.session_state.analyzed:
    st.divider()
    
    st.subheader("📝 Extracted Resume Text")
    st.text_area(
        "Preview",
        st.session_state.resume_text,
        height=200,
        disabled=True,
        label_visibility="collapsed"
    )
    
    # Metrics in columns that stack on mobile
    m1, m2 = st.columns(2)
    with m1:
        st.subheader("🎯 ATS Score")
        st.metric("Score", f"{st.session_state.ats_score}/100")
    with m2:
        if job_description.strip() or st.session_state.similarity > 0:
            st.subheader("🎯 Job Match")
            st.metric("Match", f"{st.session_state.similarity:.1f}%")
    
    st.subheader("🛠️ Skills Found")
    if st.session_state.skills:
        # Use pills/chips style for mobile readability
        skill_html = " ".join([f'<span style="display:inline-block;background:#e8f4f8;color:#0066cc;padding:4px 10px;border-radius:12px;margin:3px;font-size:14px;">{s}</span>' for s in st.session_state.skills])
        st.markdown(skill_html, unsafe_allow_html=True)
    else:
        st.warning("No skills detected.")
    
    if st.session_state.missing_skills:
        st.subheader("⚠️ Missing Skills")
        for skill in st.session_state.missing_skills:
            st.write(f"• {skill}")
    
    if st.session_state.feedback:
        st.subheader("💡 AI Feedback")
        st.markdown(st.session_state.feedback)

# ── Mobile CSS tweaks ──
st.markdown("""
<style>
    /* Prevent horizontal scroll on mobile */
    .main .block-container {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: 100% !important;
    }
    /* Make textareas more touch-friendly */
    textarea {
        font-size: 16px !important; /* Prevents iOS zoom on focus */
    }
    /* Ensure buttons are tappable */
    button {
        min-height: 44px !important;
    }
</style>
""", unsafe_allow_html=True)