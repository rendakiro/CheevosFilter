import json
import os
import calendar
import time
from urllib.request import urlopen

class leerCheevos:

    def __init__(self, systemId):
        self.listadoCheevos = []
        self.systemId = str(systemId)

        if os.path.exists("hasfiles/"+self.systemId+".json"):
            gmtActual = time.gmtime()
            tiempo1semana = calendar.timegm(gmtActual)-604800
            if int(os.path.getmtime("hasfiles/"+self.systemId+".json")) < tiempo1semana:
                os.remove("hasfiles/"+self.systemId+".json")
                self.leerCheevosOnline()
            else:
                return self.leerCheevosOffline()
        else:
            self.leerCheevosOnline()

    def leerCheevosOnline(self):
        responseHashlibrary = urlopen("https://retroachievements.org/dorequest.php?r=hashlibrary&c="+self.systemId)
        responseAllprogress = urlopen("https://retroachievements.org/dorequest.php?r=allprogress&c="+self.systemId)

        dataHashlibrary = json.load(responseHashlibrary)
        dataAllprogress = json.load(responseAllprogress)

        cheevosHas = list()

        for keyAllprogressin in dataAllprogress['Response']:
            for keyHashlibrary in dataHashlibrary['MD5List']:
                valueHashlibrary = dataHashlibrary['MD5List'][keyHashlibrary]
                if int(keyAllprogressin) == valueHashlibrary:
                    cheevosHas.append([keyHashlibrary, valueHashlibrary])

        with open("hasfiles/"+self.systemId+".json", "w") as file:
            json.dump(cheevosHas, file)

        self.listadoCheevos = cheevosHas

    def leerCheevosOffline(self):
        fileHashlibrary = open("hasfiles/"+self.systemId+".json")
        dataHashlibrary = json.load(fileHashlibrary)
        
        fileHashlibrary.close()

        self.listadoCheevos = dataHashlibrary