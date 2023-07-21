import time
import random
import noise
from parameters import *
from map_generator import MapGenerator


class MapGeneratorHeightmap(MapGenerator):

    def __init__(self):
        self.map_object = None
        
    
    def init_generator(self, map_object):
        self.map_object = map_object
        self.hauteur = self.map_object.hauteur
        self.longueur = self.map_object.longueur
        self.heightmap = self.generate_heightmap()

    def generate_heightmap(self):
        heightmap = []
        octaves = 8
        freq = 32 * octaves
        for i in range(0, self.hauteur):
            heightmap.append([])
            for j in range(0, self.longueur):
                heightmap[-1].append(noise.snoise2(j/freq, i/freq, octaves=octaves))
        # import matplotlib.pyplot as plt
        # plt.imshow(heightmap)
        # plt.show()
        # # print min and max of heightmap
        # print("min heightmap: ", min(map(min, heightmap)))
        # print("max heightmap: ", max(map(max, heightmap)))
        return heightmap


    def generate_lands(self):
        mapr_loc = self.map_object.map.copy()
        sea_level = -0.1
        for i in range(0, self.hauteur):
            for j in range(0, self.longueur):
                if self.heightmap[i][j] > sea_level:
                    mapr_loc[i][j] = terre
                else:
                    mapr_loc[i][j] = ocn
        return mapr_loc

    def generate_hills(self):
        mapr_loc = self.map_object.map.copy()
        hills_level = 0.33
        for i in range(0, self.hauteur):
            for j in range(0, self.longueur):
                if self.heightmap[i][j] > hills_level:
                    mapr_loc[i][j] = col
        return mapr_loc

    def generate_mountains(self):
        mapr_loc = self.map_object.map.copy()
        mountain_level = 0.5
        for i in range(0, self.hauteur):
            for j in range(0, self.longueur):
                if self.heightmap[i][j] > mountain_level:
                    mapr_loc[i][j] = mont
        return mapr_loc
