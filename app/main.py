import streamlit as st
import numpy as np
import pickle

# Load model and scaler
model = pickle.load(open("models/heart_model.pkl", "rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))

st.set_page_config(page_title="Heart Disease Predictor", layout="centered")
st.title("💓 Heart Disease Prediction App")

st.markdown(
    "Provide the patient details below to predict the likelihood of heart disease."
)

# Input form
with st.form("input_form"):
    age = st.slider("Age", 20, 100, 50)
    sex = st.selectbox("Sex", ["Male", "Female"])  # 1 = Male, 0 = Female
    cp = st.selectbox(
        "Chest Pain Type",
        [
            "Typical Angina (0)",
            "Atypical Angina (1)",
            "Non-anginal Pain (2)",
            "Asymptomatic (3)",
        ],
    )
    trestbps = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
    chol = st.number_input("Cholesterol (mg/dl)", 100, 600, 200)
    fbs = st.radio("Fasting Blood Sugar > 120 mg/dl", ["Yes", "No"])  # 1 = Yes, 0 = No
    restecg = st.selectbox(
        "Resting ECG",
        ["Normal (0)", "ST-T wave abnormality (1)", "Left ventricular hypertrophy (2)"],
    )
    thalach = st.slider("Max Heart Rate Achieved", 60, 220, 150)
    exang = st.radio("Exercise Induced Angina", ["Yes", "No"])  # 1 = Yes, 0 = No
    oldpeak = st.slider("ST Depression (Oldpeak)", 0.0, 6.0, 1.0)
    slope = st.selectbox(
        "Slope of ST Segment", ["Upsloping (0)", "Flat (1)", "Downsloping (2)"]
    )
    ca = st.slider("Number of Major Vessels Colored", 0, 4, 0)
    thal = st.selectbox(
        "Thalassemia", ["Normal (1)", "Fixed Defect (2)", "Reversible Defect (3)"]
    )

    submitted = st.form_submit_button("Predict")

# Encode inputs
if submitted:
    input_data = np.array(
        [
            [
                age,
                1 if sex == "Male" else 0,
                int(cp[cp.find("(") + 1 : cp.find(")")]),
                trestbps,
                chol,
                1 if fbs == "Yes" else 0,
                int(restecg[restecg.find("(") + 1 : restecg.find(")")]),
                thalach,
                1 if exang == "Yes" else 0,
                oldpeak,
                int(slope[slope.find("(") + 1 : slope.find(")")]),
                ca,
                int(thal[thal.find("(") + 1 : thal.find(")")]),
            ]
        ]
    )

    # Scale and predict
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]

    if prediction == 1:
        st.error("⚠️ The model predicts a high risk of heart disease.")
    else:
        st.success("✅ The model predicts a low risk of heart disease.")
