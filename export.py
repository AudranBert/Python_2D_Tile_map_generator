from parameters import *
import time
import os
from map_object import MapObject

def export_html(map_object, filename):
    export_time = time.time()
    if filename.endswith(".html"):
        filename = filename
    else:
        filename = filename + ".html"
    with open(os.path.join("output",filename), 'w') as fichier:
        fichier.write("<!doctype html>\n<html>\n<head>\n<style>\n .td\n { width:40px; height:40px;}\n")
        # couleurs des cases en fonction du biome/type de terrain :
        for i in range(len(BiomeColors)):
            fichier.write('.d' + str(i) + '\n{background-color:' + BiomeColors[i] + ';}\n')
        # couleurs de texte en fonction des ressources:
        for i in range(len(ResColors)):
            fichier.write('.R' + str(i) + '\n{color:' + ResColors[i] + ';}\n')
        fichier.write('</style>\n<meta charset="utf-8">\n</head>\n<body>\n<table border="0">\n')
        ligne = 0
        # ligne_time=time.time()
        for i in range(0, map_object.hauteur):
            ligne = ligne + 1
            fichier.write("			<tr>\n")
            for j in range(0, map_object.longueur):
                if map_object.generate_resources:
                    fichier.write('<td class="d' + str(map_object.map[i][j]) + '">' + "<pre class=R" + str(map_object.mapr[i][j]) + " > " + str(
                        map_object.mapr[i][j]) + " </pre>" + "</td>\n")
                else:
                    fichier.write('<td class="d' + str(map_object.map[i][j]) + '">' + "</td>\n")
            fichier.write("			</tr>\n")
            modul = ligne % 50
            if modul == 0:
                print("Export ligne : ", ligne)
                # print("Temps d execution : %s secondes ---" % (time.time() - ligne_time))
                # ligne_time=time.time()
        fichier.write("		</table>\n" + "	</body>\n" + "</html>")
    print("Duree l'export HTML : %s secondes ---" % (time.time() - export_time))

def export_img(map_object, filename):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        filename = filename
    else:
        filename = filename + ".png"
    export_time = time.time()
    # export image
    from PIL import Image, ImageDraw
    img = Image.new('RGB', (map_object.longueur, map_object.hauteur), color=(0, 0, 0))
    draw = ImageDraw.Draw(img)
    for i in range(0, map_object.hauteur):
        for j in range(0, map_object.longueur):
            draw.point((j, i), fill=BiomeColors[map_object.map[i][j]])
    img.save(os.path.join("output",filename))
    print("Duree l'export image : %s secondes ---" % (time.time() - export_time))

# ouverture html :
def Open_html(nomhtml):
    import os
    from urllib.parse import urljoin
    import webbrowser
    file_path = nomhtml
    file_path = urljoin('file://', os.path.abspath(file_path))
    webbrowser.open(file_path)

def ecriremap(map_object, nomfic):
    fichier = open(os.path.join("output", nomfic), "w")
    fichier.write(str(map_object.longueur))
    fichier.write("\n")
    fichier.write(str(map_object.hauteur))
    fichier.write("\n")
    for i in range(0, map_object.hauteur):
        for j in range(0, map_object.longueur):
            fichier.write(str(map[i][j]))
            fichier.write('|')
        fichier.write("\n")
    for i in range(0, map_object.hauteur):
        for j in range(0, map_object.longueur):
            fichier.write(str(map_object.mapr[i][j]))
            fichier.write('|')
        fichier.write("\n")
    fichier.close()

def liremap(nomfic):
    fichier = open(nomfic, "r")
    map_object = MapObject()
    map_object.longueur = int(fichier.readline())
    map_object.hauteur = int(fichier.readline())
    i = 0
    for ligne in fichier:
        s = ligne.strip("\n\r")
        s = s.strip()
        li = s.split("|")
        if (i < map_object.hauteur):
           map_object.map.append(li)
        else:
            map_object.mapr.append(li)
        i = i + 1
    fichier.close()
    return map