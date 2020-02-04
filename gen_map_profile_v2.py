#code modif: #modif_NL_2

import random
import re
import time
import csv
import os.path #modif_NL_2
from urllib.parse import urljoin #modif_NL_2

#fixe
poss=[1,2,3,4,5]
ress=[0,1,2,3,4]
nom=['rien','O','M','P','C','S']
nomr=['rien','poisson','ble','foret','minerais']
ocn=1
mer=2
pln=3
col=4
mont=5
ress_rie=0
ress_poi=1
ress_for=2
ress_ble=3
ress_min=4
lire=0
longueur=0
hauteur=0
map=[]
mapr=[]
qu="rien"
nomhtml="export.html"


# modif_NL_2{
def readProfile(profileName):
	with open("includ.py", 'w') as inc:
		inc.write("from "+profileName+" import *")
# }modif_NL_2


# taille map
def taille():
    print("Taille de votre map")
    strlongueur=str(input("Longueur : "))
    er=re.compile('\D')
    ter=er.match(strlongueur)
    while (ter):
        print("Erreur ce n'es pas un nombre !")
        strlongueur=str(input("Longueur : "))
        ter=er.match(strlongueur)
    longueur=int(strlongueur)
    strhauteur=str(input("Hauteur : "))
    er=re.compile('\D')
    ter=er.match(strhauteur)
    while (ter):
        print("Erreur ce n'es pas un nombre !")
        strhauteur=str(input("Hauteur : "))
        ter=er.match(strhauteur)
    hauteur=int(strhauteur)
    return longueur,hauteur


#lire un fichier
def lirecaracmap(nomfic):
    fichier=open(nomfic, "r")
    longueur=int(fichier.readline())
    hauteur=int(fichier.readline())
    fichier.close()
    return longueur,hauteur

#lire
def liremap(nomfic):
    fichier=open(nomfic, "r")
    longueur=int(fichier.readline())
    hauteur=int(fichier.readline())
    map.clear()
    mapr.clear()
    i=0
    for ligne in fichier:
        s=ligne.strip("\n\r")
        s=s.strip()
        li=s.split("|")
        if (i<hauteur):
            map.append(li)
        else :
            mapr.append(li)
        i=i+1
    fichier.close()
    return map


#init map
def initmap():
    map=[]
    for i in range (0,hauteur):
        map.append([])
        for j in range (0,longueur):
            map[i].append(0)
    return map


#creation map
def creationmap():
    crea_time=time.time()
    #ligne_time=time.time()
    for i in range (0,hauteur):
        for j in range (0,longueur):
            ran=[]
            ran=poss[:]
            multi=random.randint(0,2)
            for b in range (0,multi):
                ran.append(pln)
            n=len(poss)*2
            if (map[i-1][j]!=0):
                if (map[i-1][j]==mont):
                    multi=random.randint(0,2)
                    for b in range(0,multi):
                        ran.append(mont)
                    multi=random.randint(0,2)
                    for b in range(0,multi):
                        ran.append(col)
                elif (map[i-1][j]==ocn):
                    multi=random.randint(0,2)
                    for b in range(0,multi):
                        ran.append(ocn)
                    multi=random.randint(0,2)
                    for b in range(0,multi):
                        ran.append(mer)
                else :
                    multi = random.randint(1,n-1)
                    for b in range(0,multi):
                        ran.append(map[i-1][j])
            if (map[i][j-1]!=0):
                if (map[i][j-1]==mont):
                    multi=random.randint(0,1)
                    for b in range(0,multi):
                        ran.append(mont)
                    multi=random.randint(0,1)
                    for b in range(0,multi):
                        ran.append(col)
                elif (map[i][j-1]==ocn):
                    multi=random.randint(0,2)
                    for b in range(0,multi):
                        ran.append(ocn)
                    multi=random.randint(0,2)
                    for b in range(0,multi):
                        ran.append(mer)
                else :
                    multi = random.randint(1,n-1)
                    for b in range(0,multi):
                        ran.append(map[i][j-1])
            n=1
            if (map[i-1][j-1]!=0):
                multi = random.randint(0,n)
                for b in range(0,multi):
                    ran.append(map[i-1][j-1])
            if (map[i][j-2]!=0):
                multi = random.randint(0,n)
                for b in range(0,multi):
                    ran.append(map[i][j-2])
            if (map[i-2][j]!=0):
                multi = random.randint(0,n)
                for b in range(0,multi):
                    ran.append(map[i-2][j])
            n=len(ran)
            #print(ran)
            v = random.randint(0,n-1)
            map[i][j]=ran[v]
            ran.clear()
        modul=i%50
        if modul==0:
            print("Creation ligne : ", i)
            #print("Temps d execution : %s secondes ---" % (time.time() - ligne_time))
            #ligne_time=time.time()
    print("Duree de generation de la map : %s secondes ---" % (time.time() - crea_time))
    return map

