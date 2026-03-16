# 🏦 Loan Approval Prediction System (Dockerized)

A machine learning-based system designed to automate the loan eligibility process. This project uses a **Random Forest Classifier** to determine if a loan should be approved based on applicant profiles such as Income, Credit History, and Education.

This repository features a **FastAPI** backend for real-time predictions and is fully containerized using **Docker** for seamless deployment.



---

## 🛠️ Tech Stack
* **Machine Learning:** Random Forest (Scikit-Learn)
* **Backend:** FastAPI (Python)
* **Data Processing:** Pandas, NumPy
* **Containerization:** Docker
* **Serialization:** Pickle

---

## 📊 Dataset Features
The model is trained on the Dream Housing Finance dataset, focusing on these key factors:
- **Credit History:** A primary indicator of loan eligibility.
- **Applicant Income:** Evaluates the financial capacity of the borrower.
- **Loan Amount:** The requested capital vs. the applicant's profile.
- **Demographics:** Education, Marital Status, and Dependents.

---

## 🚀 How to Run the Project

### Using Docker (Recommended)
You can pull the latest production-ready image directly from Docker Hub. This ensures all dependencies, including Python and ML libraries, are pre-configured.

1.  **Pull the Image:**
    ```bash
    docker pull harshalrao/loan_predictor-api:latest
    ```

2.  **Run the Container:**
    ```bash
    docker run -p 8000:8000 harshalrao/loan_predictor-api:latest
    ```
    * **API Documentation:** Once the container is running, open your browser and go to `http://localhost:8000/docs`. This will open the **Interactive Swagger UI** where you can test the prediction endpoint directly.

---

## 📂 Project Highlights
* **Automated Preprocessing:** The system handles missing values and categorical encoding (LabelEncoding) automatically.
* **Production-Ready API:** Built with FastAPI, providing a high-performance REST API.
* **Dockerized:** Guaranteed to run exactly the same way on any server, eliminating "it works on my machine" issues.

---

## 📈 Model Insights
- **Algorithm:** Random Forest Classifier
- **Preprocessing:** Handled the "3+" dependents string conversion and imputed missing numerical values with column means.
- **Deployment:** Packaged using a lightweight Docker base image for faster deployment.

---

## 👤 Contact
**Harshal Rao** 📍 *Location: Raipur / Bhilai, Chhattisgarh* 📞 **Phone:** +91 6266641454  
🔗 **LinkedIn:** [Harshal Rao](https://linkedin.com/in/harshal-273744337)  
🔗 **GitHub:** [HarshalVision12345](https://github.com/HarshalVision12345)
