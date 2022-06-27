import streamlit as st
import pandas as pd

st.title('EVAU Ciencias')

df_datos = pd.read_csv('datos.csv',sep =';')

