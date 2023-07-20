import time
import random
from parameters import *

class MapObject():
    hauteur = 0
    longueur = 0
    map = []
    mapr = []

    def __init__(self, longueur, hauteur):
        self.longueur = longueur
        self.hauteur = hauteur
        self.map = []
        self.mapr = []
    
    def initmap(self):
        self.map = []
        for i in range(0, self.hauteur):
            self.map.append([])
            for j in range(0, self.longueur):
                self.map[i].append(1)
        return self.map
    
    def creationratio(self):
        ratio = []
        surface = self.hauteur * self.longueur
        print(surface)
        if surface <= 200:
            nbcont = random.randint(1, 6)
            taillecont = int(surface / 10)
            surfaceterre = int(surface / 4)
        elif surface > 200 and surface <= 2500:
            nbcont = random.randint(3, int(surface / 50))
            taillecont = int(surface / 20)
            surfaceterre = int(surface / 4)
        elif surface > 2500 and surface <= 25000:
            nbcont = int(surface / 25)
            taillecont = int(surface / 5)
            surfaceterre = int(surface / 2.5)
        else:
            nbcont = int(surface / 500)
            taillecont = int(surface / 250)
            surfaceterre = int(surface / 4)
        ratio.append(surface)
        ratio.append(nbcont)
        ratio.append(surfaceterre)
        ratio.append(taillecont)
        d2 = [1, 0.75, 0.66, 0.5, 0.33, 0.25, 0.15]
        d = [0.5, 0.4, 0.33, 0.25, 0.20, 0.15, 0.10, 0.05, 0.02]
        for i in range(0, len(d)):
            ##            ratio.append(int(longueur*d[i]))
            ##            ratio.append(int(hauteur*d[i]))
            ratio.append(int(ratio[2] * d[i]))
        print(ratio[2])
        return ratio


    def pourratio(ratio, x):
        var = 0
        var = int((x * 100) / ratio[0])
        print("var=", var)
        return var


    def creationterre(self, ratio):
        crea_time = time.time()
        # ligne_time=time.time()
        taille = 0
        ct = 0
        taillemap = ratio[0]
        for i in range(0, ratio[1]):  # defini le nb de continent
            if (ct < ratio[2]):
                c = 0
                x = random.randint(0, self.longueur - 1)
                y = random.randint(0, self.hauteur - 1)
                while (self.map[y][x] != ocn and c <= 4):
                    c = c + 1
                    x = random.randint(0, self.longueur - 1)
                    y = random.randint(0, self.hauteur - 1)
                terr = terre
                if (self.map[y][x] != terr):
                    self.map[y][x] = terr
                    ct = ct + 1
                tailleC = random.randint(1, ratio[3])
                for b in range(1, int(tailleC)):  # defini la taille des continents
                    if (ct < ratio[2]):
                        ##                                c=0
                        caseadj = self.caseadjacente(x, y)
                        co = random.randint(0, len(caseadj) - 1)
                        x1 = caseadj[co][0]
                        y1 = caseadj[co][1]
                        ##                                while (map[y1][x1]!=ocn and c<=4):
                        ##                                        co=random.randint(0,len(caseadj)-1)
                        ##                                        c=c+1
                        ##                                        x1=caseadj[co][0]
                        ##                                        y1=caseadj[co][1]
                        ##            print("y1= ",y1,"  x1=",x1)
                        x = x1
                        y = y1
                        if (self.map[y][x] != terr):
                            self.map[y][x] = terr
                            ct = ct + 1
        ##                                caseadj.clear()
        ##                print(ct)
        ##                n=len(poss)*2
        ##        adj,diag=adjacence(map,x,y)
        print("Duree de generation des terres emergees : %s secondes ---" % (time.time() - crea_time))
        return self.map


    def creationeige(self, ratio):
        crea_time = time.time()
        taille = 0
        nord = int((self.hauteur / 10) * 0.5)
        sud = int((self.hauteur / 10) * 9.5)
        terr = neige
        for j in range(0, self.hauteur):
            for i in range(0, self.longueur):
                if self.map[j][i] == terre:
                    if (j < nord or j > sud):
                        taille = random.randint(0, 20)
                        x = i
                        y = j
                        for b in range(0, taille):
                            c = 0
                            caseadj = self.caseadjacente(x, y)
                            co = random.randint(0, len(caseadj) - 1)
                            x1 = caseadj[co][0]
                            y1 = caseadj[co][1]
                            while (self.map[y1][x1] != terre and c < 5):
                                co = random.randint(0, len(caseadj) - 1)
                                x1 = caseadj[co][0]
                                y1 = caseadj[co][1]
                                c = c + 1
                            self.map[y1][x1] = terr
                            x = x1
                            y = y1
        print("Duree de generation des neiges : %s secondes ---" % (time.time() - crea_time))
        return self.map


    def creationdesert(self, ratio):
        crea_time = time.time()
        nord = (self.hauteur / 10) * 4.5
        sud = (self.hauteur / 10) * 5.5
        hns = sud - nord
        terr = desert
        for j in range(0, self.hauteur):
            for i in range(0, self.longueur):
                if self.map[j][i] == terre:
                    if j > nord and j < sud:
                        ##                    ran=[]
                        ##                    multi=random.randint(1,20)
                        ##                    ran.append(desert)
                        ##                    for b in range (0,multi):
                        ##                        ran.append(0)
                        ##                    ch=random.randint(0,len(ran)-1)
                        ##                    if ran[ch]==desert :
                        taille = random.randint(0, 20)
                        x = i
                        y = j
                        for b in range(0, int(taille)):
                            c = 0
                            caseadj = self.caseadjacente(x, y)
                            co = random.randint(0, len(caseadj) - 1)
                            x1 = caseadj[co][0]
                            y1 = caseadj[co][1]
                            while (self.map[y1][x1] != terre and c < 5):
                                co = random.randint(0, len(caseadj) - 1)
                                x1 = caseadj[co][0]
                                y1 = caseadj[co][1]
                                c = c + 1
                            self.map[y1][x1] = terr
                            x = x1
                            y = y1
        print("Duree de generation des deserts : %s secondes ---" % (time.time() - crea_time))
        return self.map


    def creationplaine(self, ratio):
        crea_time = time.time()
        # ligne_time=time.time()
        for j in range(0, self.hauteur):
            for i in range(0, self.longueur):
                if self.map[j][i] == terre:
                    self.map[j][i] = pln
        print("Duree de generation des plaines : %s secondes ---" % (time.time() - crea_time))
        return self.map


    def creationcolline(self, ratio):
        crea_time = time.time()
        # ligne_time=time.time()
        taille = 0
        ct = 0
        print(ratio[8])
        taillemap = ratio[0]
        for i in range(0, int(ratio[10])):
            if (ct < ratio[8]):
                x = random.randint(0, self.longueur - 1)
                y = random.randint(0, self.hauteur - 1)
                while (self.map[y][x] not in [neige, pln, desert]):
                    x = random.randint(0, self.longueur - 1)
                    y = random.randint(0, self.hauteur - 1)
                terr = col
                self.map[y][x] = terr
                ct = ct + 1
                tailleC = random.randint(1, ratio[10])
                for b in range(1, int(tailleC)):
                    c = 0
                    caseadj = self.caseadjacente(x, y)
                    co = random.randint(0, len(caseadj) - 1)
                    x1 = caseadj[co][0]
                    y1 = caseadj[co][1]
                    while (self.map[y1][x1] not in [neige, pln, desert] and c < 5):
                        x1 = caseadj[co][0]
                        y1 = caseadj[co][1]
                        co = random.randint(0, len(caseadj) - 1)
                        c = c + 1
                    ##            print("y1= ",y1,"  x1=",x1)
                    self.map[y1][x1] = terr
                    x = x1
                    y = y1
                    ct = ct + 1
                    caseadj.clear()
            n = len(poss) * 2
        ##        adj,diag=adjacence(map,x,y)
        print("Duree de generation des collines : %s secondes ---" % (time.time() - crea_time))
        return self.map


    def creationmontagne(self, ratio):
        crea_time = time.time()
        # ligne_time=time.time()
        taille = 0
        ctt = 0
        ct = 0
        c = 0
        x1 = 0
        y1 = 0
        for i in range(0, int(ratio[12])):
            if (ct < ratio[10]):
                x = random.randint(0, self.longueur - 1)
                y = random.randint(0, self.hauteur - 1)
                while (self.map[y][x] != col):
                    x = random.randint(0, self.longueur - 1)
                    y = random.randint(0, self.hauteur - 1)
                terr = mont
                self.map[y][x] = terr
                ctt = ctt + 1
                ##        print("taille=",taille)
                tailleC = random.randint(1, ratio[10])
                for b in range(1, tailleC):
                    ct = 3
                    c = 0
                    caseadj = self.caseadjacente(self.map, x, y)
                    casediag = self.casediagonale(self.map, x, y)
                    while ct > 2 and c < 6:
                        ##                print("c=",c)
                        ct = 0
                        c = c + 1
                        co = random.randint(0, len(caseadj) - 1)
                        x1 = caseadj[co][0]
                        y1 = caseadj[co][1]
                        caseadj1 = self.caseadjacente(self.map, x1, y1)
                        for i in range(0, len(caseadj1)):
                            ##                    print("i=",i)
                            x2 = caseadj1[i][0]
                            y2 = caseadj1[i][1]
                            if (self.map[y2][x2] == mont):
                                ct = ct + 1
                    ##                        print(ct)
                    co = random.randint(0, len(caseadj) - 1)
                    x1 = caseadj[co][0]
                    y1 = caseadj[co][1]
                    self.map[y1][x1] = terr
                    ctt = ctt + 1
                    x = x1
                    y = y1
                    caseadj.clear()
        n = len(poss) * 2
        ##        adj,diag=adjacence(map,x,y)
        print("Duree de generation des montagnes : %s secondes ---" % (time.time() - crea_time))
        return self.map


    def creationmer(self, ratio):
        crea_time = time.time()
        for j in range(0, self.hauteur):
            for i in range(0, self.longueur):
                if self.map[j][i] == ocn:
                    caseadj = self.caseadjacente(i, j)
                    for b in range(0, len(caseadj)):
                        x1 = caseadj[b][0]
                        y1 = caseadj[b][1]
                        if self.map[y1][x1] in [pln, col, mont, neige, desert]:
                            self.map[j][i] = mer
                    if self.map[j][i] == ocn:
                        casediag = self.casediagonale(i, j)
                        ##                                        print(casediag)
                        for b in range(0, len(casediag)):
                            x1 = casediag[b][0]
                            y1 = casediag[b][1]
                            ##                                                print("y1=",y1,"x1=",x1)
                            if self.map[y1][x1] in [pln, col, mont, neige, desert]:
                                self.map[j][i] = mer
        print("Duree de generation des mers : %s secondes ---" % (time.time() - crea_time))
        return self.map


    def lissage(self, ratio):
        crea_time = time.time()
        for j in range(0, self.hauteur):
            for i in range(0, self.longueur):
                if self.map[j][i] in [ocn, mer]:
                    caseadj = self.caseadjacente(i, j)
                    ct = 0
                    x = 0
                    y = 0
                    for b in range(0, len(caseadj)):
                        x1 = caseadj[b][0]
                        y1 = caseadj[b][1]
                        if self.map[y1][x1] in [pln, col, mont, neige, desert]:
                            ct = ct + 1
                            x = x1
                            y = y1
                    if ct == 3:
                        ran = []
                        for b in range(1, 6):
                            ran.append(self.map[y][x])
                        ran.append(lac)
                        ran.append(marais)
                        rdn = random.randint(0, len(ran) - 1)
                        self.map[j][i] = ran[rdn]
                    if ct == 4:
                        ran = []
                        for b in range(1, 10):
                            ran.append(self.map[y][x])
                        ran.append(lac)
                        ran.append(marais)
                        rdn = random.randint(0, len(ran) - 1)
                        self.map[j][i] = ran[rdn]
        print("Duree du lissage : %s secondes ---" % (time.time() - crea_time))
        return self.map


    # ressource map
    def ressourcemap(self):
        ctp = 0
        cto = 0
        ress_time = time.time()
        self.mapr = []
        for i in range(0, self.hauteur):
            self.mapr.append([])
            for j in range(0, self.longueur):
                self.mapr[i].append(0)
        for i in range(0, self.hauteur):
            for j in range(0, self.longueur):
                ran = []
                multi = random.randint(2, 5)
                for b in range(0, multi):
                    ran.append(ress_rie)
                if (self.map[i][j] == ocn or self.map[i][j] == mer):
                    cto = cto + 1
                    multi = random.randint(0, 1)
                    for b in range(0, multi):
                        ran.append(ress_poi)
                n = len(ran)
                v = random.randint(0, n - 1)
                if (ran[v] == ress_poi):
                    ctp = ctp + 1
                self.mapr[i][j] = ran[v]
        print("Duree de generation de la map des ressources : %s secondes ---" % (time.time() - ress_time))
        if cto == 0:
            r = 0
        else:
            r = ctp / cto
        r = r * 100
        r = round(r, 2)
        print("ratio poisson =", r, "%")
        return self.mapr


    # fonction qui regarde si type case n est adjacent a la case actuelle
    def adjacence(self, i, j):
        adj = []
        diag = []
        if (j > 0):
            adj.append(self.map[i][j - 1])
        if (i > 0):
            adj.append(self.map[i - 1][j])
        if (j < self.longueur - 1):
            adj.append(self.map[i][j + 1])
        if (i < self.hauteur - 1):
            adj.append(self.map[i + 1][j])
        if (j < self.longueur - 2):
            diag.append(self.map[i][j + 2])
        if (i < self.hauteur - 2):
            diag.append(self.map[i + 2][j])
        if (j > 1):
            diag.append(self.map[i][j - 2])
        if (i > 1):
            diag.append(self.map[i - 2][j])
        if (i > 0 and j > 0):
            diag.append(self.map[i - 1][j - 1])
        if i > 0 and j < self.longueur - 1:
            diag.append(self.map[i - 1][j + 1])
        if (i < self.hauteur - 1 and j > 0):
            diag.append(self.map[i + 1][j - 1])
        if (i < self.hauteur - 1 and j < self.longueur - 1):
            diag.append(self.map[i + 1][j + 1])
        return adj, diag


    def caseadjacente(self, i, j):  # i=longueur et j=hauteur terre sous forme de tube donc possibilite de passer d un coté a l autre
        caseadj = []
        if (j > 0):
            caseadj.append([i, j - 1])
        ##        else :
        ##                caseadj.append([i,hauteur-1])
        if (i > 0):
            caseadj.append([i - 1, j])
        else:
            caseadj.append([self.longueur - 1, j])
        if (j < self.hauteur - 1):
            caseadj.append([i, j + 1])
        ##        else :
        ##                caseadj.append([i,0])
        if (i < self.longueur - 1):
            caseadj.append([i + 1, j])
        else:
            caseadj.append([0, j])
        return caseadj


    def casediagonale(self, i, j):  # i=longueur et j=hauteur
        casediag = []
        if (j > 0 and i > 0):
            casediag.append([i - 1, j - 1])
        elif (j > 0):
            casediag.append([self.longueur - 1, j - 1])
        if (i > 0 and j < self.hauteur - 1):
            casediag.append([i - 1, j + 1])
        elif (j < self.hauteur - 1):
            casediag.append([self.longueur - 1, j + 1])
        if (j < self.hauteur - 1 and i < self.longueur - 1):
            casediag.append([i + 1, j + 1])
        elif (j < self.hauteur - 1):
            casediag.append([0, j + 1])
        if (i < self.longueur - 1 and j > 0):
            casediag.append([i + 1, j - 1])
        elif (j > 0):
            casediag.append([0, j - 1])
        return casediag


    def recherche(L, x):
        for i in range(0, len(L)):
            if (L[i] == x):
                return True
        return False

    def creationmap(self):
        self.map = self.initmap()
        ratio = self.creationratio()
        self.map = self.creationterre(ratio)
        self.map = self.creationeige(ratio)
        self.map = self.creationdesert(ratio)
        self.map = self.creationplaine(ratio)
        self.map = self.creationcolline(ratio)
        ##        map=creationmontagne(ratio)
        self.map = self.creationmer(ratio)
        self.map = self.lissage(ratio)
        self.mapr = self.ressourcemap()
        print(ratio)
        return self.map, self.mapr