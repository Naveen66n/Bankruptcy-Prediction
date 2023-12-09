import pickle
import streamlit as st
import pandas as pd
import numpy as np

# Load the model
pickle_in = open("model_poly.pkl", "rb")
classifier = pickle.load(pickle_in)

# Function to predict bankruptcy
def predict_bankruptcy(industrial_risk, management_risk, financial_flexibility, credibility, competitiveness, operating_risk):
    prediction = classifier.predict([[industrial_risk, management_risk, financial_flexibility, credibility, competitiveness, operating_risk]])
    return "Non-Bankrupt" if prediction[0] == 1 else "Bankrupt"

# Main function for the Streamlit app
def main():
    # Set page title and add some styling
    st.set_page_config(
        page_title="Bankruptcy Detector",
        page_icon="💼",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.title("Bankruptcy Detector")
    st.markdown(
        """
        Welcome to the Bankruptcy Detector app! Use the sliders to input risk factors,
        and the app will predict whether a company is likely to go bankrupt or not.
        """
    )

    # Sidebar with instructions
    st.sidebar.title("Instructions")
    st.sidebar.info(
        "Adjust the sliders to set the risk factors for a company. "
        "Click the 'Predict' button to see the prediction."
    )

    # Set the options for the slider
    slider_options = [0.0, 0.5, 1.0]

    # Sliders for risk factors
    industrial_risk = st.slider("Industrial Risk", min_value=0.0, max_value=1.0, step=0.5, value=0.5, key="industrial")
    management_risk = st.slider("Management Risk", min_value=0.0, max_value=1.0, step=0.5, value=0.5, key="management")
    financial_flexibility = st.slider("Financial Flexibility", min_value=0.0, max_value=1.0, step=0.5, value=0.5, key="financial")
    credibility = st.slider("Credibility", min_value=0.0, max_value=1.0, step=0.5, value=0.5, key="credibility")
    competitiveness = st.slider("Competitiveness", min_value=0.0, max_value=1.0, step=0.5, value=0.5, key="competitiveness")
    operating_risk = st.slider("Operating Risk", min_value=0.0, max_value=1.0, step=0.5, value=0.5, key="operating")

    # Add a button to trigger prediction
    if st.button("Predict"):
        prediction = predict_bankruptcy(industrial_risk, management_risk, financial_flexibility, credibility, competitiveness, operating_risk)
        
        # Highlight prediction result with background color
        if prediction == "Bankrupt":
            result_color = "red"
        else:
            result_color = "green"
            
        st.markdown(f'<div style="background-color: {result_color}; padding: 10px; border-radius: 5px;">', unsafe_allow_html=True)
        st.success(f"The prediction is: {prediction}")
        st.markdown('</div>', unsafe_allow_html=True)

    

# Run the app
if __name__ == "__main__":
    main()
