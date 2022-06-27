import streamlit as st
import pandas as pd

st.title('EVAU Ciencias')

df_datos = pd.read_csv('datos.csv',sep =';')

st.write(df_datos.enunciado)

for ej in df_datos.iterrows() :
    st.header(ej[1].bloque)
    st.subheader(ej[1].anyo + '-' + ej[1].convocatoria)
    st.image('img/'+ej[1].enunciado)


# st.image('img/caj2101.png')
