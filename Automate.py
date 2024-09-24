#coding: utf-8
"""
TP2 : Automate
Auteur : Anaëlle ROBIN
Date : 24/09/2024

TODO:
    spliter les points ou virgules (fonction qui sépare tout ?)
    voir pk ça ne fonctionne pas

"""
dictionnaire = {
    "le" : 0, "la" : 0, "chat" : 2, "souris" : 2, "martin" : 4,
    "mange" : 3, "la" : 0, "petite" : 1, "joli" : 1, "grosse" : 1,
    "bleu" : 1, "verte" : 1, "dort" : 3,"julie" : 4, "jean" : 4, "." : 5
}

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

def analyse_de_phrase(phrase):
    """
    Fonction qui va analyser la phrase et vérifier si elle est juste ou non.
    Variables :
        phrase : chaine de caractere puis liste (de mot)
        etat : entier (de 0 à 9)
        type_de_mot : entier 

    """
    phrase = phrase.split()
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

phrases_a_tester_justes = [
    "le joli chat mange .",
    "le ,joli chat; dort.", # OK car on ne prend pas en compte les séparateurs
    "la grosse souris verte mange le joli petite chat blanc.",
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

"""TEST DU PROGRAMME"""

print(analyse_de_phrase(phrases_a_tester_justes[1]))

    