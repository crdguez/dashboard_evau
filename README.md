# Dashboard evau (En contrucción)

App con [Streamlit](https://streamlit.io/) para ver ejercicios de Evau. Está desplegado en [https://crdguez-dashboard-evau-0--inicio-mo2poi.streamlitapp.com/](https://crdguez-dashboard-evau-0--inicio-mo2poi.streamlitapp.com/).

# Uso con Docker

### Crear la imagen a partir del Dockefile

Si no tenemos la imagen en local:

```
sudo docker build -t crdguez/mi_streamlit:v2 .
```



### Lanzando un contendor docker con Streamlit y la aplicacion *main.py*

El fichero principal es: 0_🏠_Inicio.py. Creamos el docker con el siguiente comando:

```
docker run -it -p 8501:8501 --name evau -v $PWD:/app crdguez/mi_streamlit:v2 0_🏠_Inicio.py

```

Una vez creado podemos lanzarlo yendo desde un terminal:


```
docker start evau

```
Y en el navegador

Network URL: http://172.17.0.2:8501
External URL: http://85.60.254.2:8501


### Actualizar streamlit en el contenedor

En mi caso, la imagen mi_streamlit era antigua y no tenía la última versión así que he entrado en el docker y he actualizado:

```
docker exec -it -u 0 evau /bin/bash
```
Y una vez en la terminal:
```
pip install --upgrade streamlit
```


