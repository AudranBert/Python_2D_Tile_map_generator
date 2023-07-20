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
        print("Erreur!")
        print(text, end='')
        quest = str(input(" ? "))
    return quest


# ini variable fixe
def question():
    print("Lecture, ecriture ou rien")
    fic = str(input("l,e,r : "))
    while (
        fic != 'r' and fic != 'e' and fic != 'l' and fic != 'lire' and fic != 'lecture' and fic != 'ecrire' and fic != 'ecriture' and fic != 'rien'):
        print("Erreur!")
        print("Lecture, ecriture ou rien")
        fic = str(input("l,e,r : "))
    return fic

# question ferme avec verif
def yesno(text):
    print(text, end='')
    qu = str(input(" : "))
    while (qu != "n" and qu != "o" and qu != "non" and qu != "oui"):
        print("Erreur")
        print(text, end='')
        qu = str(input(" : "))
    return qu

# taille map
def taille():
    print("Taille de votre map")
    strlongueur = str(input("Longueur : "))
    er = re.compile('\D')
    ter = er.match(strlongueur)
    while (ter):
        print("Erreur ce n'es pas un nombre !")
        strlongueur = str(input("Longueur : "))
        ter = er.match(strlongueur)
    longueur = int(strlongueur)
    strhauteur = str(input("Hauteur : "))
    er = re.compile('\D')
    ter = er.match(strhauteur)
    while (ter):
        print("Erreur ce n'es pas un nombre !")
        strhauteur = str(input("Hauteur : "))
        ter = er.match(strhauteur)
    hauteur = int(strhauteur)
    return longueur, hauteur