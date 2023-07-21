import yaml
from .questions import *

def load_profil(profil_file):
    # load profile.yaml
    with open(profil_file, 'r') as f:
        profil = yaml.safe_load(f)
    return profil

def auto_profil():
    profil = {
        "longueur": 20,
        "hauteur": 10,
        "aff": "non",
        "html": "oui",
        "fic": "rien",
        "nomhtml": "export.html"
    }
    return profil




# lire un fichier
def lirecaracmap(nomfic):
    fichier = open(nomfic, "r")
    longueur = int(fichier.readline())
    hauteur = int(fichier.readline())
    fichier.close()
    return longueur, hauteur

def manual_profil():
    V = ["e", "l", "r", "ecriture", "lecture", "rien"]
    fic = quest_responses("Lecture,ecriture ou rien", V)
    if (fic == 'e' or fic == 'ecriture'):
        nomfic = quest("Nom du fichier de destination (.txt)")
    if (fic == 'r' or fic == 'e' or fic == 'rien' or fic == 'ecrire' or fic == 'ecriture'):
        longueur, hauteur = taille()
    else:
        nomfic = quest("Nom du fichier de lecture (.txt)")
        longueur, hauteur = lirecaracmap(nomfic)
    aff = yesno("Affichage? o/n ")
    html = yesno("Export Html? o/n")
    if (html == 'o' or html == 'oui'):
        nomhtml = quest("Nom du fichier de l export (.html)")
        nomhtml = nomhtml + ".html"
    # make a dict
    profile = {
        "longueur": longueur,
        "hauteur": hauteur,
        "aff": aff,
        "html": html,
        "fic": fic,
        "nomhtml": nomhtml
    }
    return profile