import streamlit as st
from predict_page import show_predict_page
from chart_page import show_chart_page

if "page" not in st.session_state:
    st.session_state.page = "Predict"

st.sidebar.markdown("## Navigate")

if st.sidebar.button("Predict Salary"):
    st.session_state.page = "Predict"

if st.sidebar.button("Explore Charts"):
    st.session_state.page = "Chart"

if st.session_state.page == "Predict":
    show_predict_page()
else:
    show_chart_page()
