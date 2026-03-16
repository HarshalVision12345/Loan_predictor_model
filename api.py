from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle

# Load model and columns
model = pickle.load(open("model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

app = FastAPI(title="Loan Prediction API")

class LoanInput(BaseModel):
    Gender: str
    Married: str
    Education: str
    Self_Employed: str
    ApplicantIncome: float
    CoapplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: int
    Credit_History: float
    Property_Area: str

@app.post("/predict")
def predict_loan(data: LoanInput):
    df = pd.DataFrame([data.dict()])
    df = pd.get_dummies(df)
    df = df.reindex(columns=columns, fill_value=0)
    prediction = model.predict(df)[0]
    return {"prediction": str(prediction)}