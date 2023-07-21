import time
import random
from parameters import *


class MapGenerator():

    def __init__(self):
        self.map_object = None
        
    
    def init_generator(self, map_object):
        self.map_object = map_object
        self.hauteur = self.map_object.hauteur
        self.longueur = self.map_object.longueur

    def get_ratios(self):
        ratio = dict()
        surface = self.hauteur * self.longueur
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
        ratio['surface'] = surface
        ratio['nbcont'] = nbcont
        ratio['taillecont'] = taillecont
        ratio['surfaceterre'] = surfaceterre
        return ratio

    def generate_lands(self):
        ct = 0
        ratio = self.get_ratios()
        map_loc = self.map_object.map.copy()
        for i in range(0, ratio['nbcont']):  # defini le nb de continent
            if (ct < ratio['taillecont']):
                c = 0
                x = random.randint(0, self.longueur - 1)
                y = random.randint(0, self.hauteur - 1)
                while (map_loc[y][x] != ocn and c <= 4):
                    c = c + 1
                    x = random.randint(0, self.longueur - 1)
                    y = random.randint(0, self.hauteur - 1)
                terr = terre
                if (map_loc[y][x] != terr):
                    map_loc[y][x] = terr
                    ct = ct + 1
                tailleC = random.randint(1, ratio['surfaceterre'])
                for b in range(1, int(tailleC)):  # defini la taille des continents
                    if (ct < ratio['taillecont']):
                        ##                                c=0
                        caseadj = self.map_object.caseadjacente(x, y)
                        co = random.randint(0, len(caseadj) - 1)
                        x1 = caseadj[co][0]
                        y1 = caseadj[co][1]
                        x = x1
                        y = y1
                        if (map_loc[y][x] != terr):
                            map_loc[y][x] = terr
                            ct = ct + 1
        return map_loc





    def create_stain(self, starting_position, size, requirements=None):
        x =  starting_position[0]
        y = starting_position[1]
        map_loc = self.map_object.map.copy()
        stain = {(x, y)}
        if requirements is None:
            requirements = []
        potentials = set()
        ct = 0

        while ct<=size:
            caseadj = self.map_object.caseadjacente(x, y)
            caseadj = {(i[0], i[1]) for i in caseadj if map_loc[i[1]][i[0]] in requirements}
            potentials.update(caseadj-stain)
            if len(potentials) == 0:
                break
            x, y = random.sample(potentials, 1)[0]
            stain.add((x, y))
            potentials.remove((x, y))
            ct += 1
        return stain


    def generate_snows(self):
        nord = int((self.hauteur / 10) * 0.5)
        sud = int((self.hauteur / 10) * 9.5)
        hns = nord + self.hauteur - sud
        poles_surface = hns * self.longueur

        map_loc = self.map_object.map.copy()

        number_of_snows=  int(self.map_object.get_land_ratio() * poles_surface * 0.001 )
        number_of_snows = max(1, number_of_snows + random.randint(int(-number_of_snows/15), int(number_of_snows/15)))
        max_number_of_snow_per_group = int(100 + self.map_object.get_land_ratio() * poles_surface * 0.02)
        min_number_of_snow_per_group = int(100 + self.map_object.get_land_ratio() * poles_surface * 0.005)
        terr = neige

        for i in range(0, number_of_snows):
            x = random.randint(0, self.longueur - 1)
            pos1 = random.randint(0, int(nord+random.randint(0,int(self.hauteur/8))))
            pos2 = random.randint(int(sud+random.randint(int(-self.hauteur/8),0)), self.hauteur-1)
            y = random.choice([pos1, pos2])
            # y = random.randint(int(nord)+random.randint(0, int(self.hauteur/8)), int(sud)+random.randint(int(-self.hauteur/8), 0))
            while (map_loc[y][x] != terre):
                x = random.randint(0, self.longueur - 1)
                pos1 = random.randint(0, int(nord+random.randint(0,int(self.hauteur/8))))
                pos2 = random.randint(int(sud+random.randint(int(-self.hauteur/8),0)), self.hauteur-1)
                y = random.choice([pos1, pos2])
            tailleC = random.randint(max(100, min_number_of_snow_per_group), max_number_of_snow_per_group)
            stain = self.create_stain((x, y), tailleC, [terre])
            for xy in stain:
                x = xy[0]
                y = xy[1]
                map_loc[y][x] = terr

        return map_loc


    def generate_deserts(self):
        nord = (self.hauteur / 10) * 4.5
        sud = (self.hauteur / 10) * 5.5
        hns = sud - nord
        equator_surface = hns * self.longueur
        
        map_loc = self.map_object.map.copy()
        number_of_deserts=  int(self.map_object.get_land_ratio() * equator_surface * 0.0005 )
        number_of_deserts = max(1, number_of_deserts + random.randint(int(-number_of_deserts/15), int(number_of_deserts/15)))
        max_number_of_desert_per_group = int(100 + self.map_object.get_land_ratio() * equator_surface * 0.02)
        min_number_of_desert_per_group = int(100 + self.map_object.get_land_ratio() * equator_surface * 0.005)
        terr = desert

        for i in range(0, number_of_deserts):
            x = random.randint(0, self.longueur - 1)
            y = random.randint(int(nord)+random.randint(int(-self.hauteur/8), 0), int(sud)+random.randint(0, int(self.hauteur/8)))
            while (map_loc[y][x] != terre):
                x = random.randint(0, self.longueur - 1)
                y = random.randint(int(nord)+random.randint(int(-self.hauteur/8), 0), int(sud)+random.randint(0, int(self.hauteur/8)))
            tailleC = random.randint(max(100, min_number_of_desert_per_group), max_number_of_desert_per_group)
            stain = self.create_stain((x, y), tailleC, [terre])
            for xy in stain:
                x = xy[0]
                y = xy[1]
                map_loc[y][x] = terr
        return map_loc


    def generate_plains(self):
        map_loc = self.map_object.map.copy()
        for j in range(0, self.hauteur):
            for i in range(0, self.longueur):
                if map_loc[j][i] == terre:
                    map_loc[j][i] = pln
        return map_loc


    def generate_hills(self):
        ct = 0
        map_loc = self.map_object.map.copy()
        number_of_hills = random.randint(1, int(self.map_object.get_land_ratio() * self.map_object.get_surface() * 0.3))
        number_of_tries = int(number_of_hills * 0.5)
        max_number_of_hills_per_group =int(min(250, number_of_hills*0.2))
        for i in range(0, number_of_tries):
            if (ct < number_of_hills):
                x = random.randint(0, self.longueur - 1)
                y = random.randint(0, self.hauteur - 1)
                while (map_loc[y][x] not in [neige, pln, desert]):
                    x = random.randint(0, self.longueur - 1)
                    y = random.randint(0, self.hauteur - 1)
                terr = col
                map_loc[y][x] = terr
                ct = ct + 1
                tailleC = random.randint(1, max_number_of_hills_per_group)
                for b in range(1, int(tailleC)):
                    c = 0
                    caseadj = self.map_object.caseadjacente(x, y)
                    co = random.randint(0, len(caseadj) - 1)
                    x1 = caseadj[co][0]
                    y1 = caseadj[co][1]
                    while (map_loc[y1][x1] not in [neige, pln, desert] and c < 5):
                        x1 = caseadj[co][0]
                        y1 = caseadj[co][1]
                        co = random.randint(0, len(caseadj) - 1)
                        c = c + 1
                    ##            print("y1= ",y1,"  x1=",x1)
                    map_loc[y1][x1] = terr
                    x = x1
                    y = y1
                    ct = ct + 1
                    caseadj.clear()
            n = len(poss) * 2
        ##        adj,diag=adjacence(map,x,y)
        return map_loc


    def generate_mountains(self):
        ctt = 0
        ct = 0
        c = 0
        x1 = 0
        y1 = 0
        map_loc = self.map_object.map.copy()
        number_of_mountains = random.randint(1, int(self.map_object.get_hills_qtt()*0.5))
        number_of_tries = int(number_of_mountains * 0.5)
        max_number_of_mountains_per_group =int(min(100, number_of_mountains*0.2))
        for i in range(0, number_of_tries):
            if (ct <number_of_mountains):
                x = random.randint(0, self.longueur - 1)
                y = random.randint(0, self.hauteur - 1)
                while (map_loc[y][x] != col):
                    x = random.randint(0, self.longueur - 1)
                    y = random.randint(0, self.hauteur - 1)
                terr = mont
                map_loc[y][x] = terr
                ctt = ctt + 1
                ##        print("taille=",taille)
                tailleC = random.randint(1, max_number_of_mountains_per_group)
                for b in range(1, tailleC):
                    ct = 3
                    c = 0
                    caseadj = self.map_object.caseadjacente(x, y)
                    casediag = self.map_object.casediagonale(x, y)
                    while ct > 2 and c < 6:
                        ##                print("c=",c)
                        ct = 0
                        c = c + 1
                        co = random.randint(0, len(caseadj) - 1)
                        x1 = caseadj[co][0]
                        y1 = caseadj[co][1]
                        caseadj1 = self.map_object.caseadjacente(x1, y1)
                        for i in range(0, len(caseadj1)):
                            ##                    print("i=",i)
                            x2 = caseadj1[i][0]
                            y2 = caseadj1[i][1]
                            if (map_loc[y2][x2] == mont):
                                ct = ct + 1
                    ##                        print(ct)
                    co = random.randint(0, len(caseadj) - 1)
                    x1 = caseadj[co][0]
                    y1 = caseadj[co][1]
                    map_loc[y1][x1] = terr
                    ctt = ctt + 1
                    x = x1
                    y = y1
                    caseadj.clear()
        n = len(poss) * 2
        return map_loc


    def generate_seas(self):
        map_loc = self.map_object.map.copy()
        for j in range(0, self.hauteur):
            for i in range(0, self.longueur):
                if map_loc[j][i] == ocn:
                    caseadj = self.map_object.caseadjacente(i, j)
                    for b in range(0, len(caseadj)):
                        x1 = caseadj[b][0]
                        y1 = caseadj[b][1]
                        if map_loc[y1][x1] not in [ocn, mer]:
                            map_loc[j][i] = mer
        return map_loc


    def flatten(self):
        map_loc = self.map_object.map.copy()
        for j in range(0, self.hauteur):
            for i in range(0, self.longueur):
                if map_loc[j][i] in [ocn, mer]:
                    caseadj = self.map_object.caseadjacente(i, j)
                    ct = 0
                    x = 0
                    y = 0
                    for b in range(0, len(caseadj)):
                        x1 = caseadj[b][0]
                        y1 = caseadj[b][1]
                        if map_loc[y1][x1] in [pln, col, mont, neige, desert]:
                            ct = ct + 1
                            x = x1
                            y = y1
                    if ct == 3:
                        ran = []
                        for b in range(1, 6):
                            ran.append(map_loc[y][x])
                        ran.append(lac)
                        ran.append(marais)
                        rdn = random.randint(0, len(ran) - 1)
                        map_loc[j][i] = ran[rdn]
                    if ct == 4:
                        ran = []
                        for b in range(1, 10):
                            ran.append(map_loc[y][x])
                        ran.append(lac)
                        ran.append(marais)
                        rdn = random.randint(0, len(ran) - 1)
                        map_loc[j][i] = ran[rdn]
        return map_loc


    # ressource map
    def generate_resources_map(self):
        ctp = 0
        cto = 0
        mapr_loc = self.map_object.mapr.copy()
        if mapr_loc is None:
            mapr_loc = []
        map_loc = self.map_object.map.copy()
        for i in range(0, self.hauteur):
            mapr_loc.append([])
            for j in range(0, self.longueur):
                mapr_loc[i].append(0)
        for i in range(0, self.hauteur):
            for j in range(0, self.longueur):
                ran = []
                multi = random.randint(2, 5)
                for b in range(0, multi):
                    ran.append(ress_rie)
                if (map_loc[i][j] == ocn or map_loc[i][j] == mer):
                    cto = cto + 1
                    multi = random.randint(0, 1)
                    for b in range(0, multi):
                        ran.append(ress_poi)
                n = len(ran)
                v = random.randint(0, n - 1)
                if (ran[v] == ress_poi):
                    ctp = ctp + 1
                mapr_loc[i][j] = ran[v]
        if cto == 0:
            r = 0
        else:
            r = ctp / cto
        r = r * 100
        r = round(r, 2)
        print("ratio poisson =", r, "%")
        return mapr_loc