import streamlit as st
import pandas as pd

st.write('Hola')

#df_datos = pd.read_csv('datos.csv',sep =';',encoding='latin-1')
df_datos = pd.read_csv('datos.csv',sep =';')

st.dataframe(df_datos)
st.write(df_datos.enunciado)

option = st.sidebar.selectbox(
     'Bloque',
     df_datos.bloque.unique())

st.write('Has seleccionado:', option)
#st.image('lenna.png', width = 150)
st.image('lenna.png')
