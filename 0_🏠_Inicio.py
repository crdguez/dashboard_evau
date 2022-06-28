import streamlit as st
import pandas as pd
# import streamlit.components.v1 as components


st.title('Ejercicios de Matemáticas de la EVAU ')
st.write(':arrow_left: A la izquierda tienes el menú')

#df_datos = pd.read_csv('datos.csv',sep =';',encoding='latin-1')
df_datos = pd.read_csv('datos.csv',sep =';')

st.dataframe(df_datos)
st.write(df_datos.enunciado)

option = st.sidebar.selectbox(
     'Bloque',
     df_datos.bloque.unique())

st.write('Has seleccionado:', option)
#st.image('lenna.png', width = 150)
#st.image('lenna.png')

df_datos.tags
st.write(df_datos.tags.str.split(',', expand=True))
#pd.concat([dat1, dat2], axis=1)
df_tags=df_datos.tags.str.split(',', expand=True)
st.write(list(pd.concat([df_tags[0], df_tags[1]], axis=0).unique()))

# lista de los diferentes tags

st.write(list(set([x for xs in df_datos.tags.apply(lambda x: x.split(',')) for x in xs])))

# Incluir una terminal de python para hacer pruebas

# code ="""
# <iframe
#   src="https://jupyterlite.github.io/demo/repl/index.html?kernel=python&toolbar=1"
#   width="100%"
#   height="500px"
# >
# </iframe>
# """
# code ="""
# <iframe
#   src="https://jupyterlite.github.io/demo/repl/index.html?kernel=python&toolbar=1&code=from sympy import *
#  "
#   width="100%"
#   height="500px"
# >
# </iframe>
# """

# components.html(code)


