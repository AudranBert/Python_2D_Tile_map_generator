import re

# question ouverte sans verif
def quest(text):
    print(text, end='')
    quest = str(input(" ? "))
    return quest


# question ouverte avec 6 verif
def quest_responses(text, V):
    print(text, end='')
    quest = str(input(" ? "))
    while (quest not in V):
        print("Error!")
        print(text, end='')
        quest = str(input(" ? "))
    return quest


# ini variable fixe
def question():
    print("Read, write, or nothing")
    fic = str(input("r,w,n : "))
    while (
        fic != 'r' and fic != 'w' and fic != 'n' and fic != 'read' and fic != 'write' and fic != 'nothing'):
        print("Error!")
        print("Read, write, or nothing")
        fic = str(input("r,w,n : "))
    return fic

# question ferme avec verif
def yesno(text):
    print(text, end='')
    qu = str(input(" : "))
    while (qu != "n" and qu != "y" and qu != "no" and qu != "yes"):
        print("Error")
        print(text, end='')
        qu = str(input(" : "))
    if (qu == "n" or qu == "no"):
        qu = False
    else:
        qu = True
    return qu

# taille map
def map_size():
    print("Size of the map")
    strlongueur = str(input("Lenght : "))
    er = re.compile('\D')
    ter = er.match(strlongueur)
    while (ter):
        print("This is not a number !")
        strlongueur = str(input("Lenght : "))
        ter = er.match(strlongueur)
    longueur = int(strlongueur)
    strhauteur = str(input("Height : "))
    er = re.compile('\D')
    ter = er.match(strhauteur)
    while (ter):
        print("This is not a number !")
        strhauteur = str(input("Height : "))
        ter = er.match(strhauteur)
    hauteur = int(strhauteur)
    return longueur, hauteur