import os
import subprocess
import shutil
from listConsoles import listConsoles
listConsoles = listConsoles()

class checkRoms:
    def __init__(self):
        self.gameCheevos = list ()
        for folder in listConsoles.consoleID:
            if os.path.isdir("roms/"+folder):
                pass
            else:
                os.mkdir("roms/"+folder)

    def checkFolder(self):
        for folder in listConsoles.consoleID:
            folderFile = []
            for path in os.listdir("roms/"+folder):
                if os.path.isfile(os.path.join("roms/"+folder, path)):
                        folderFile.append(path)
            
            if len(folderFile) > 0:
                consoleID = listConsoles.consoleID[folder]
                self.readFolder(consoleID, folder, folderFile)
        
    def readFolder(self, consoleID, folder, folderFile):
        gameHash = list()
        checkFolder = list()
        
        print("Sistema con Roms: "+folder)
        for file in folderFile:
            output = subprocess.Popen(["./RAHasher", str(consoleID), "roms/"+folder+"/"+file], stdout=subprocess.PIPE).communicate()[0]
            if output.decode("utf-8").rstrip() == "":
                pass
            else:
                gameHash.append([output.decode("utf-8").rstrip(), file])
                print("Juego reconocido: "+file)

        self.checkGame(consoleID, folder, gameHash)

    def checkGame(self, consoleID, folder, gameHash):
        from readCheevos import readCheevos
        readCheevos = readCheevos(consoleID)
        listCheevos = readCheevos.listCheevos
        for game in gameHash:
            for has in listCheevos:
                if has[0] == game[0]:
                    if ".cue" in game[1]:
                        self.gestinarCue(folder, game)
                    else:
                        pass
                    self.gameCheevos.append([folder, game[1]])
                    print("Logros En: "+ game[1])

    def moveGame(self):
        if len(self.gameCheevos) == 0:
            return

        self.checkFolderClean()

        for folder, game in self.gameCheevos:
            if os.path.isdir("clean/"+folder):
                pass
            else:
                os.mkdir("clean/"+folder)

            folderOri = "roms/"+folder+"/"+game
            folderEnd = "clean/"+folder+"/"+game
            shutil.move(folderOri, folderEnd)

    def checkFolderClean(self):
        if os.path.isdir('clean'):
            pass
        else:
            os.mkdir("clean")
    
    def checkCueBin(self, folder, game):
        file = open("roms/"+folder+"/"+game[1], "r")
        with file as f:
            for line in f.readlines():
                if "FILE" in line:
                    lineData = line.split('"')
                    for console, game in self.gameCheevos:
                        duplicado = True
                        if game == lineData[1]:
                            duplicate = False
                        else:
                            pass        
                    if duplicate:
                        self.gameCheevos.append([folder, lineData[1]])
                    else:
                        pass
                else:
                    pass
