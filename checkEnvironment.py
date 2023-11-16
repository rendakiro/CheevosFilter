import os

class checkEnvironment:
    def __init__(self) -> None:
        if os.path.exists("RAHasher"):
            pass
        else:
            print("es neceario RAHasher")
            exit()
        
        if os.path.isdir('hasfiles'):
            pass
        else:
            os.mkdir("hasfiles")
        if os.path.isdir('roms'):
            pass
        else:
            self.generatorFolder()
    
    def generatorFolder(self):
        os.mkdir("roms")
        from listConsoles import listConsoles
        listConsoles = listConsoles()
        for carpeta in listConsoles.consoleID:
            os.mkdir("roms/"+carpeta)

        print("Carpetas para ROMS generadas.")
        input("Presiona cualquier tecla para cerrar....")
        exit()