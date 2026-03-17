import joblib
import streamlit as st
import numpy as np


# LOAD MODELS SAFELY


# Random Forest
try:
    rf_model = joblib.load("random_forest_motor_fault.pkl")
except Exception as e:
    st.error(f"Error loading Random Forest model: {e}")
    rf_model = None

# ANN
try:
    scaler, ann_model = joblib.load("motor2.pkl")
except Exception as e:
    st.error(f"Error loading ANN model: {e}")
    scaler, ann_model = None, None

# ------------------------------
# STYLE
# ------------------------------

st.markdown("""
<style>
/* Main background and font */
[data-testid="stAppViewContainer"] {
    background-color: #ffffff;  /* Keep it white */
    font-family: 'Helvetica', 'Arial', sans-serif;
}

/* Headings */
h1 {
    text-align: center;
    color: #0f172a !important;
    font-weight: 900 !important;
    font-size: 3rem !important;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
}

h2, h3 {
    color: #1e293b !important;
    font-weight: 700 !important;
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
}

/* Paragraphs and list items */
p, li {
    color: #334155;
    font-size: 18px;
    line-height: 1.6;
}

/* Info boxes */
.stInfo {
    background-color: #f9fafbcc;
    border-left: 5px solid #0f172a;
    padding: 1rem;
    border-radius: 8px;
    color: #0f172a;
}

/* Buttons */
.stButton>button {
    background-color: #0f172a;
    color: #ffffff;
    font-weight: 600;
    border-radius: 6px;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color:#d9e2ec;
    font-family: 'Helvetica', 'Arial', sans-serif;
}
</style>
""", unsafe_allow_html=True)


# FAULT LABELS


fault_labels = {
    0: "Healthy Motor",
    1: "Noise + Harmonics Fault",
    2: "Amplitude Modulation Fault",
    3: "Frequency Fault (Slip-based)",
    4: "Broken Rotor Bar Fault"
}


# PAGE NAVIGATION


if "page" not in st.session_state:
    st.session_state.page = "intro"


# INTRO PAGE


if st.session_state.page == "intro":

    st.markdown("<h1>Three-Phase Induction Motor Fault Detection</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        st.write("""
This application demonstrates **machine learning-based fault detection for
three-phase induction motors** using statistical and spectral features.

Induction motors are widely used in industrial systems and early detection
helps prevent:

• unexpected downtime  
• mechanical damage  
• expensive maintenance  
• industrial production losses
""")

        st.subheader("Why Two Models Were Used")

        st.write("""

**Random Forest**

• Excellent for tabular datasets  
• Interpretable feature importance  
• Very stable predictions  

**Artificial Neural Network**

• Captures nonlinear patterns  
• Good for signal-based features  
• Handles complex relationships
""")

        st.write("""
Both models performed well, therefore the user can choose
either model for prediction.
""")

        if st.button("Start Prediction"):

            st.session_state.page = "predict"
            st.rerun()


# PREDICTION PAGE


if st.session_state.page == "predict":

    st.title("Motor Fault Prediction")

    model_choice = st.selectbox(
        "Select Model",
        ["Random Forest", "Artificial Neural Network"]
    )

    st.subheader("Enter Feature Values")

    rms = st.number_input("RMS", 0.25, 1.10, 0.6)
    peak = st.number_input("Peak", 0.4, 2.1, 1.0)
    dom_freq = st.number_input("Dominant Frequency (Hz)", 47.0, 51.0, 50.0)
    peak_mag = st.number_input("Peak Magnitude", 0.05, 1.1, 0.5)
    spec_energy = st.number_input("Spectral Energy", 0.03, 0.55, 0.2)
    sideband_energy = st.number_input("Sideband Energy", 0.03, 0.55, 0.2)
    kurtosis = st.number_input("Kurtosis", 1.4, 2.8, 1.7)
    skewness = st.number_input("Skewness", -0.02, 0.06, 0.0)
    crest = st.number_input("Crest Factor", 1.4, 2.6, 1.8)

    features = np.array([[

        rms,
        peak,
        dom_freq,
        peak_mag,
        spec_energy,
        sideband_energy,
        kurtosis,
        skewness,
        crest

    ]])

    st.info("""
      Predictions are reliable only when feature values fall within realistic
      motor operating ranges.
""")

    if st.button("Predict Fault Condition"):

        if model_choice == "Random Forest":
            if rf_model is not None:
                prediction = rf_model.predict(features)
                result = fault_labels[int(prediction[0])]
                st.success(f"Predicted Motor Condition: {result}")
            else:
                st.error("Random Forest model not loaded!")

        else:  # ANN
            if ann_model is not None and scaler is not None:
                features_scaled = scaler.transform(features)
                prediction = ann_model.predict(features_scaled)
                prediction = np.argmax(prediction, axis=1)
                result = fault_labels[int(prediction[0])]
                st.success(f"Predicted Motor Condition: {result}")
            else:
                st.error("ANN model or scaler not loaded!")