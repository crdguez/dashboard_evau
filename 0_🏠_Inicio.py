import streamlit as st
import pandas as pd

st.write('Hola')
st.dataframe(pd.read_csv('datos.csv',encoding='latin-1'))
