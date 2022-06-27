import streamlit as st
import pandas as pd

st.title('EVAU Ciencias')

df_datos = pd.read_csv('datos.csv',sep =';')

st.write(df_datos.enunciado)
# for ej in df_datos :
#   st.write(str(ej.enunciado))

for ej in df_datos.iterrows() :
    st.header(ej[2])
    st.subheader(ej[1])
    st.write(ej)
