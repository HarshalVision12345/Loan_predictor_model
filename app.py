import streamlit as st
import pandas as pd
import pickle

# Load model and columns
model = pickle.load(open("model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

st.title("🏦 Loan Prediction App")

st.write("Fill in the details below to predict loan approval:")

# Collect user input
user_input = {}
for col in columns:
    user_input[col] = st.text_input(f"Enter {col}")

# Convert to DataFrame
if st.button("Predict"):
    df = pd.DataFrame([user_input], columns=columns)

    # Convert numeric columns safely
    for c in df.columns:
        try:
            df[c] = pd.to_numeric(df[c])
        except:
            pass

    prediction = model.predict(df)[0]
    result = "Approved ✅" if prediction == 1 else "Rejected ❌"
    st.success(f"Loan Status: {result}")




# import streamlit as st
# import pandas as pd
# import pickle
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier

# # -----------------------------
# # 1. Training phase (runs once)
# # -----------------------------
# @st.cache_resource
# def train_model():
#     # Load dataset
#     data = pd.read_csv("loan_dataset.csv")

#     # Drop Loan_ID if present
#     if "Loan_ID" in data.columns:
#         data = data.drop("Loan_ID", axis=1)

#     # One-hot encode categorical variables
#     data = pd.get_dummies(data)

#     # Split features and target
#     X = data.drop("Loan_Status", axis=1)   # adjust target column name if different
#     y = data["Loan_Status"]

#     # Train/test split
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#     # Train model
#     model = RandomForestClassifier(random_state=42)
#     model.fit(X_train, y_train)

#     # Save model and columns
#     pickle.dump(model, open("model.pkl", "wb"))
#     pickle.dump(X.columns, open("columns.pkl", "wb"))

#     return model, X.columns

# # Load or train model
# try:
#     model = pickle.load(open("model.pkl", "rb"))
#     columns = pickle.load(open("columns.pkl", "rb"))
# except:
#     model, columns = train_model()

# # -----------------------------
# # 2. Streamlit UI
# # -----------------------------
# st.title("🏦 Loan Prediction App")

# # User input form
# gender = st.selectbox("Gender", ["Male", "Female"])
# married = st.selectbox("Married", ["Yes", "No"])
# education = st.selectbox("Education", ["Graduate", "Not Graduate"])
# self_employed = st.selectbox("Self Employed", ["Yes", "No"])
# applicant_income = st.number_input("Applicant Income", min_value=0)
# coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
# loan_amount = st.number_input("Loan Amount", min_value=0)
# loan_term = st.selectbox("Loan Amount Term", [360, 180, 120, 60])
# credit_history = st.selectbox("Credit History", [1.0, 0.0])
# property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# # Collect input
# input_data = {
#     "Gender": gender,
#     "Married": married,
#     "Education": education,
#     "Self_Employed": self_employed,
#     "ApplicantIncome": applicant_income,
#     "CoapplicantIncome": coapplicant_income,
#     "LoanAmount": loan_amount,
#     "Loan_Amount_Term": loan_term,
#     "Credit_History": credit_history,
#     "Property_Area": property_area
# }

# df = pd.DataFrame([input_data])

# # Apply same preprocessing
# df = pd.get_dummies(df)
# df = df.reindex(columns=columns, fill_value=0)

# # Prediction button
# if st.button("Predict Loan Approval"):
#     prediction = model.predict(df)[0]
#     st.success(f"✅ Loan Prediction: {prediction}")