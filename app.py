import joblib
import streamlit as st


# Load the trained logistic regression model
model = joblib.load('logistic_regression_model.pkl')

# Define the Streamlit app
st.title("Diabetes Prediction App")
st.write("Enter patient details to predict diabetes probability:")

# Input fields for user to enter patient details
pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20, value=0)
glucose = st.number_input("Glucose Level", min_value=0, max_value=  200, value=100)
blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=150   , value=70)
skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
insulin = st.number_input("Insulin Level", min_value=0, max_value=900, value=80)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0)
diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.5)
age = st.number_input("Age", min_value=1, max_value=120, value=30)


# Predict button
if st.button("Predict"):
    # Prepare the input data for prediction
    input_data = [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]]
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Display the result
    if prediction[0] == 1:
        st.error(f"The model predicts that the patient has diabetes.")
    else:
        st.success(f"The model predicts that the patient does not have diabetes.")     
