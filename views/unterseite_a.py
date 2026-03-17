import streamlit as st
from functions.calculator import  multiplication
import pandas as pd 
from utils.data_manager import DataManager

st.title("Multiplication")

st.write("Diese Seite ist eine Unterseite der Startseite.")

st.divider()
number_a = st.number_input("")
number_b = st.number_input(" ")
st.divider()

if st.button("submitt"):
    result = multiplication(number_a,number_b)
    st.session_state['data_df'] = pd.concat([st.session_state['data_df'], pd.DataFrame(data = {"multiplication" : [result]})])

        # --- CODE UPDATE: save data to data manager ---
    data_manager = DataManager()
    data_manager.save_user_data(st.session_state['data_df'], 'data.csv')


st.write(st.session_state["data_df"])
