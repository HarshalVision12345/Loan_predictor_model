import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# 1. Load the dataset
data = pd.read_csv("loan_dataset.csv")
print("Dataset loaded successfully with shape:", data.shape)



# 3. Drop Loan_ID if present
if "Loan_ID" in data.columns:
    data = data.drop("Loan_ID", axis=1)

# 4. Fix Dependents column ("3+" → 3, fill NaN, convert to int)
if "Dependents" in data.columns:
    data["Dependents"] = data["Dependents"].replace("3+", 3)
    data["Dependents"] = data["Dependents"].fillna(data["Dependents"].mode()[0])
    data["Dependents"] = data["Dependents"].astype(int)

# 5. Handle missing values
numeric_cols = data.select_dtypes(include=[np.number]).columns
categorical_cols = data.select_dtypes(include=["object"]).columns

for col in numeric_cols:
    data[col] = data[col].fillna(data[col].mean())

for col in categorical_cols:
    data[col] = data[col].fillna(data[col].mode()[0])

# 6. Label encode categorical columns
cols_to_encode = [
    "Gender",
    "Married",
    "Education",
    "Self_Employed",
    "Property_Area",
    "Loan_Status",
]

label_encoders = {}
for col in cols_to_encode:
    if col in data.columns:
        le = LabelEncoder()
        data[col] = le.fit_transform(data[col])
        label_encoders[col] = le

# 7. Split features and target
X = data.drop("Loan_Status", axis=1)
y = data["Loan_Status"]
columns_list = list(X.columns)

# 8. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# 9. Train Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 10. Evaluate
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print("Accuracy:", acc)

# 11. Save model and columns
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("columns.pkl", "wb") as f:
    pickle.dump(columns_list, f)

print("Model saved as model.pkl")
print("Columns saved as columns.pkl")