from checkEnvironment import checkEnvironment
from checkRoms import checkRoms

checkEnvironment = checkEnvironment()

checkRoms = checkRoms()
checkRoms.checkFolder()
checkRoms.moveGame()

listFinal = checkRoms.gameCheevos

if len(listFinal) == 0:
    print("Los juegos no tienen logros.")

input("Presiona cualquier tecla para cerrar....")