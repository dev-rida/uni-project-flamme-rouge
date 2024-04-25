from random import *

######### SECTION : INITIALISATION DE LA COURSE ##########
##########################################################


def creer_liste_joueurs(nb_joueurs):
    liste=[] # creation liste vide
    if nb_joueurs > 0: 
        for i in range(nb_joueurs): # boucle pour creer les elements de la liste
            liste.append("J"+str(i))
    return liste # resultat liste joueurs


def creer_listes_positions(nb_lignes,taille_seg):
    return ["__"]*nb_lignes*taille_seg, ["__"]*nb_lignes*taille_seg # renvoie deux listes de tailles nb_lignes*taille_seg


def placer_joueur_alea(position_dispos):
    pos = choice(position_dispos) # prend une position aleatoire dans la liste
    position_dispos.remove(pos) # enleve la position selectionée de la liste 
    return pos


def initialiser_jeu_alea(liste_joueurs, positions_droite, positions_gauche, start):
    lst_dispo = list() #creation liste vide
    for i in range(start): #remplissage de la liste 
        lst_dispo.extend(["D" + str(i),"G" + str(i)])
    for j in liste_joueurs: # parcourir la liste des joueurs
        pos = placer_joueur_alea(lst_dispo)  
        dg = pos[0] # cote gauche ou droite
        entier = int(pos[1:]) # numero de la case
        if dg == 'D':
            positions_droite[entier] = j #positionement des joueurs à droite
        elif dg == 'G':
            positions_gauche[entier] = j #positionement des joueurs à gauche


def construit_dico_positions(positions_droite,positions_gauche,start):
    dico = {} # creation dictionnaire vide
    for i in range(start): # parcourir liste jusquà start
        if 'J' in positions_droite[i]:
            dico[positions_droite[i]] = "D" + str(i) #ajout des clés des positions droite
        if 'J' in positions_gauche[i]:
            dico[positions_gauche[i]] = "G" + str(i) #ajout des clés des positions gauche
    return dico


def numero_de_case(nom_joueur,dico_positions):
    return int(dico_positions[nom_joueur][1:])


def choix_mode_jeu():
    config = input(f"Choisir une map ? ").upper()
    while config not in ["V", "F", "D"]: # redemander une saisie à l'utilisateur
        config = input(f"Recommencez! Choisir une map ? ").upper()
    return config
