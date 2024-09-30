#coding: utf-8
"""
TP2 : Automate
Auteur : Anaëlle ROBIN
Date : 24/09/2024

TODO:
    Début de phrase = Majuscule
"""
import re #utilisé pour la fonction split

"""FONCTIONS"""

def lire_txt(fichiertxt):
    """
    Fonction qui lit un fichier texte et retourne une liste
    Variables :
        fichiertxt : str
    Sortie :
        liste : liste
    """
    with open(fichiertxt, 'r', encoding='utf-8') as fichier:
        liste = [ligne.strip() for ligne in fichier.readlines() if ligne.strip()] # Lire lignes et supprimer les espaces blancs
    return liste

def dico(fichiers):
    """
    Fonction qui crée un dictionnaire avec les types de mots
    Variables :
        fichiers : liste (de fichier txt)
    Sortie :
        dictionnaire_mots : dict (les clés sont les types de mot)
    """
    correspondance = {
        'articles.txt': 0,
        'adjectifs.txt': 1,
        'noms.txt': 2,
        'verbes.txt': 3,
        'noms_propre.txt': 4,
        'ponctuation.txt': 5
    }
    dictionnaire_mots = {}
    for i in fichiers:
        mots = lire_txt(i)
        for j in mots:
            dictionnaire_mots[j] = correspondance[i]
    return dictionnaire_mots

def analyse_de_phrase(phrase):
    """
    Fonction qui va analyser la phrase et vérifier si elle est juste ou non.
    Variables :
        phrase : liste (de chaine de caractere)
        etat : entier (de 0 à 9)
        type_de_mot : entier 
    Sortie :
        "Phrase incorrecte"
        "Phrase correcte"
        "Le mot {mot} n'est pas dans le dictionnaire."
    """
    phrase = re.findall(r'\w+|[.!?]',phrase) #split avec plusieurs séparateurs mais garde le point  
    etat = 0
    for mot in phrase:
        type_de_mot = dictionnaire_mots.get(mot)
        if type_de_mot is None:  #mot pas dans le dico
            print(f"Le mot {mot} n'est pas dans le dictionnaire.")
            ajouter_mot_dico(mot, dictionnaire_mots, fichiers)
            return "Fin de l'analyse"
        etat = table_de_transition[etat][type_de_mot]
        if etat == 8:
            return "Phrase incorrecte"
    if etat == 9:
        return "Phrase correcte"
    else :
        return "Phrase incorrecte"

def ajouter_mot_dico(mot,dictionnaire_mots,fichiers):
    """
    Fonction qui va ajouter un mot dans le dico
    Variables :
        ajouter_mot : str (oui / non)
    Sortie :
        "Le mot '{mot}' a été ajouté."
        "Le mot '{mot}' n'a pas été ajouté. Phrase incorrecte."
    """
    
    ajouter_mot="rien"
    while True:
        try :
            ajouter_mot = str(input("Voulez vous ajouter ce mot au dictionnaire ? (oui/non): "))
            if ajouter_mot == "oui":
                type_de_mot = demander_type_de_mot()
                fichier_d_ajout = rf"{fichiers[type_de_mot]}"
                with open(fichier_d_ajout, "a") as f:
                    f.write(f"{mot}\r\n")
                print(f"Le mot '{mot}' a été ajouté au fichier {fichiers[type_de_mot]}.")
                return
            elif ajouter_mot == "non":
                print(f"Le mot '{mot}' n'a pas été ajouté. Phrase incorrecte.")
                return
        except ValueError:
            print("Veuillez répondre par 'oui' ou 'non'.")

def demander_type_de_mot():
    """
    Fonction qui demande à l'utilisateur de spécifier le type de mot.
    Retourne :
        type_de_mot : entier
    """
    print("Quel est le type du mot ?")
    print("0 - article , \n1 - adjectif , \n2 - nom , \n3 - verbe , \n4 - nom propre , \n5 - ponctuation")
    while True:
        try:
            type_de_mot = int(input("Entrez le numéro correspondant au type de mot : "))
            if type_de_mot in range(6):  # S'assure que la valeur est entre 0 et 5
                return type_de_mot
            else:
                print("Veuillez entrer un nombre entre 0 et 5.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

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

fichiers = ['articles.txt', 'adjectifs.txt', 'noms.txt','verbes.txt', 'noms_propre.txt','ponctuation.txt']

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

"""TEST DU PROGRAMME"""

#print(analyse_de_phrase(phrases_a_tester_justes[7]))
Entree_phrase = str(input("Entrez votre phrase à vérifier : "))
print(analyse_de_phrase(Entree_phrase))
