# Three-Phase Induction Motor Fault Prediction App

link to new app- https://updatedmotorapp-nsedbk882u5shngej9ulog.streamlit.app
## Overview
This application predicts the condition of three-phase induction motors, determining whether a motor is **Healthy** or **Faulty** based on extracted features from starter currents. It is designed to support predictive maintenance by providing accurate real-time insights.

---

## Initial Approach
The project initially used **MATLAB** to generate a dataset by extracting multiple features from the starter current using **Fourier Transform** and other signal processing techniques. This process created a dataset of approximately **800–1000 rows**.

An **Artificial Neural Network (ANN)** was trained on this dataset, achieving high accuracy across training, validation, and testing. However, the narrow feature ranges simplified the decision boundaries, which limited the model’s real-world robustness.
previous app- https://motor-fault-detection-sifrh47ct8w3q9f4iz5frj.streamlit.app

---

## Dataset Expansion
To improve model performance and generalization:
- The dataset was expanded to around **4000 rows**.
- Features were significantly enhanced to capture more nuanced patterns.
- Labels were refined for better representation of motor states.

This expanded dataset allowed the models to learn more complex relationships between features.

---

## Model Development and Comparison
Two models were tested on the updated dataset:

### 1. Artificial Neural Network (ANN)
- Capable of handling overlapping feature ranges.
- Achieved **>95% accuracy**.
- Demonstrated strong differentiation between subtle motor conditions.

### 2. Random Forest
- Also achieved **>95% accuracy**.
- Less effective at distinguishing overlapping features compared to ANN.

> A detailed comparison of the models can be found in Model_Comparison pdf above.

---

## Deployment
- The current app is deployed using **Random Forest** due to deployment challenges with TensorFlow/ANN.
- Future updates aim to deploy the **ANN model** for improved accuracy and feature sensitivity.

---

## App Features
- Simple and intuitive user interface.
- Real-time prediction: **Healthy** or **Faulty(types of fault)**.

---

## Technologies Used
- **MATLAB** – Feature extraction and dataset creation.
- **Python (scikit-learn, TensorFlow)** – Model development and training.
- **Streamlit** – Web application interface and deployment.

---

## Future Work
- Deploy the ANN model using TensorFlow.
- Further expand the dataset for complex motor conditions.
- Introduce additional feature extraction techniques for higher prediction robustness.
