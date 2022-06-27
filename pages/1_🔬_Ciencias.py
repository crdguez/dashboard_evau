import streamlit as st
import pandas as pd

st.title('EVAU Ciencias')

df_datos = pd.read_csv('datos.csv',sep =';')

# st.write(df_datos.enunciado)

for ej in df_datos.iterrows() :
    st.header(ej[1].bloque.capitalize()+str(ej[1].convocatoria).capitalize() + '-' + str(ej[1].anyo))
    st.subheader(str(ej[1].anyo) + '-' + str(ej[1].convocatoria).capitalize())
#     st.subheader(ej[1].anyo)
    st.image('img/'+ej[1].enunciado)
    with st.expander("Ver solución"):
            st.image('img/'+ej[1].solucion)