#ressource map
def ressourcemap():
    ress_time=time.time()
    mapr=[]
    for i in range (0,hauteur):
        mapr.append([])
        for j in range (0,longueur):
            mapr[i].append(0)
    for i in range (0,hauteur):
        for j in range (0,longueur):
            ran=[]
            multi=random.randint(1,3)
            for b in range (0,multi):
                ran.append(ress_rie)
            if (map[i][j]==ocn or map[i][j]==mer):
                multi=random.randint(0,2)
                for b in range (0,multi):
                    ran.append(ress_poi)
            n=len(ran)
            v=random.randint(0,n-1)
            mapr[i][j]=ran[v]
    print("Duree de generation de la map des ressources : %s secondes ---" % (time.time() - ress_time))            
    return mapr


#fonction qui regarde si type case n est adjacent a la case actuelle

#fct qui regarde si type case n est present en diagonale de la case traite

#sous map

#affichage graphique

#ecrire dans un fichier
def ecriremap(nomfic):
    fichier=open(nomfic, "w")
    fichier.write(str(longueur))
    fichier.write("\n")
    fichier.write(str(hauteur))
    fichier.write("\n")
    for i in range (0,hauteur):
        for j in range (0,longueur):
            fichier.write(str(map[i][j]))
            fichier.write('|')
        fichier.write("\n")
    for i in range (0,hauteur):
        for j in range (0,longueur):
            fichier.write(str(mapr[i][j]))
            fichier.write('|')
        fichier.write("\n")
    fichier.close()


#affichage map
def affichagetm():
    print("\n Map : ")
    for i in range (0,hauteur):
        for j in range (0,longueur):
            print(map[i][j],'| ',end='')
        print('')
    print('')
##    for i in range (0,hauteur):
##        for j in range (0,longueur):
##            print(nom[map[i][j]],'| ',end='')
##        print('')
##    print('')

#affichage mapressource
def affichagetr():
    print("\n Map des ressources : ")
    for i in range (0,hauteur):
        for j in range (0,longueur):
            print(mapr[i][j],'| ',end='')
        print('')
    print('')
##    for i in range (0,hauteur):
##        for j in range (0,longueur):
##            print(nom[map[i][j]],'| ',end='')
##        print('')
##    print('')


#question ouverte sans verif
def quest(text):
    print(text,end='')
    quest=str(input(" ? "))
    return quest

#question ouverte avec 6 verif
def quest6(text,V):
    print(text,end='')
    quest=str(input(" ? "))
    #while (quest!=V[0] and quest!=V[1] and quest!=V[2] and quest!=V[3] and quest!=V[4] and quest!=V[5]):
    while (quest not in V):
        print("Erreur!")
        print(text,end='')
        quest=str(input(" ? "))
    return quest


#ini variable fixe
def question():
    lp=len(poss)
    print("Lecture, ecriture ou rien")
    fic=str(input("l,e,r : "))
    #while (fic!='r' and fic!='e' and fic!='l' and fic!='lire' and fic!='lecture' and fic!='ecrire' and fic!='ecriture' and fic!='rien'):
    while (fic not in ["r", "e", "l", "lire", "lecture", "ecrire", "ecriture", "rien"]):
        print("Erreur!")
        print("Lecture, ecriture ou rien")
        fic=str(input("l,e,r : "))
    return fic


#question ferme avec verif
def yesno( text):
    print(text,end='')
    qu=str(input(" : "))
    #while (qu!="n" and qu!="o" and qu!="non" and qu!="oui"):
    while (not qu in ["n", "o", "non", "oui"]):
        print("Erreur")
        print(text,end='')
        qu=str(input(" : "))     
    return qu


