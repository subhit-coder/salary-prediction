import streamlit as st
import pandas as pd
import joblib

# ---------------- Load Model ----------------
@st.cache_resource
def load_model():
    try:
        model = joblib.load("linear_pipe.pkl")
        return model
    except:
        return None

model = load_model()

# ---------------- UI ----------------
st.title("💼 Salary Prediction App")
st.markdown("Enter details to predict salary")

# ---------------- User Inputs ----------------
col1, col2 = st.columns(2)

with col1:
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

with col2:
    location = st.selectbox("Location", [
        "India", "USA", "UK", "Canada", "Germany"
    ])

    remote_work = st.selectbox("Remote Work", [
        "Yes", "No", "Hybrid"
    ])

    certifications = st.number_input("Certifications", min_value=0, max_value=20, step=1)

    experience_years = st.number_input("Experience (Years)", min_value=0, max_value=50, step=1)

    skills_count = st.number_input("Skills Count", min_value=0, max_value=50, step=1)

# ---------------- Prediction ----------------
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
        st.success(f"💰 Predicted Salary: ₹ {round(prediction, 2)}")

    except Exception as e:
        st.error(f"Error: {e}")