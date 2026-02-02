import streamlit as st
import numpy as np
import joblib

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="🩺 Diabetic Prediction",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------
# Load Model Safely
# ----------------------------
try:
    model = joblib.load("diabetes_logistic_pipeline.pkl")
    model_loaded = True
except Exception as e:
    st.warning(f"⚠️ Could not load model: {e}")
    st.info("Prediction is disabled until the model is fixed.")
    model_loaded = False

# ----------------------------
# Custom CSS (Medical Dashboard Look)
# ----------------------------
st.markdown("""
<style>
    .main {
        background-color: #f6f9fc;
    }
    .metric-box {
        background: white;
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0px 8px 20px rgba(0,0,0,0.08);
        text-align: center;
    }
    .title-text {
        font-size: 40px;
        font-weight: 700;
        color: #0d6efd;
    }
    .subtitle-text {
        color: #6c757d;
        font-size: 18px;
    }
</style>
""", unsafe_allow_html=True)

# ----------------------------
# Header
# ----------------------------
st.markdown('<div class="title-text">🩺 Diabetic Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">AI-powered clinical risk assessment dashboard</div>', unsafe_allow_html=True)
st.markdown("---")

# ----------------------------
# Sidebar Inputs
# ----------------------------
st.sidebar.header("📋 Patient Information")

preg = st.sidebar.slider("Pregnancies", 0, 20, 1)
glucose = st.sidebar.slider("Glucose (mg/dL)", 50, 200, 120)
bp = st.sidebar.slider("Blood Pressure (mm Hg)", 40, 130, 70)
skin = st.sidebar.slider("Skin Thickness (mm)", 5, 100, 20)
insulin = st.sidebar.slider("Insulin (µU/mL)", 0, 900, 80)
bmi = st.sidebar.slider("BMI", 10.0, 60.0, 25.0)
dpf = st.sidebar.slider("Diabetes Pedigree Function", 0.0, 2.5, 0.5)
age = st.sidebar.slider("Age (years)", 10, 100, 30)

# ----------------------------
# Input Array
# ----------------------------
input_data = np.array([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])

# ----------------------------
# Layout: Metrics
# ----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f'<div class="metric-box"><h4>Glucose</h4><h2>{glucose}</h2></div>', unsafe_allow_html=True)

with col2:
    st.markdown(f'<div class="metric-box"><h4>BMI</h4><h2>{bmi}</h2></div>', unsafe_allow_html=True)

with col3:
    st.markdown(f'<div class="metric-box"><h4>Age</h4><h2>{age}</h2></div>', unsafe_allow_html=True)

st.markdown("")

# ----------------------------
# Prediction Section
# ----------------------------
if model_loaded:
    if st.button("🔍 Predict Diabetes Risk", use_container_width=True):
        try:
            prediction = model.predict(input_data)[0]
            probability = model.predict_proba(input_data)[0][1]

            st.markdown("---")

            if prediction == 1:
                st.error(f"⚠️ High Risk of Diabetes\n\n**Probability:** {probability*100:.2f}%")
            else:
                st.success(f"✅ Low Risk of Diabetes\n\n**Probability:** {probability*100:.2f}%")
        except Exception as e:
            st.error(f"❌ Error during prediction: {e}")
else:
    st.info("Prediction is disabled because the model could not be loaded.")

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.caption("⚕️ This tool is for educational purposes only. Not a medical diagnosis.")
