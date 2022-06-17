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
code ="""
<iframe
  src="https://jupyterlite.github.io/demo/repl/index.html?kernel=python&toolbar=1#code={
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "IPython console for SymPy 1.6.2 (Python 3.6.12-64-bit) (ground types: gmpy)\n",
      "\n",
      "These commands were executed:\n",
      ">>> from __future__ import division\n",
      ">>> from sympy import *\n",
      ">>> x, y, z, t = symbols('x y z t')\n",
      ">>> k, m, n = symbols('k m n', integer=True)\n",
      ">>> f, g, h = symbols('f g h', cls=Function)\n",
      ">>> init_printing()\n",
      "\n",
      "Documentation can be found at https://docs.sympy.org/1.6.2/\n",
      "\n"
     ]
    },
    {
     "data": {
      "text/latex": [
       "$\\displaystyle \\left( \\left[\\begin{matrix}1 & 1 & -1 & 5\\\\2 & 1 & 1 & -4\\\\-1 & 3 & -2 & 6\\end{matrix}\\right], \\  \\left[\\begin{matrix}1 & 1 & -1 & 5\\\\0 & -1 & 3 & -14\\\\0 & 0 & 9 & -45\\end{matrix}\\right], \\  \\left[\\begin{matrix}1\\\\-1\\\\-5\\end{matrix}\\right]\\right)$"
      ],
      "text/plain": [
       "⎛⎡1   1  -1  5 ⎤  ⎡1  1   -1   5 ⎤  ⎡1 ⎤⎞\n",
       "⎜⎢             ⎥  ⎢              ⎥  ⎢  ⎥⎟\n",
       "⎜⎢2   1  1   -4⎥, ⎢0  -1  3   -14⎥, ⎢-1⎥⎟\n",
       "⎜⎢             ⎥  ⎢              ⎥  ⎢  ⎥⎟\n",
       "⎝⎣-1  3  -2  6 ⎦  ⎣0  0   9   -45⎦  ⎣-5⎦⎠"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Funcion que diagonaliza y resuelve un sistema a partir de la matriz asociada\n",
    "\n",
    "from sympy import *\n",
    "init_session()\n",
    "\n",
    "def mi_gauss(M) :\n",
    "    return(M, M.LUdecomposition()[1],M[:,:-1].LUsolve(M.col(-1)))\n",
    "\n",
    "# Ejemplo\n",
    "\n",
    "M=Matrix([[1,1,-1,5],[2,1,1,-4],[-1,3,-2,6]])\n",
    "mi_gauss(M)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}"
  width="100%"
  height="500px"
>
</iframe>
"""

components.html(code)

