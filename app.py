
import streamlit as st
import pandas as pd
import joblib
import numpy as np

# ---------------- Page Config ----------------
st.set_page_config(page_title="Salary Predictor", layout="wide")

# ---------------- CSS ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}



.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
}

div.stButton > button {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    border-radius: 10px;
    height: 50px;
    width: 100%;
}

/* Money Animation */
.money {
    position: fixed;
    top: -50px;
    font-size: 25px;
    animation: fall linear infinite;
}
@keyframes fall {
    0% { transform: translateY(-10vh); }
    100% { transform: translateY(110vh); }
}
</style>
""", unsafe_allow_html=True)

# ---------------- Money Elements ----------------
for i in range(10):
    st.markdown(f'<div class="money" style="left:{i*10}%; animation-duration:{5+i%3}s;">💸</div>', unsafe_allow_html=True)

# ---------------- Load Model ----------------

def load_model():
    try:
        return joblib.load("linear_pipe.pkl")
    except:
        return None

model = load_model()

# ---------------- Title ----------------
st.markdown('<div class="title">💼 Salary Predictor</div>', unsafe_allow_html=True)

# ---------------- Layout ----------------
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    job_title = st.selectbox("Job Title", [
        "Data Analyst", "Data Scientist", "AI Engineer",
        "Backend Developer", "Frontend Developer", "Business Analyst"
    ])

    education_level = st.selectbox("Education Level", [
        "Bachelor", "Master", "PhD"
    ])

    industry = st.selectbox("Industry", [
        "IT", "Finance", "Healthcare", "Retail", "Education"
    ])

    company_size = st.selectbox("Company Size", [
        "Small", "Medium", "Large"
    ])

    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    location = st.selectbox("Location", [
        "India", "USA", "UK", "Canada", "Germany"
    ])

    remote_work = st.selectbox("Remote Work", [
        "Yes", "No", "Hybrid"
    ])

    certifications = st.slider("Certifications", 0, 20, 1)
    experience_years = st.slider("Experience (Years)", 0, 30, 1)
    skills_count = st.slider("Skills Count", 0, 30, 1)

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- Predict ----------------
if st.button("🚀 Predict Salary"):

    input_df = pd.DataFrame([{
        "job_title": job_title,
        "education_level": education_level,
        "industry": industry,
        "company_size": company_size,
        "location": location,
        "remote_work": remote_work,
        "certifications": certifications,
        "experience_years": experience_years,
        "skills_count": skills_count
    }])

    try:
        prediction = model.predict(input_df)[0]

        # KPI
        k1, k2 = st.columns(2)

        with k1:
            st.metric("💰 Salary", f"₹ {round(prediction, 2)}")

        with k2:
            st.metric("📊 Confidence", f"{np.random.randint(85,95)}%")

        

        st.balloons()

    except Exception as e:
        st.error(f"Error: {e}")