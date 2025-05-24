
---

### ❤️ `Heart Disease Predictor` – `README.md`

# ❤️ Heart Disease Predictor

An intelligent health tool that uses machine learning to predict the presence of heart disease based on patient health metrics. Designed for easy use by both healthcare professionals and patients.

## 🚀 Demo

[👉 Live Demo Link ](https://heart-disease-predictor-ai.streamlit.app/)

## ⚙️ Features

- Predicts whether a person is likely to have heart disease.
- Built with **Streamlit** for a clean and responsive frontend.
- Accepts input via sliders and dropdowns for various medical indicators.
- Uses a **Decision Tree Classifier** trained on public heart disease dataset.

## 🧠 Model Info

- **Algorithm:** Decision Tree Classifier
- **Input Features:** Age, Sex, Cholesterol, Chest Pain Type, Blood Pressure, etc.
- **Data Preprocessing:** Normalization, missing value handling, label encoding

## 🏗 Tech Stack

- Python
- Scikit-learn
- Streamlit
- Pandas / NumPy
- Pickle

## 🛠 How to Run Locally

```bash
git clone https://github.com/your-username/heart-disease-predictor.git
cd heart-disease-predictor
pip install -r requirements.txt
streamlit run app/main.py
