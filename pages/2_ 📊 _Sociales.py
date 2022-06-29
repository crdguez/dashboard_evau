import streamlit as st
import pandas as pd
from funciones import filtrar_y_mostrar

st.title('EVAU Sociales')
st.sidebar.title('EVAU Sociales')

df_datos = pd.read_csv('datos.csv',delimiter =';')
slice = df_datos[df_datos.itinerario == 'sociales']


filtrar_y_mostrar(slice)
