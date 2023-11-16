import json
import os
import calendar
import time
from urllib.request import Request, urlopen

class readCheevos:
    def __init__(self, systemId):
        self.listCheevos = []
        self.systemId = str(systemId)

        if os.path.exists("hasfiles/"+self.systemId+".json"):
            gmtActual = time.gmtime()
            tiempo1semana = calendar.timegm(gmtActual)-604800
            if int(os.path.getmtime("hasfiles/"+self.systemId+".json")) < tiempo1semana:
                os.remove("hasfiles/"+self.systemId+".json")
                self.readOnlineCheevosList()
            else:
                return self.readOffilneCheevos()
        else:
            self.readOnlineCheevosList()
    
    def readOnlineCheevosList(self):
        requestHashlibrary = Request("https://retroachievements.org/dorequest.php?r=hashlibrary&c="+self.systemId, headers={"User-Agent": "Mozilla/5.0"})
        webpageHashlibrary = urlopen(requestHashlibrary).read().decode('utf-8')
        dataHashlibrary = json.loads(webpageHashlibrary)

        requestAllprogress = Request("https://retroachievements.org/dorequest.php?r=officialgameslist&c="+self.systemId, headers={"User-Agent": "Mozilla/5.0"})
        webpageAllprogress = urlopen(requestAllprogress).read().decode('utf-8')
        dataAllprogress = json.loads(webpageAllprogress)

        cheevosHas = list()

        for keyAllprogressin in dataAllprogress['Response']:
            for keyHashlibrary in dataHashlibrary['MD5List']:
                valueHashlibrary = dataHashlibrary['MD5List'][keyHashlibrary]
                if int(keyAllprogressin) == valueHashlibrary:
                    cheevosHas.append([keyHashlibrary, valueHashlibrary, dataAllprogress['Response'][keyAllprogressin]])

        with open("hasfiles/"+self.systemId+".json", "w") as file:
            json.dump(cheevosHas, file)

        self.listCheevos = cheevosHas
    
    def readOffilneCheevos(self):
        fileHashlibrary = open("hasfiles/"+self.systemId+".json")
        dataHashlibrary = json.load(fileHashlibrary)
        
        fileHashlibrary.close()

        self.listCheevos = dataHashlibrary
