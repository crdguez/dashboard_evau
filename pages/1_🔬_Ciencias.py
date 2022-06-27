import streamlit as st
import pandas as pd

st.title('EVAU Ciencias')

df_datos = pd.read_csv('datos.csv',sep =';')

st.write(df_datos.enunciado)
for ej in df_datos :
  st.image('img/'+str(ej.enunciado))
