import streamlit as st

def filtrar_y_mostrar(slice):
    # Filtro año
    l=list(slice.anyo.sort_values().unique())
    l.insert(0,'Todos')
    s = st.sidebar.selectbox('Año:',l,0,format_func=lambda x: str(x).capitalize())
    # st.sidebar.write(s)
    slice = slice if s == 'Todos' else slice[slice.anyo == s]

    # Filtro convocatoria
    l=list(slice.convocatoria.sort_values().unique())
    l.insert(0,'Todas')
    s = st.sidebar.selectbox('Convocatoria:',l,0,format_func=lambda x: str(x).capitalize())
    # st.sidebar.write(s)
    slice = slice if s == 'Todas' else slice[slice.convocatoria == s]

    # Filtro bloque
    lb=list(slice.bloque.sort_values().unique())
    lb.insert(0,'Todos')
    bl = st.sidebar.selectbox('Bloque:',lb,0,format_func=lambda x: str(x).capitalize())
    slice = slice if bl == 'Todos' else slice[slice.bloque == bl]

    # Filtro tag
    lt=list(set([x for xs in slice.tags.apply(lambda x: x.split(',')) for x in xs]))
    lt.insert(0,'Todos')
    tg = st.sidebar.selectbox('Contenido:',lt,0,format_func=lambda x: str(x).capitalize())
    slice = slice if tg == 'Todos' else slice[slice.tags.str.contains(tg)]


    # Mostramos los ejercicios
    for ej in slice.iterrows() :
        st.subheader(ej[1].bloque.capitalize()+'-'+str(ej[1].convocatoria).capitalize() + '-' + str(ej[1].anyo))
        st.image('img/'+ej[1].enunciado)
        with st.expander("Ver solución"):
                st.image('img/'+ej[1].solucion)
