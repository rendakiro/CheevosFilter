import json
import os
from datetime import datetime, timedelta
import platform
import urllib.request

def leer_json_desde_url(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            return data
    except Exception as e:
        print(f"Error al leer el JSON desde la URL: {e}")
        exit(0)

def almacenar_json(data, filename):
    with open("hash/"+filename+".json", "w") as file:
        json.dump(data, file)
def comprobar_hashfile(filename):
    filename = "hash/"+filename+".json"
    if os.path.exists(filename):
        creation_time = os.path.getctime(filename)
        if os.path.exists(filename):
            creation_time = os.path.getctime(filename)
            creation_date = datetime.fromtimestamp(creation_time)
            current_date = datetime.now()
            one_month_ago = current_date - timedelta(days=30)            
            if creation_date < one_month_ago:
                return False
    else:
        return False
    return True

def descargar_console_list(user, api):
    url = "https://retroachievements.org/API/API_GetConsoleIDs.php?z="+user+"&y="+api
    almacenar_json(leer_json_desde_url(url), "Consoles")

def descargar_console_hashes(user, api, id):
    url = "https://retroachievements.org/API/API_GetGameList.php?z="+user+"&y="+api+"&i="+id+"&f=1&h=1"
    almacenar_json(leer_json_desde_url(url), id)

def generar_carpetas(user, api):
    if not os.path.exists("hash"):
        os.makedirs("hash")
    if not os.path.exists("clean"):
        os.makedirs("clean")
    if not os.path.exists("roms"):
        os.makedirs("roms")
        data_id = comprobar_hashfile("Consoles")
        if not data_id:
            descargar_console_list(usuario, apikey)
        with open("hash/Consoles.json", "r") as file:
            data = json.load(file)
            names = [item["Name"] for item in data]
            for name in names:
                name_parts = name.split("/")
                os.makedirs("roms/"+name_parts[0])

def obtener_id_console(nombre):
    with open("hash/Consoles.json", "r") as file:
        data = json.load(file)
    if (nombre == 'NES'):
        nombre = 'NES/Famicom'
    if (nombre == 'SNES'):
        nombre = 'SNES/Super Famicom'
    name_search = [item for item in data if nombre in item["Name"]]
    for search in name_search:
        return search["ID"]
    return None

def consultar_hashes(filename):
    filename = "hash/"+filename+".json"
    with open(filename, "r") as file:
        data = json.load(file)
    hashes = [item["Hashes"] for item in data]
    hashes = [hash for sublist in hashes for hash in sublist]
    return hashes

if not os.path.exists("params"):
    usuario = input("Ingrese el nombre de USER: ")
    apikey = input("Ingrese la clave de API: ")
    with open("params", "w") as file:
        file.write(f"user={usuario}\n")
        file.write(f"apikey={apikey}\n")
else:
    with open("params", "r") as file:
        params = file.readlines()
        usuario = params[0].split("=")[1].strip()
        apikey = params[1].split("=")[1].strip()

generar_carpetas(usuario, apikey)

roms_folders = os.listdir("roms")
for folder in roms_folders:
    folder_path = os.path.join("roms", folder)
    if os.path.isdir(folder_path):
        files = os.listdir(folder_path)
    if len(files) > 0:
        id = obtener_id_console(folder)
        data_id = comprobar_hashfile(str(id))
        if not data_id:
            descargar_console_hashes(usuario, apikey, str(id))
        for file in files:
            if platform.system() == "Windows":
                output = os.popen("RAHasher.exe "+str(id)+' "roms/'+folder+'/'+file+'"').read().strip()
            elif platform.system() == "Linux":
                output = os.popen("./RAHasher "+str(id)+' "roms/'+folder+'/'+file+'"').read().strip()
            hashes = consultar_hashes(str(id))

            if output in hashes:
                clean_directory = "clean/"+folder
                if not os.path.exists("clean/"+folder):
                    os.makedirs(clean_directory)
                os.rename("roms/"+folder+'/'+file, "clean/"+folder+'/'+file)
                print(f"The file {file} have Cheevos")
input("Press any key to continue...")                
exit(0)