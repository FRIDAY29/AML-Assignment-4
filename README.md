# AML-Assignment-4
# Breast Cancer Prediction App
=============================

A Streamlit app for predicting breast cancer diagnosis based on user input.

## Description

This app uses a trained machine learning model to predict the likelihood of breast cancer based on four input features: mean radius, mean texture, mean perimeter, and mean area. The model is loaded from a `model.jolib` file and used to make predictions on new data.

## Usage

1. Clone the repository: `git clone https://github.com/FRIDAY29/AML-Assignment-4.git`
2. Install the dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`
4. Open a web browser and navigate to `http://localhost:8501`

## Input Features

The app accepts the following input features:

* Mean Radius: a value between 0.0 and 30.0
* Mean Texture: a value between 0.0 and 30.0
* Mean Perimeter: a value between 0.0 and 200.0
* Mean Area: a value between 0.0 and 2000.0

## Model

The app uses a trained machine learning model stored in `breast_cancer_model.jolib`. The model was trained on a dataset of breast cancer samples and can make predictions on new data.


