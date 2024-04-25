from random import *
from B_initialisation_course import numero_de_case

######### SECTION : GESTION DES CARTES #################
########################################################


def paquet_initial():
    # ce paquet est initialement prévu pour une partie à 5 lignes,
    # des segments de 20 cases, un start = 4 et terminus = 10
    return [2] * 3 + [3] * 3 + [4] * 3 + [5] * 3 + [6] * 3 + [9] * 3


def dico_paquets_initial(liste_joueurs):
    dico = {}
    for j in liste_joueurs: # ajouter les paquets initials à chaque joueurs
        paquet = paquet_initial()
        shuffle(paquet) # melanger le paquet
        dico[j] = paquet
    return dico


def dico_defausses_initial(liste_joueurs):
    dico = {}
    for joueur in liste_joueurs: # ajouter les défausses initiales à chaque joueurs
        dico[joueur] = []
    return dico


def configurations_joueurs(liste_joueurs):
    dico = {}
    
    for j in liste_joueurs:
        config = input(f"Choisir un mode pour {j} ? Saisir A (pour Aléatoire), I (pour IA) ou M (pour Manuel) : ").upper()
        while config not in ["A", "M", "I"]: # redemander une saisie à l'utilisateur
            config = input(f"Recommencez! Choisir un mode pour {j} ? Saisir A (pour Aléatoire), I (pour IA) ou M (pour Manuel) : ").upper()
        dico[j]= config # ajout de la config au dict

    print("Choix des configurations effectué !")
    return dico


def maxdeux(liste):
    liste2 = [x for x in liste if x < max(liste)]
    if liste2 == []:
        liste2.extend(liste)
    return max(liste2)

def choix_carte_max(main_joueur, nom_joueur, dico_positions):
    indice_joueur = numero_de_case(nom_joueur,dico_positions)
    maxi = indice_joueur
    for joueur in dico_positions:
        if joueur != nom_joueur:
            indice = numero_de_case(joueur,dico_positions)
            if maxi < indice:
                maxi = indice
    if indice_joueur <= maxi:
        return max(main_joueur)
    elif indice_joueur > 75:
        return max(main_joueur)
    else:
        return maxdeux(main_joueur)

def choix_carte_alea(main_joueur):
    return choice(main_joueur)


def choix_carte_manuel(nom_joueur, main_joueur):
    try:
        choix = int(input(f"Quel déplacement pour {nom_joueur} souhaitez-vous effectuer {main_joueur} ? "))
        while choix not in main_joueur: # redemander une saisie à l'utilisateur
            choix = int(input(f"Recommencez! Quel déplacement pour {nom_joueur} souhaitez-vous effectuer {main_joueur} ? "))
        return choix
    except:
        print("Erreur de saisie, choix par défault.")
        return min(main_joueur)


def pioche_main_joueur(nom_joueur, dico_paquets, dico_defausses):
    elem = list() # liste vide represente la main du joueur 

    if len(dico_paquets[nom_joueur]) >= 4: # cas n1
        elem = list(dico_paquets[nom_joueur][0:4]) # ajout des cartes à la main
        for e in dico_paquets[nom_joueur][0:4]: # parcourir la liste paquets pour enlever les cartes ajoutés à la main
            dico_paquets[nom_joueur].remove(e)
    else: # cas n2
        elem = list(dico_paquets[nom_joueur]) # ajout des cartes à la main
        leng = 4 - len(elem) # carte(s) restante(s) à ajouté(s)
        dico_paquets[nom_joueur].clear()

        shuffle(dico_defausses[nom_joueur]) # mélange des cartes défausses
        dico_paquets[nom_joueur] = list(dico_defausses[nom_joueur]) # ajout des cartes au paquets du joueurs
        dico_defausses[nom_joueur].clear() # on vide la liste défausses

        if len(dico_paquets[nom_joueur]) < leng: # cas : bug rare
            elem.extend(dico_paquets[nom_joueur])
            while len(elem) < 4: # on ajoute le nombres de cartes manquantes
                elem.append(2)
        else:
            elem.extend(dico_paquets[nom_joueur][0:leng]) # ajout carte(s) manquante(s) à la main 
            for e in dico_paquets[nom_joueur][0:leng]: # parcourir la liste paquets pour enlever les cartes ajoutés à la main
                dico_paquets[nom_joueur].remove(e)
    return elem


def selection_carte_main(nom_joueur, main_joueur, choix, dico_defausses):
    nbrep = main_joueur.count(choix) # nb apparition de la carte dans la main
    for e in main_joueur: # parcourir la main pour ajouter les autres élements dans défausses
        if e != choix:
            dico_defausses[nom_joueur].append(e)
    if nbrep > 1:
        for c in range(nbrep-1): # cas où choix apparait plusieurs fois dans la main
            dico_defausses[nom_joueur].append(choix)


def choix_deplacement(nom_joueur,dico_paquets,dico_defausses,configurations,dico_positions,affichage=False):
    main_joueur = pioche_main_joueur(nom_joueur, dico_paquets, dico_defausses)
    if configurations[nom_joueur]=="I": # condition : IA, aléatoire ou manuel
        choix = choix_carte_max(main_joueur,nom_joueur,dico_positions)
    elif configurations[nom_joueur]=="A":
        choix = choix_carte_alea(main_joueur)
    else:
        choix = choix_carte_manuel(nom_joueur,main_joueur)
    selection_carte_main(nom_joueur, main_joueur, choix, dico_defausses) # update défausses
    if affichage == True:
        print(f"Le paquet de {nom_joueur} contient : {dico_paquets[nom_joueur]}")
        print(f"La defausse de {nom_joueur} contient : {dico_defausses[nom_joueur]}")
    return choix
