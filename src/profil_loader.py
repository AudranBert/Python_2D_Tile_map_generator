import yaml
from .questions import *

def load_profil(profil_file):
    # load profile.yaml
    with open(profil_file, 'r') as f:
        profil = yaml.safe_load(f)
    return profil

def auto_profil():
    profil = {
        "length": 100,
        "height": 80,
        "print_map": False,
        "mode": "generate",
        "generate_resources": False,
        "generator": "heightmap",
        "file_map": None,
        "export_format": "img",
        "export_file": "export.png"
    }
    return profil




# lire un fichier
def read_map_in_file(nomfic):
    fichier = open(nomfic, "r")
    longueur = int(fichier.readline())
    hauteur = int(fichier.readline())
    fichier.close()
    return longueur, hauteur

def manual_profil():
    V = ["w", "r", "n", "write", "read", "nothing"]
    fic = quest_responses("Read, write or northing", V)
    if (fic == 'w' or fic == 'write'):
        nomfic = quest("Save file name for the map (.txt)")
    if (fic == 'n' or fic == 'w' or fic == 'nothing' or fic == 'write'):
        length, height = map_size()
    else:
        nomfic = quest("File to read (.txt)")
        length, height = read_map_in_file(nomfic)
    print_map = yesno("Print map? y/n ")
    generator = quest_responses("Generator used for generating map", ["v0","heightmap"])
    generate_resources = yesno("Generate resources? y/n ")
    export_format = quest_responses("Export format (no, html, img)", ["no", "html", "img"])
    if (export_format == 'html' or export_format == 'img'):
        export_file = quest("Export file name (.html)")
        if export_format == 'img':
            export_file = export_file + ".png"
        else:
            export_file = export_file + ".html"
    # make a dict
    profil = {
        "length": length,
        "height": height,
        "print_map": print_map,
        "mode": "generate",
        "generate_resources": generate_resources,
        "generator": generator,
        "file_map": None,
        "export_format": export_format,
        "export_file": export_file,
    }
    return profil