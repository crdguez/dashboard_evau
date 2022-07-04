import streamlit as st
import pandas as pd
# import streamlit.components.v1 as components

#st.set_page_config(page_title='Matemáticas EVAU', page_icon=':page_facing_up:', layout="wide", initial_sidebar_state="expanded", menu_items=None)
st.set_page_config(
    page_title='Laboratorio de funciones',
    page_icon="🧊",
    layout='wide')


st.title('Exámenes de Matemáticas - EVAU :page_facing_up:')
st.write(':arrow_left: A la izquierda tienes el menú.')

st.info(""":point_right: Esta aplicación no es más que un **filtro** de los ejercicios de **matemáticas** que aparecen en [https://matematicasentumundo.es/PAU/PAU.htm](https://matematicasentumundo.es/PAU/PAU.htm)
      correspondientes a la **EVAU de la Universidad de Zaragoza**.""")
st.write("""""")
      
st.image('portada.png', caption='Imagen de la web Matemáticas en tu Mundo') 

st.write('Muchas gracias por vuestro trabajo, **José María y Julio**.')

st.subheader('Licencia')
st.markdown('- Autor: *Carlos Rodríguez*  \n -   :exclamation: Tienes el código en [este repositorio de *Github*](https://github.com/crdguez/dashboard_evau) \
            \n - Tanto el código como la aplicación se publican con **licencia libre**')


# #df_datos = pd.read_csv('datos.csv',sep =';',encoding='latin-1')
# df_datos = pd.read_csv('datos.csv',sep =';')

# st.dataframe(df_datos)
# st.write(df_datos.enunciado)

# option = st.sidebar.selectbox(
#      'Bloque',
#      df_datos.bloque.unique())

# st.write('Has seleccionado:', option)
# #st.image('lenna.png', width = 150)
# #st.image('lenna.png')

# df_datos.tags
# st.write(df_datos.tags.str.split(',', expand=True))
# #pd.concat([dat1, dat2], axis=1)
# df_tags=df_datos.tags.str.split(',', expand=True)
# st.write(list(pd.concat([df_tags[0], df_tags[1]], axis=0).unique()))

# # lista de los diferentes tags

# st.write(list(set([x for xs in df_datos.tags.apply(lambda x: x.split(',')) for x in xs])))

# # Incluir una terminal de python para hacer pruebas

# # code ="""
# # <iframe
# #   src="https://jupyterlite.github.io/demo/repl/index.html?kernel=python&toolbar=1"
# #   width="100%"
# #   height="500px"
# # >
# # </iframe>
# # """
# # code ="""
# # <iframe
# #   src="https://jupyterlite.github.io/demo/repl/index.html?kernel=python&toolbar=1&code=from sympy import *
# #  "
# #   width="100%"
# #   height="500px"
# # >
# # </iframe>
# # """

# # components.html(code)


