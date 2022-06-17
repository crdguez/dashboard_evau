import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

st.title('Inicio')
st.write('Esto son pruebas')

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

df_datos.tags
st.write(df_datos.tags.str.split(',', expand=True))
#pd.concat([dat1, dat2], axis=1)
df_tags=df_datos.tags.str.split(',', expand=True)
st.write(list(pd.concat([df_tags[0], df_tags[1]], axis=0).unique()))
#pd.DataFrame(list(df_datos.tags.split(','))).set_index(0)[1]
code ="""
<iframe
  src="https://jupyterlite.github.io/demo/repl/index.html?kernel=python&toolbar=1"
  width="100%"
  height="500px"
>
</iframe>
"""

components.html(code)

