import yaml
import time
import os
import glob
from src.profil_loader import *
from src.parameters import *
from src.export import *
from src.utils import *
from src.map_object import MapObject
from src.generators.map_generator import MapGenerator
from src.generators.map_generator_heightmap import MapGeneratorHeightmap

def main():
    print("\tMap generation is starting...")
    start_time = time.time()
    os.makedirs("output", exist_ok=True)
    profileList = glob.glob('presets/profil*.yaml')
    profileList = list(i for i in profileList)  # [:-3] pour enlever .py
    profileList.insert(0, "Auto")
    profileList.insert(1, "Manual")
    
    for i in range(len(profileList)):
        print(i + 1, " : ", profileList[i])
    profil_number = int(input("Profil number : "))
    if profil_number > len(profileList):
        print("Profil unvalid")
        exit()
    includName = profileList[profil_number - 1]

    params = {}

    if (includName == "Auto"):
        params = auto_profil()
    elif (includName == "Manual"):
        params = manual_profil()  
    else:
        params = load_profil(includName)

    length = params["length"]
    height = params["height"]
    if (params.get('generator','') == "heightmap"):
        generator = MapGeneratorHeightmap()
    else:
        generator = MapGenerator()
    map_object = MapObject(length, height, generator, params.get('generate_resources',True))
    if (params['mode'] in ["generate", "write"]):
        map_object.generate_map()
        if (params['mode'] == 'write'):
            write_map(map_object, params['file_map'])
    elif (params['mode'] in ["read", "load"]):
        raise NotImplementedError
        # map_object = liremap(params['file_map'])
    else:
        print("Mode unvalid")
        exit()
    if params['print_map']:
        print_map(map_object)
        print_resources_map(map_object)
    if (params['export_format'] in ["img"," image"]):
        export_img(map_object, params['export_file'])
    elif (params['export_format'] in ["html", "html"]):
        export_html(map_object, params['export_file'])
    print(f"Map exported in {params['export_file']}")
    print(f"\tMap generation is finished (in {(time.time() - start_time):.2f}s)")

if __name__ == "__main__":
    main()