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

# Filtro bloque
lb=list(slice.bloque.sort_values().unique())
lb.insert(0,'Todos')
bl = st.sidebar.selectbox('Bloque:',lb,0,format_func=lambda x: str(x).capitalize())
slice = slice if bl == 'Todos' else slice[slice.bloque == bl]

# Filtro tag
lt=list(set([x for xs in df_datos.tags.apply(lambda x: x.split(',')) for x in xs]))
lt.insert(0,'Todos')
tg = st.sidebar.selectbox('Tags:',lt,0,format_func=lambda x: str(x).capitalize())
slice = slice if tg == 'Todos' else slice[slice.tags.str.contains(tg)]



for ej in slice.iterrows() :
    st.subheader(ej[1].bloque.capitalize()+'-'+str(ej[1].convocatoria).capitalize() + '-' + str(ej[1].anyo))
#     st.subheader(str(ej[1].anyo) + '-' + str(ej[1].convocatoria).capitalize())
#     st.subheader(ej[1].anyo)
    st.image('img/'+ej[1].enunciado)
    with st.expander("Ver solución"):
            st.image('img/'+ej[1].solucion)



