# los entornos virtuales se utilizan porque aveces se desarrollan aplicaciones que
# necesitan diferentes reqquerimientos, y con elfin de que estos no entren en conflicto se crea un entorno virtual
# un entorno virtual es un directorio con la instalación de una versión de python

#creación

# pyvenv.pyvenv normalmente instalara la versión mas reciente de python que tengas

# define la carpeta donde quierse crearlo

# ejecuta python3 -m venv tutorial-env

# -> eso creara la carpeta tutorial-env si no existe y tambien creara la subcarpetas con una copia de python y sus librerias

# activación

# source tutorial-env/bin/activate -> cambiara el prompt para mostrarte que ya esta activado


# Paquetes pip

# este tiene varios subcomandos -search-install-uninstall-freeze,etc 

# -> pip install novas  o  con un requerimiento especifico pip install requests==2.6.0