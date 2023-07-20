import yaml
import time
import os
import glob
from profil_loader import *
from parameters import *
from export import *
from utils import *
from map_object import MapObject

def main():
    print("\tProgramme de generation de map aleatoire par Audran")
    start_time = time.time()
    os.makedirs("output", exist_ok=True)
    profileList = glob.glob('presets/profil*.yaml')
    profileList = list(i for i in profileList)  # [:-3] pour enlever .py
    profileList.insert(0, "Auto")
    profileList.insert(1, "Manual")
    
    for i in range(len(profileList)):
        print(i + 1, " : ", profileList[i])
    includName = profileList[int(input("profile number : ")) - 1]

    params = {}

    if (includName == "Auto"):
        params = auto_profil()
    elif (includName == "Manual"):
        params = manual_profil()  
    else:
        params = load_profil(includName)

    longueur = params["longueur"]
    hauteur = params["hauteur"]

    map_object = MapObject(longueur, hauteur)
    if (params['mode'] in ["generate", "write"]):
        map_object.creationmap()
        if (params['mode'] == 'write'):
            ecriremap(map_object, params['file_map'])
    elif (params['mode'] in ["read", "load"]):
        raise NotImplementedError
        # map_object = liremap(params['file_map'])
    else:
        print("Mode unvalid")
        exit()
    if params['print_map']:
        affichagetm(map_object)
        affichagetr(map_object)
    if (params['export_format'] in ["img"," image"]):
        export_img(map_object, params['export_file'])
    elif (params['export_format'] in ["html", "html"]):
        export_html(map_object, params['export_file'])
    print("Temps total d execution : %s secondes ---" % (time.time() - start_time))
    print("\tGeneration termine !")

if __name__ == "__main__":
    main()