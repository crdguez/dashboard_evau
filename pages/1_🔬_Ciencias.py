import streamlit as st
import pandas as pd

st.title('EVAU Ciencias')
st.sidebar.title('EVAU Ciencias')

# Filtro Temporada
# lt=list(slice.Temporada.sort_values().unique())
# lt.insert(0,'Todas')
# tm = st.sidebar.selectbox('Temporada:',lt,1)
# slice = slice if tm == 'Todas' else slice[slice.Temporada == tm]

# df_datos = pd.read_csv('datos.csv',sep =';')
df_datos = pd.read_csv('datos.csv',delimiter =';')

slice = df_datos[df_datos.itinerario == 'ciencias']

# st.write(df_datos.enunciado)

for ej in alice.iterrows() :
    st.subheader(ej[1].bloque.capitalize()+'-'+str(ej[1].convocatoria).capitalize() + '-' + str(ej[1].anyo))
#     st.subheader(str(ej[1].anyo) + '-' + str(ej[1].convocatoria).capitalize())
#     st.subheader(ej[1].anyo)
    st.image('img/'+ej[1].enunciado)
    with st.expander("Ver solución"):
            st.image('img/'+ej[1].solucion)



