import streamlit as st

st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="centered"
)

st.title("❤️ Heart Disease Prediction System")
st.write("Enter the patient's details below and click **Predict**.")

age = st.number_input("Age", 1, 100, 45)

sex = st.selectbox("Sex", ["Male", "Female"])

cp = st.selectbox(
    "Chest Pain Type",
    ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"]
)

trestbps = st.number_input("Resting Blood Pressure", 80, 250, 120)

chol = st.number_input("Cholesterol (mg/dL)", 100, 600, 200)

fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", ["No", "Yes"])

restecg = st.selectbox(
    "Resting ECG",
    ["Normal", "ST-T Abnormality", "Left Ventricular Hypertrophy"]
)

thalach = st.slider("Maximum Heart Rate", 60, 220, 150)

exang = st.selectbox("Exercise Induced Angina", ["No", "Yes"])

oldpeak = st.slider("Oldpeak", 0.0, 6.5, 1.0)

if st.button("🔍 Predict Heart Disease"):

    risk = 0

    if age > 50:
        risk += 1

    if trestbps > 140:
        risk += 1

    if chol > 240:
        risk += 1

    if exang == "Yes":
        risk += 1

    if oldpeak > 2:
        risk += 1

    if risk >= 3:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")

st.markdown("---")
st.caption("Developed by Shaikh Mohammed Talha")