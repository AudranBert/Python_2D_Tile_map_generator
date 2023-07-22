
def print_map(map_object):
    print("\n Map : ")
    for i in range(0, map_object.hauteur):
        for j in range(0, map_object.longueur):
            print(map_object.map[i][j], '| ', end='')
        print('')
    print('')


def print_resources_map(map_object):
    print("\n Resources map : ")
    for i in range(0, map_object.hauteur):
        for j in range(0, map_object.longueur):
            print(map_object.mapr[i][j], '| ', end='')
        print('')
    print('')