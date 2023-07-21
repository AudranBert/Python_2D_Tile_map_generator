import time
import random
from parameters import *

class MapObject():

    def __init__(self, longueur, hauteur, map_generator=None, generate_resources=True):
        self.longueur = longueur
        self.hauteur = hauteur
        self.map_generator = map_generator
        self.map_generator.init_generator(self)
        print(f"Using '{self.map_generator.__class__.__name__}' as map generator")
        self.use_heightmap = True
        self.generate_resources = generate_resources
        self.map = []
        self.mapr = []
    
    def initmap(self):
        self.map = []
        for i in range(0, self.hauteur):
            self.map.append([])
            for j in range(0, self.longueur):
                self.map[i].append(1)
        return self.map
    
    def get_surface(self):
        return self.longueur * self.hauteur

    def get_land_ratio(self):
        total = self.longueur * self.hauteur
        land = 0
        for i in range(0, self.hauteur):
            for j in range(0, self.longueur):
                if self.map[i][j] != ocn and self.map[i][j] != mer:
                    land += 1
        return land/total

    def get_hills_qtt(self):
        hills = 0
        for i in range(0, self.hauteur):
            for j in range(0, self.longueur):
                if self.map[i][j] == col:
                    hills += 1
        return hills    

   


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

    def generate_map(self):
        self.map = self.initmap()
        t = time.time()
        self.map = self.map_generator.generate_lands()
        print(f"Duree de generation des terres : {time.time() - t:.2f} secondes")
        t = time.time()
        self.map = self.map_generator.generate_snows()
        print(f"Duree de generation des neiges : {time.time() - t:.2f} secondes")
        t = time.time()
        self.map = self.map_generator.generate_deserts()
        print(f"Duree de generation des deserts : {time.time() - t:.2f} secondes")
        t = time.time()
        self.map = self.map_generator.generate_plains()
        print(f"Duree de generation des plaines : {time.time() - t:.2f} secondes")
        t = time.time()
        self.map = self.map_generator.generate_hills()
        print(f"Duree de generation des collines : {time.time() - t:.2f} secondes")
        t = time.time()
        self.map = self.map_generator.generate_mountains()
        print(f"Duree de generation des montagnes : {time.time() - t:.2f} secondes")
        t = time.time()
        self.map = self.map_generator.generate_seas()
        print(f"Duree de generation des mers : {time.time() - t:.2f} secondes")
        t = time.time()
        self.map = self.map_generator.flatten()
        print(f"Duree du lissage : {time.time() - t:.2f} secondes")
        t = time.time()
        if self.generate_resources:
            self.mapr = self.map_generator.generate_resources_map()
            print(f"Duree de generation des ressources : {time.time() - t:.2f} secondes")
        return self.map, self.mapr
    