# export html
BiomeColors = ["#000000", "#3c4adb","#67c1fa", "#54d239","#ba762d","#afafaf"]
ResColors = ["#000000", "#f62bff", "#f4ff00", "#73ff55", "#ff2b2b"]
def export_html(L, nomhtml):
    export_time=time.time()
    with open(nomhtml, 'w') as fichier:
	    fichier.write("<!doctype html>\n<html>\n<head>\n<style>\n .td\n { width:40px; height:40px;}\n")
	    # couleurs des cases en fonction du biome/type de terrain :
	    for i in range(len(BiomeColors)):
	    	fichier.write('.d'+str(i)+'\n{background-color:'+BiomeColors[i]+';}\n')
	    # couleurs de texte en fonction des ressources:
	    for i in range(len(ResColors)):
	    	fichier.write('.R'+str(i)+'\n{color:'+ResColors[i]+';}\n')
	    fichier.write('</style>\n<meta charset="utf-8">\n</head>\n<body>\n<table border="0">\n')
	    ligne = 0
	    #ligne_time=time.time()
	    for i in range (0,hauteur):
	        ligne = ligne+1
	        fichier.write( "			<tr>\n")
	        for j in range (0,longueur):
	            fichier.write('<td class="d'+str(map[i][j])+'">'+"<pre class=R"+str(mapr[i][j])+" > "+str(map[i][j])+"|"+str(mapr[i][j])+" </pre>"+"</td>\n")
	        fichier.write("			</tr>\n")
	        modul = ligne%50
	        if modul == 0:
	            print("Export ligne : ", ligne)
	            # print("Temps d execution : %s secondes ---" % (time.time() - ligne_time))
	            # ligne_time=time.time()
	    fichier.write("		</table>\n"+"	</body>\n"+"</html>")
    print("Duree l'export HTML : %s secondes ---" % (time.time() - export_time))
    

# ouverture html :
def Open_html(nomhtml):
    import os
    from urllib.parse import urljoin
    import webbrowser
    file_path = nomhtml
    file_path = urljoin('file://', os.path.abspath(file_path))
    webbrowser.open(file_path)
####


#main


print ("\tProgramme de gÃ©nÃ©ration de map alÃ©atoire par Audran")
if(yesno("import profile? (o/n)") in ["non", "n"]):
	with open("includ.py", 'w') as inc:
		inc.write("")
	auto=yesno("Mode auto")
	V=[]
	if (auto=='n' or auto=='non'):
	    V=["e","l","r","ecriture","lecture","rien"]
	    fic=quest6("Lecture,ecriture ou rien",V)
	    if (fic=='e' or fic=='ecriture'):
	        nomfic=quest("Nom du fichier de destination (.txt)")
	    if (fic=='r' or fic=='e' or fic=='rien' or fic=='ecrire' or fic=='ecriture') :
	        longueur,hauteur=taille()
	    else :
	        nomfic=quest("Nom du fichier de lecture (.txt)")
	        longueur,hauteur=lirecaracmap(nomfic)
	    aff=yesno("Affichage? o/n ")
	    html=yesno("Export Html? o/n")
	    if (html=='o' or html=='oui'):
	        nomhtml=quest("Nom du fichier de l export (.html)")
	else:
			longueur=20
			hauteur=20
			aff="non"
			html="oui"
			fic="rien"
else:
	import glob, dialogs
	profileList = glob.glob('profile*.py')
	profileList = list(i[:-3] for i in profileList) # [:-3] pour enlever .py
	includName = dialogs.list_dialog(title='hello', items=profileList, multiple=False)
	'''for i in range(len(profileList)):
		print(i+1, " : ", profileList[i])
	includName=profileList[int(input("profile number : "))-1]'''
	readProfile(includName)
from includ import *

start_time=time.time()
map=initmap()
if (fic=='r' or fic=='e' or fic=='rien' or fic=='ecrire' or fic=='ecriture'):
    map=creationmap()
    mapr=ressourcemap()
    if (fic=='e'):
        ecriremap(nomfic)
elif (fic=='l' or fic=='lecture'):
        map=liremap(nomfic)
if (aff=='oui' or aff=='o'):
    affichagetm()
    affichagetr()
if (html=='oui' or html=='o'):
    export_html(map,nomhtml)
print("Temps total d execution : %s secondes ---" % (time.time() - start_time)) 
print("\tGeneration termine !") 

if (html=='oui' or html=='o'):
    Open_html(nomhtml)
