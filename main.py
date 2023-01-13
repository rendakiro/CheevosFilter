from recursos.generadorEntorno import generadorEntorno
from recursos.comprobarRoms import comprobarRoms

generadorEntorno = generadorEntorno()

comprobarRoms = comprobarRoms()
comprobarRoms.comprobarDirectorios()
comprobarRoms.moverJuegos()
listado = comprobarRoms.juegosCheevos

if len(listado) == 0:
    print("Los juegos no tienen logros.")

input("Presiona cualquier tecla para cerrar....")