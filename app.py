# Import necessary libraries
import streamlit as st
import pandas as pd
import joblib

# Load the trained model
@st.cache
def load_model():
    model = joblib.load("breast_cancer_model.jolib")
    return model

# Create the Streamlit app
st.title("Breast Cancer Prediction App")

# Load the model
model = load_model()

# Create a sidebar for user input
st.sidebar.header("User Input")
mean_radius = st.sidebar.slider("Mean Radius", 0.0, 30.0, 10.0)
mean_texture = st.sidebar.slider("Mean Texture", 0.0, 30.0, 10.0)
mean_perimeter = st.sidebar.slider("Mean Perimeter", 0.0, 200.0, 100.0)
mean_area = st.sidebar.slider("Mean Area", 0.0, 2000.0, 1000.0)

# Create a button to trigger model prediction
if st.sidebar.button("Predict"):
    # Create a new sample based on user input
    new_sample = pd.DataFrame({
        "mean_radius": [mean_radius],
        "mean_texture": [mean_texture],
        "mean_perimeter": [mean_perimeter],
        "mean_area": [mean_area]
    })

    # Make a prediction on the new sample
    prediction = model.predict(new_sample)

    # Display the results
    st.header("Model Prediction")
    st.write("Prediction:", prediction[0])