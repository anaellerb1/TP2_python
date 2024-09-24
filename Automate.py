#coding: utf-8
"""
TP2 : Automate
Auteur : Anaëlle ROBIN
Date : 24/09/2024

TODO:
    Début de phrase = Majuscule
"""
import re #utilisé pour la fonction split
import adjectifs.txt,articles.txt,noms.txt,verbes.txt,noms_propre.txt

"""DICO & LISTES"""

dictionnaire_originel = {
    "le" : 0, "la" : 0, "chat" : 2, "souris" : 2, "martin" : 4,
    "mange" : 3, "la" : 0, "petite" : 1, "joli" : 1, "grosse" : 1,
    "bleu" : 1, "verte" : 1, "dort" : 3,"Julie" : 4, "Jean" : 4, 
    "." : 5,"!" : 5,"?" : 5
}

phrases_a_tester_justes = [
    "le joli chat mange .",
    "le ,joli chat; dort.", # OK car on ne prend pas en compte les séparateurs
    "la grosse souris verte mange le joli petite chat.",
    "la grosse souris verte mange jean.",
    "Jean dort.",
    "Jean mange Martin.",
    "Jean mange le chat.",
    "la verte souris grosse petit mange le bleu verte chat petite."
]

phrases_a_tester_fausses = [
    ".", # ne commence pas par article
    "", # chaîne vide
    "le joli chat joue", # pas ’.’ final
    "le joli chat joue." # ’joue’ inconnu
]

fichiers = ['articles.txt', 'adjectifs.txt', 'noms.txt','verbes.txt', 'noms_propre.txt',ponctuation]

ponctuation = ['.','!','?']

table_de_transition=[
    [1,8,8,8,4,8], #etat 0
    [8,1,2,8,8,8], #etat 1
    [8,2,8,3,8,8], #etat 2
    [5,8,8,8,7,9], #etat 3
    [8,8,8,3,8,8], #etat 4
    [8,5,6,8,8,8], #etat 5
    [8,6,8,8,8,9], #etat 6
    [8,8,8,8,8,9]  #etat 7
    #[8,8,8,8,8,8]  #etat 8 : pas de transition tjrs le meme etat
    #[9,9,9,9,9,9]  #etat 9 : pas de transition tjrs le meme etat
]

dictionnaire_mots = dico(fichiers)

"""FONCTIONS"""

def lire_txt(fichiertxt):
    with open(fichiertxt, 'r', encoding='utf-8') as fichier:
        liste = [ligne.strip() for ligne in fichier.readlines() if ligne.strip()] # Lire lignes et supprimer les espaces blancs
    return liste

def dico(fichiers):
    dictionnaire_mots = {}
    for i in fichiers:
        mots = lire_txt(i)
        for j in mots:
            dictionnaire_mots[j] = i
    return dictionnaire_mots

def analyse_de_phrase(phrase):
    """
    Fonction qui va analyser la phrase et vérifier si elle est juste ou non.
    Variables :
        phrase : liste (de chaine de caractere)
        etat : entier (de 0 à 9)
        type_de_mot : entier 

    """

    phrase = re.findall(r'\w+|[.!?]',phrase) #split avec plusieurs séparateurs mais garde le point  
    etat = 0
    for mot in phrase:
        type_de_mot = dictionnaire.get(mot,6) #.get permet de chercher le mot dans le dico et de renvoyer "8" si il ne trouve pas
        if type_de_mot == 6:
            return f"Le mot {mot} n'est pas dans le dictionnaire."
        etat = table_de_transition[etat][type_de_mot]
        if etat == 8:
            return "Phrase incorrecte"
    if etat == 9:
        return "Phrase correcte"
    else :
        return "Phrase incorrecte"

"""TEST DU PROGRAMME"""

#print(analyse_de_phrase(phrases_a_tester_justes[7]))
Entree_phrase = str(input("Entrez votre phrase à vérifier : "))
print(analyse_de_phrase(Entree_phrase))
