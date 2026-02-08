# 🩺 Diabetes Prediction Using Logistic Regression
### Overview

This is an AI-powered web app that predicts the risk of diabetes based on patient information.
Built using **Python**, **Streamlit**, and **scikit-learn**, it provides an interactive clinical risk assessment dashboard.

---

### Detailed Analysis

A complete exploratory data analysis, feature engineering, model training and 
evaluation is documented in the notebook:📔[Colab Notebook-Full ML Blog](https://colab.research.google.com/drive/1S0pS1fB5LzqKoaUNcT4vCCARPQZOog3t#scrollTo=l2g8E795Osz6)

---

### Live Demo

You can try the app here: [open app](https://diabetic-prediction-gzyh99vptzfju8zkcbd9l9.streamlit.app/#120)🌐

---

### 📷Screenshot

<img width="1729" height="870" alt="Screenshot 2026-02-02 200232" src="https://github.com/user-attachments/assets/d1388724-edfc-40e8-a63d-87a2ae7a2a57" />

---

### 🎥Demo video

![ScreenRecording2026-02-09011227-ezgif com-optimize](https://github.com/user-attachments/assets/a8daef7b-a775-4e87-85ec-63b78a9a68e5)

---

### Features

* Input patient data via sliders in the sidebar

* Predict diabetes risk instantly with a **probability score**

* Interactive dashboard with **metrics like Glucose, BMI, Age**

* Clean, modern UI with custom styling


### Installation (Local)

**1.** Clone the repository:

```bash
git clone https://github.com/Rabindrajena/diabetic-prediction.git
```

**2.** Create and activate a Python 3.11 virtual environment:

```bash
python -m venv venv
.\venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
```

**3.** Install dependencies:

```bash
pip install -r requirements.txt
```

**4.** Run the app locally:

```bash
streamlit run app.py
```

### Usage

* Use the sidebar to input patient data:

* Pregnancies, Glucose, Blood Pressure, Skin Thickness, Insulin, BMI, Diabetes Pedigree Function, Age

* Click **Predict Diabetes Risk** to get:

* ✅ Low Risk

* ⚠️ High Risk with probability percentage

### Files

* `app.py` – Main Streamlit app

* `diabetes_logistic_pipeline.pkl` – Trained logistic regression model

* `requirements.txt` – Package dependencies

* `runtime.txt` – Python version for deployment

### Notes

* ⚠️ This app is for **educational purposes only** and **not a medical diagnosis**.

* Make sure to run it on **Python 3.11** to match dependencies.

### Author

**Rabindra Jena** [Github](https://github.com/Rabindrajena)
