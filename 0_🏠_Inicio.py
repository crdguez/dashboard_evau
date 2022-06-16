import streamlit as st
import pandas as pd

st.write('Hola')

df_datos = pd.read_csv('datos.csv',sep =';',encoding='latin-1')
st.dataframe(df_datos)
st.write(df_datos.enunciado)

option = st.selectbox(
     'Bloque',
     df_datos.enunciado)

st.write('Has seleccionado:', option)
