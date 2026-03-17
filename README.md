link to new app- https://updatedmotorapp-nsedbk882u5shngej9ulog.streamlit.app
Three-Phase Induction Motor Fault Prediction App
Overview
This project is a predictive application for three-phase induction motors that determines whether a motor is healthy or faulty based on current and other extracted features. The app leverages machine learning models to provide accurate predictions, with a focus on feature engineering and model performance comparison.
Project Background
Initially, the dataset for this project was created using MATLAB. Features were extracted from the starter current using Fourier Transform and other signal processing techniques. This process generated a dataset of approximately 800–1000 rows, which was used to train an Artificial Neural Network (ANN).
The initial results were promising:
High accuracy in training, validation, and testing.
Simple decision boundaries due to narrow feature ranges.
However, limitations included:
Limited dataset size.
Small feature ranges, which made the decision boundary trivial for the ANN.
previous app - https://motor-fault-detection-sifrh47ct8w3q9f4iz5frj.streamlit.app
Updated Dataset and Feature Expansion
To improve the robustness of the model:
The dataset was expanded to ~4000 rows.
Feature set was significantly expanded to capture more nuanced patterns.
Labels were also expanded and refined for better representation of motor states.
This enhanced dataset enabled better learning and differentiation between motor conditions.
Model Development and Comparison
Two models were tested on the updated dataset:
Artificial Neural Network (ANN)
Complex architecture capable of capturing overlapping feature patterns.
Demonstrated strong accuracy (>95%) across all metrics.
Better at distinguishing between subtle differences in features.
Random Forest
Provided good overall accuracy (>95%).
Faced challenges with overlapping feature ranges, leading to less nuanced predictions compared to ANN.
A detailed comparison of the models, including metrics and visualizations, is provided in Model_Comparison.pdf.
Deployment
The current version of the app is deployed using Random Forest due to deployment issues with TensorFlow/ANN models.
Future versions will aim to deploy the ANN model for potentially improved prediction accuracy.
App Features
User-friendly interface to input motor measurements.
Real-time prediction of motor status: Healthy or Faulty.
Display of extracted features for transparency and analysis.
Technologies Used
MATLAB – Feature extraction and initial dataset generation.
Python (scikit-learn, TensorFlow) – Model development (ANN and Random Forest).
Streamlit – App interface and deployment.
Future Work
Deploy the ANN model using TensorFlow for enhanced feature differentiation.
Expand the dataset further for more complex motor conditions.
Include additional feature extraction techniques to improve model robustness.
