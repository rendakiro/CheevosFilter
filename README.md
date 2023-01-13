# CheevosFilter

CheevosFilter es una interfaz en Python para [RALibretro](https://github.com/RetroAchievements/RALibretro/) con el fin de poder localizar de forma rápida que juegos son compatibles con Logros (Cheevos).

## Historia

Soy asiduo de esta plataforma desde 2017 y gracias a los "retos y logros" me ha servido para rescatar juegos que ya había terminado y a conocer nuevos títulos, que de otra forma hubieran pasado desapercibidos para mí.

El problema es que en muchas ocasiones no daba con la rom correcta o en el casi de las traducciones, no coincidía con la de la plataforma, normalmente lo solucionaba por “prueba y error”, pero con el tiempo necesitaba algo más eficaz, sobre todo cuando le recomendaba un juego a un amigo. 

Encontré un proyecto que realizaba esta acción [Hascheevos](https://github.com/meleu/hascheevos/), pero traía todos los registrados en la plataforma, tanto con logros como si no.

Aprovechando esta idea monte una interfaz simple en Python que usando el *RALibretro* y cruzando con la base de RetroAchievements, podía marcar las roms compatibles y con logros.

# Requerimientos 

No se usa nada adicional a [Python 3](https://www.python.org/downloads/) y el Propio RALibretro, que no incluyo para por si este actualiza.

- Descargamos el codigo y añadimos el  **RALibretro** en la raiz de la carpeta junto al **main.py**

## Funcionamiento

En el primer arranque, generara las carpetas donde almacenar las **Roms** y los archivos que usara para filtrar, el nombre de las carpetas coincide con los que usa **Batocera**.

Una vez incluidas las roms en sus sistemas **Recomiendo que estén sin comprimir** el sistema recorrerá las mismas **también funcionan los CUE** y añadirá las validas en la carpeta **clean**.

Es **necesaria conexión a internet** para descargar los datos de **RetroAchievements**, una vez finalizado las roms no compatibles se dejarán en la carpeta original.

Este script esta pensado **para Windows** pero en breve modificare 2 cosas para que funcione bien en **Linux**