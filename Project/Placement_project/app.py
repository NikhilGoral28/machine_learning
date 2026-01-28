import streamlit as st
import pickle
import numpy as np

st.title("Placement Predictor")

cgpa = st.number_input("Enter CGPA", 0.0, 10.0, 0.1)
iq = st.number_input("Enter IQ", 0.0, 200.0, 1.0)

# 🔒 fixed values from training data
cgpa_mean = 6.5
cgpa_std = 0.8
iq_mean = 110
iq_std = 15

def manual_scale(cgpa, iq):
    return np.array([[
        (cgpa - cgpa_mean) / cgpa_std,
        (iq - iq_mean) / iq_std
    ]])

model = pickle.load(open("model.pkl", "rb"))

if st.button("Predict"):
    scaled_input = manual_scale(cgpa, iq)
    prediction = model.predict(scaled_input)

    if prediction[0] == 1:
        st.success("🎉 Student will be Placed")
    else:
        st.error("❌ Student will NOT be Placed")
