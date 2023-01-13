import os
import subprocess
import shutil

class comprobarRoms:

    def __init__(self):
        from recursos.listadosEstaticos import listadosEstaticos
        listadosEstaticos = listadosEstaticos()
        self.juegosCheevos = list ()
        for carpeta in listadosEstaticos.consoleID:
            if os.path.isdir("roms/"+carpeta):
                pass
            else:
                os.mkdir("roms/"+carpeta)

    def comprobarDirectorios(self):
        from recursos.listadosEstaticos import listadosEstaticos
        listadosEstaticos = listadosEstaticos()
        for carpeta in listadosEstaticos.consoleID:
            ficherosDirectorio = []
            for path in os.listdir("roms/"+carpeta):
                if os.path.isfile(os.path.join("roms/"+carpeta, path)):
                        ficherosDirectorio.append(path)
            
            if len(ficherosDirectorio) > 0:
                consoleID = listadosEstaticos.consoleID[carpeta]
                self.leerDirectorio(consoleID, carpeta, ficherosDirectorio)  

    def leerDirectorio(self, consoleID, carpeta, ficherosDirectorio):
        juegoHas = list()
        ListadoComprobado = list()
        
        print("Sistema con Roms: "+carpeta)
        for file in ficherosDirectorio:
            output = subprocess.Popen(["RAHasher.exe", str(consoleID), "roms/"+carpeta+"/"+file], stdout=subprocess.PIPE).communicate()[0]
            if output.decode("utf-8").rstrip() == "":
                pass
            else:
                juegoHas.append([output.decode("utf-8").rstrip(), file])
                print("Juego reconocido: "+file)

        self.comprobarJuegos(consoleID, carpeta, juegoHas)

    def comprobarJuegos(self, consoleID, carpeta, juegoHas):
        from recursos.leerCheevos import leerCheevos
        leerCheevos = leerCheevos(consoleID)
        listadoCheevos = leerCheevos.listadoCheevos
        for juego in juegoHas:
            for has in listadoCheevos:
                if has[0] == juego[0]:
                    if ".cue" in juego[1]:
                        self.gestinarCue(carpeta, juego)
                    else:
                        pass
                    self.juegosCheevos.append([carpeta, juego[1]])
                    print("Logros En: "+ juego[1])

    def moverJuegos(self):
        if len(self.juegosCheevos) == 0:
            return

        self.comprobarDirectorioClean()

        for directorio, juego in self.juegosCheevos:
            if os.path.isdir("clean/"+directorio):
                pass
            else:
                os.mkdir("clean/"+directorio)

            dirOrigen = "roms/"+directorio+"/"+juego
            dirFinal = "clean/"+directorio+"/"+juego
            shutil.move(dirOrigen, dirFinal)

    def comprobarDirectorioClean(self):
        if os.path.isdir('clean'):
            pass
        else:
            os.mkdir("clean")

    def gestinarCue(self, carpeta, juego):
        file = open("roms/"+carpeta+"/"+juego[1], "r")
        with file as f:
            for line in f.readlines():
                if "FILE" in line:
                    lineData = line.split('"')
                    for sistema, juego in self.juegosCheevos:
                        duplicado = True
                        if juego == lineData[1]:
                            duplicado = False
                        else:
                            pass        
                    if duplicado:
                        self.juegosCheevos.append([carpeta, lineData[1]])
                    else:
                        pass
                else:
                    pass