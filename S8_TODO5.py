import streamlit as st
from sklearn.linear_model import LinearRegression
import pickle
import numpy as np

st.title("Revenue Prediction")
with open("C:/Users/HP/Downloads/VS CODE/Study_Python/MathCoding4AI/model.pickle", 'rb') as model_file:
    model = pickle.load(model_file)

inputvar = st.number_input('Input Variable')
if st.button("Predict"):
    result = model.predict(np.array([[inputvar]]))
    result = result[0]
    st.success(result)

# streamlit run S8_TODO5.py  