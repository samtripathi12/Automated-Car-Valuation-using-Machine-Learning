import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(page_title="Car Price Prediction")

st.title("🚗 Used Car Price Prediction")

st.write("Enter car details below:")

# Example inputs (modify based on your dataset)
year = st.number_input("Year of Purchase", 2000, 2024)
present_price = st.number_input("Present Price (in lakhs)")
kms_driven = st.number_input("Kilometers Driven")
owner = st.selectbox("Owner", [0, 1, 2, 3])
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])

if st.button("Predict Price"):
    st.success("Model prediction will appear here (after model file added)")
