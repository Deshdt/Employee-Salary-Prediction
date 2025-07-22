import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor_loaded = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]


def show_predict_page():

    st.markdown("""
        <style>
        div.stButton > button { 
        background-color: #F1F3F8;  
        color: black;               
        font-size: 20px;            
        padding: 0.6em 1.8em;       
        border-radius: 8px;         
        border: none;
        font-weight: bold;          
}

    div.stButton > button:hover {
    background-color: #2196F3;  
    color: white;               
}
</style>

    """, unsafe_allow_html=True)

    st.title("EMPLOYEE SALARY PREDICTION")
    st.write("### Let us predict your salary")

    countries = (
        "Australia",
        "Brazil",
        "Canada",
        "France",
        "Germany",
        "India",
        "Italy",
        "Netherland",
        "Poland",
        "Russian Federation",
        "Spain",
        "Sweden",
        "United Kingdom",
        "United States",       
    )

    education_levels = (
        "Less than a Bachelors",
        "Bachelor's degree",
        "Master's degree",
        "Post grad",
    )

    country = st.selectbox("Country", countries)
    education = st.selectbox("Education Level", education_levels)
    experience = st.slider("Years Of Experience", 0, 50, 5)

    ok = st.button("PREDICT")
    if ok:
        
        X = np.array([[country, education, experience]])
        X[:, 0] = le_country.transform(X[:, 0])
        X[:, 1] = le_education.transform(X[:, 1])
        X = X.astype(float)

        salary = regressor_loaded.predict(X)
        st.subheader(f"The estimated salary is ${salary[0]:,.2f}")

