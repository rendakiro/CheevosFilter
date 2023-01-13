import os

class generadorEntorno:
    def __init__(self):
        if os.path.exists("RAHasher.exe"):
            pass
        else:
            print("es neceario RAHasher.exe")
            exit()

        if os.path.isdir('hasfiles'):
            pass
        else:
            os.mkdir("hasfiles")
        if os.path.isdir('roms'):
            pass
        else:
            self.generarCarpetasRoms()
    
    def generarCarpetasRoms(self):
        os.mkdir("roms")
        from recursos.listadosEstaticos import listadosEstaticos
        listadosEstaticos = listadosEstaticos()
        for carpeta in listadosEstaticos.consoleID:
            os.mkdir("roms/"+carpeta)

        print("Carpetas para ROMS generadas.")
        input("Presiona cualquier tecla para cerrar....")
        exit()