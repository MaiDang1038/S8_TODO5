import streamlit as st
import pickle
import numpy as np

st.title("Revenue Prediction")
model = pickle.load(open('model.pickle', 'rb'))

inputvar = st.number_input('Input Variable')
if st.button("Predict"):
    result = model.predict(np.array([[inputvar]]))
    result = result[0]
    st.text("Revenue Prediction")
    st.success(result)

# streamlit run S8_TODO5.py  
