import random
import re
import time
import csv

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


#taille map
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
            map[i].append(1)
    return map


#creation map
def creationterre():
    crea_time=time.time()
    #ligne_time=time.time()
    taille=0
    gr=[]
    taillemap=hauteur*longueur
    for i in range (0,longueur):
        u=random.randint(1,longueur)
        u=int(taillemap/u)
        taille=random.randint(1,u)
        x=random.randint(0,longueur-1)
        y=random.randint(0,hauteur-1)
        terr=pln
        map[x][y]=terr
        for b in range (1,taille):
            caseadj=caseadjacente(map,x,y)
            co=random.randint(0,len(caseadj)-1)
            x1=caseadj[co][0]
            y1=caseadj[co][1]
            map[x1][y1]=terr
            x=x1
            y=y1
            caseadj.clear()
        ran=[]
        ran=poss[:]
        n=len(poss)*2
        adj,diag=adjacence(map,x,y)
        ran.clear()
        modul=1
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
def adjacence(map,i,j):
    adj=[]
    diag=[]
    if (j>0):
        adj.append(map[i][j-1])
    if (i>0):
        adj.append(map[i-1][j])
    if (j<longueur-1):
        adj.append(map[i][j+1])
    if (i<hauteur-1):
        adj.append(map[i+1][j])
    if (j<longueur-2):
        diag.append(map[i][j+2])
    if (i<hauteur-2):
        diag.append(map[i+2][j])
    if (j>1):
        diag.append(map[i][j-2])
    if (i>1):
        diag.append(map[i-2][j])
    if (i>0 and j>0):
        diag.append(map[i-1][j-1])
    if (i>0 and j<longueur-1):
        diag.append(map[i-1][j+1])
    if (i<hauteur-1 and j>0):
        diag.append(map[i+1][j-1])
    if (i<hauteur-1 and j<longueur-1):
        diag.append(map[i+1][j+1])
    return adj,diag


def caseadjacente(map,i,j):
    caseadj=[]
    if (j>0):
        caseadj.append([i,j-1])
    if (i>0):
        caseadj.append([i-1,j])
    if (j<longueur-1):
        caseadj.append([i,j+1])
    if (i<hauteur-1):
        caseadj.append([i+1,j])
    return caseadj


def recherche(L,x):
    for i in range(0,len(L)):
        if (L[i]==x):
            return True
    return False

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
    while (quest!=V[0] and quest!=V[1] and quest!=V[2] and quest!=V[3] and quest!=V[4] and quest!=V[5]):
        print("Erreur!")
        print(text,end='')
        quest=str(input(" ? "))
    return quest


#ini variable fixe
def question():
    lp=len(poss)
    print("Lecture, ecriture ou rien")
    fic=str(input("l,e,r : "))
    while (fic!='r' and fic!='e' and fic!='l' and fic!='lire' and fic!='lecture' and fic!='ecrire' and fic!='ecriture' and fic!='rien'):
        print("Erreur!")
        print("Lecture, ecriture ou rien")
        fic=str(input("l,e,r : "))
    return fic


#question ferme avec verif
def yesno( text):
    print(text,end='')
    qu=str(input(" : "))
    while (qu!="n" and qu!="o" and qu!="non" and qu!="oui"):
        print("Erreur")
        print(text,end='')
        qu=str(input(" : "))     
    return qu


#### export html
BiomeColors = ["#000000", "#3c4adb","#67c1fa", "#54d239","#ba762d","#afafaf"]
ResColors = ["#000000", "#f62bff", "#f4ff00", "#73ff55", "#ff2b2b"]
def export_html(L,nomhtml):
    export_time=time.time()
    with open(nomhtml, 'w') as fichier:
	    fichier.write("<!doctype html>\n<html>\n<head>\n<style>\n .td\n { width:40px; height:40px;}\n")
	    #couleurs des cases en fonction du biome/type de terrain :
	    for i in range(len(BiomeColors)):
	    	fichier.write('.d'+str(i)+'\n{background-color:'+BiomeColors[i]+';}\n')
	    #couleurs de texte en fonction des ressources:
	    for i in range(len(ResColors)):
	    	fichier.write('.R'+str(i)+'\n{color:'+ResColors[i]+';}\n')
	    fichier.write('</style>\n<meta charset="utf-8">\n</head>\n<body>\n<table border="0">\n')
	    ligne=0
	    #ligne_time=time.time()
	    for i in range (0,hauteur):
	        ligne=ligne+1
	        fichier.write( "			<tr>\n")
	        for j in range (0,longueur):
	            fichier.write('<td class="d'+str(map[i][j])+'">'+"<pre class=R"+str(mapr[i][j])+" > "+str(map[i][j])+"|"+str(mapr[i][j])+" </pre>"+"</td>\n")
	        fichier.write("			</tr>\n")
	        modul=ligne%50
	        if modul==0:
	            print("Export ligne : ", ligne)
	            #print("Temps d execution : %s secondes ---" % (time.time() - ligne_time))
	            #ligne_time=time.time()
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
else :
    longueur=200
    hauteur=200
    aff="non"
    html="oui"
    fic="rien"
start_time=time.time()
map=initmap()
if (fic=='r' or fic=='e' or fic=='rien' or fic=='ecrire' or fic=='ecriture'):
    map=creationterre()
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