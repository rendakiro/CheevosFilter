# CheevosFilter
CheevosFilter is a Python interface for [RALibretro](https://github.com/RetroAchievements/RALibretro/) that allows you to quickly find which games are compatible with Achievements (Cheevos).

### History
I have been a regular user of this platform since 2017, and thanks to the "challenges and achievements" it has helped me to revisit games that I had already finished and to discover new titles that would otherwise have gone unnoticed.
The problem is that on many occasions I could not find the correct ROM or the translation did not match the one on the platform. I usually solved this by "trial and error", but over time I needed something more efficient, especially when recommending a game to a friend.
I found a project that did this, Hascheevos: [https://github.com/meleu/hascheevos/](https://github.com/meleu/hascheevos/), but it included all the games registered on the platform, both with and without achievements.
Taking advantage of this idea, I created a simple Python interface that uses *RALibretro* and cross-references it with the RetroAchievements database to mark compatible ROMs with achievements.

In 2024, RetroAchievements changed the way these achievements are called. I have updated the code and generated a new version adapted to this change, requiring the use of the API_KEY (which can be obtained from your profile on the website). I have tested it on Debian and Windows 10 without problems.

### Requirements
Nothing additional to Python 3: [https://www.python.org/downloads/](https://www.python.org/downloads/) and RALibretro itself is used, which I do not include in case it is updated.

* Download the code and add **RALibretro** to the root of the folder next to `search.py`

### How it works
On the first start, it will ask for the **Username** and the **API KEY** to connect. With this, it will use the RetroAchievements names to generate the folders for the different systems.
Once the ROMs to be analyzed have been included, it will move the valid ones to **clean**, inform you which ones it has moved, and that's it.



# CheevosFilter
CheevosFilter es una interfaz en Python para [RALibretro](https://github.com/RetroAchievements/RALibretro/) con el fin de poder localizar de forma rápida que juegos son compatibles con Logros (Cheevos).

## Historia
Soy asiduo de esta plataforma desde 2017 y gracias a los "retos y logros" me ha servido para rescatar juegos que ya había terminado y a conocer nuevos títulos, que de otra forma hubieran pasado desapercibidos para mí.
El problema es que en muchas ocasiones no daba con la rom correcta o en el casi de las traducciones, no coincidía con la de la plataforma, normalmente lo solucionaba por “prueba y error”, pero con el tiempo necesitaba algo más eficaz, sobre todo cuando le recomendaba un juego a un amigo.
Encontré un proyecto que realizaba esta acción [Hascheevos](https://github.com/meleu/hascheevos/), pero traía todos los registrados en la plataforma, tanto con logros como si no.
Aprovechando esta idea, monte una interfaz simple en Python que usando el *RALibretro* y cruzando con la base de RetroAchievements, podía marcar las roms compatibles y con logros.

En este año 2024, RetroAchievements ha cambiado la forma de llamar a estos logros, he actualizado el código y he generado una nueva versión adapta a este cambio, requiriendo el uso del API_KEY (que se obtiene desde su perfil en la web), lo he probado en Debian y Windows 10 sin problemas. 

# Requerimientos
No se usa nada adicional a [Python 3](https://www.python.org/downloads/) y el Propio RALibretro, que no incluyo para por si este actualiza.

*   Descargamos el codigo y añadimos el **RALibretro** en la raiz de la carpeta junto al `search.py`

## Funcionamiento
En el primer arranque, solicitara el **Usuario** y el **API KEY** para poder conectar, con ello usando los nombres de RetroAchievements generara las carpetas de los distintos sistemas.
Una vez incluidas las roms para analizar, movera las validas a **clean**, informara de cuales ha movido y listo.

