<img width="1173" height="377" alt="Portada" src="https://github.com/user-attachments/assets/0b535160-6a92-46ca-b254-8d7053606b32" />

![Status](https://img.shields.io/badge/Status-Terminado-brightgreen) ![GitHub](https://img.shields.io/badge/GitHub-Kuchais-black?logo=github) ![Universidad Tecnológica de León](https://img.shields.io/badge/Universidad%20Tecnol%C3%B3gica%20de%20Le%C3%B3n-004B23?style=for-the-badge&logo=university&logoColor=white) ![Python](https://img.shields.io/badge/Python-3.8.0-3776AB?style=for-the-badge&logo=python&logoColor=white)

# Índice

- [Índice](#índice)
- [Descripción del proyecto](#descripción-del-proyecto)
- [Funcionalidades del proyecto](#funcionalidades-del-proyecto)
- [Acceso al proyecto](#acceso-al-proyecto)
- [Tecnologías utilizadas](#tecnologías-utilizadas)
- [Desarrolladores del Proyecto](#desarrolladores-del-proyecto)
- [Conclusión](#conclusión)
- [Notas](#notas)

# Descripción del proyecto

Este proyecto consta del desarrollo de una mano robotica controlada por visión artificial, la cual tiene una conexión con un microcontrolador ARDUINO el cual se encarga de recibir las señales e interpretarlas para realizar el movimiento en nuestra mano robotica

# Funcionalidades del proyecto

- `Funcionalidad 1`: Detección en tiempo real de nuestras propias manos
- `Funcionalidad 2`: Movimiento en tiempo real sobre nuestra mano robotica detectando el movimiento de nuestras manos

# Acceso al proyecto

📁 Acceso al proyecto
Para este proyecto se utilizo la version de Python 3.8.0
Para pode probarlo es necesario contar con las siguientes librerias de python instaladas (se recomienda hacer un entorno virtual para su instalación)
- Paso 1: Descarga el repositorio completo el cual incluye el codigo de arduino y python
- Paso 2: Abre el codigo de python e inserta las siguientes instrucciones en la terminal.
1. Primero se crea el entorno virtual con: `python -m venv venv`
2. Despues se activa el entorno virtual con: `venv\Scripts\activate`
3. Despues se instalan las librerias con sus respectivas versiones indicadas aqui mismo: `pip install opencv-python==4.8.1.78 cvzone==1.5.6 mediapipe==0.10.11 pyserial==3.5`

🛠️ Abre y ejecuta el proyecto
Para probarlo solo es necesario ejecutar el codigo de Python y el codigo de arduino conectado a los respectivos servomotores y los servomotores se moveran dependiendo del dedo que se levante o se agache.

Para que funcione correctamente en cualquier dispositivo hay que modificar el codigo teniendo las siguientes consideraciones:
- Entorno virtual activado: El entorno virtual tiene la funcion de no instalar las librerias en el proyecto como tal, sino en un entorno que se activa y se desactiva segun lo quieras usar o no, esto se realiza para evitar conflictos al momento de ejecutar el codigo.
- El puerto COM: El puerto COM cambia dependiendo del microntrolados y computadora donde lo conectes, por lo que tienes que verificar en que puerto esta conectado y cambiarlo en el codigo.
- Tambien para poder utilizar alguna otra camara, en la linea de codigo `cap = cv2.VideoCapture(0)` cambiamos el argumento "0", por 1 o 2, y probar si es la camara que queremos utilizar. 


# Tecnologías utilizadas

- **OpenCV**
- **Mediapipe**
- **Python**
- **Arduino**
- **Serial**

# Desarrolladores del proyecto
**Juan Benjamin Tovar Villa**

# Conclusión
Este proyecto impulsa la robotica y la vision artificial para soluciones a problematicas en el área tecnologica. 

#Notas
-Recomiendo personalmente eliminar la carpeta "venv" encargada del entorno virtual para el codigo de python y crearlo de forma independiente para evitar conflictos
-Tambien es posible probar los codigos de forma individual. Para poder ver si esta funcionando correctamente el codigo de python, debajo del arreglo de datos que nos indica cuales dedos estan levantados podemos agregar la siguiente linea de codigo `print(datos)`. Esto hara que en nuestra terminal se visualice el arreglo de los dedos que levantamos al correr el programa. Para el caso del codigo arduino, podemos abrir el monitor serial e ingresar los valores individualmente y ver si los servomotrores responden correctamente. Por ejemplo: "00000" (ningun dedo levantado), "11111" (todos los dedos levantados).
