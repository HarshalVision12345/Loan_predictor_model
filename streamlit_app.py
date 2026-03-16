import streamlit as st
import requests

st.title("🏦 Loan Prediction App (FastAPI + Streamlit)")

# User input form
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_term = st.selectbox("Loan Amount Term", [360, 180, 120, 60])
credit_history = st.selectbox("Credit History", [1.0, 0.0])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

input_data = {
    "Gender": gender,
    "Married": married,
    "Education": education,
    "Self_Employed": self_employed,
    "ApplicantIncome": applicant_income,
    "CoapplicantIncome": coapplicant_income,
    "LoanAmount": loan_amount,
    "Loan_Amount_Term": loan_term,
    "Credit_History": credit_history,
    "Property_Area": property_area
}

if st.button("Predict Loan Approval"):
    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=input_data)
        if response.status_code == 200:
            prediction = response.json()["prediction"]
            st.success(f"✅ Loan Prediction: {prediction}")
        else:
            st.error("❌ Backend error, check FastAPI logs")
    except Exception as e:
        st.error("⚠️ Could not connect to FastAPI. Is it running?")