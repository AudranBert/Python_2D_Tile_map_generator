import time
import random
from parameters import *
from map_generator import MapGenerator


class MapGeneratorHeightmap(MapGenerator):

    def __init__(self):
        self.map_object = None
        
    
    def init_generator(self, map_object):
        self.map_object = map_object
        self.hauteur = self.map_object.hauteur
        self.longueur = self.map_object.longueur

    def generate_heightmap(self):
        import noise
        heightmap = []
        octaves = 8
        freq = 32 * octaves
        for i in range(0, self.hauteur):
            heightmap.append([])
            for j in range(0, self.longueur):
                heightmap[-1].append(noise.snoise2(j/freq, i/freq, octaves=octaves))
        # plot the result
        
        # import matplotlib.pyplot as plt
        # plt.imshow(heightmap)
        # plt.show()
        return heightmap


    def generate_lands(self):
        heightmap = self.generate_heightmap()
        mapr_loc = self.map_object.map.copy()
        sea_level = 0.05
        for i in range(0, self.hauteur):
            for j in range(0, self.longueur):
                if heightmap[i][j] > sea_level:
                    mapr_loc[i][j] = terre
                else:
                    mapr_loc[i][j] = ocn
        return mapr_loc