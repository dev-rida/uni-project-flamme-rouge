from D_deplacement_coureurs import *

######### SECTION : PHASE TERMINALE DU JEU #################
##############################################################


def distribution_fatigue(dico_positions, positions_droite,dico_defausses):
    try:
        for joueur in dico_positions:
            indice = numero_de_case(joueur, dico_positions) # indice de la case devant le joueur
            if positions_droite[indice + 1] == "__" and positions_droite[indice + 2] == "__":
                dico_defausses[joueur].append(2) # ajouter carte fatigue
    except:
        pass


def groupes_coureurs(dico_positions,positions_droite,positions_gauche):
    joueur_min = le_moins_eloigne(dico_positions,positions_droite)
    joueur_max = le_plus_eloigne(dico_positions)
    case_min = numero_de_case(joueur_min,dico_positions)
    case_max = numero_de_case(joueur_max,dico_positions)
    i = case_min
    liste_groupes = []
    while i <= case_max:
        groupe = []
        droite_i = positions_droite[i]
        gauche_i = positions_gauche[i]
        while droite_i != "__":
            if gauche_i != "__":
                groupe.append(gauche_i)
            groupe.append(droite_i)
            i += 1
            droite_i = positions_droite[i]
            gauche_i = positions_gauche[i]
        if len(groupe) > 0:
            liste_groupes.append(groupe)
        i += 1
    return liste_groupes


def decale_coureurs(groupe,dico_positions,positions_droite,positions_gauche):
    for joueur in reversed(groupe): # parcourir le groupe dans le sens inverse
        avancee_coureurs(joueur,dico_positions,positions_droite, positions_gauche, 1)


def aspiration(dico_positions,positions_droite,positions_gauche):
    liste_groupes = groupes_coureurs(dico_positions,positions_droite,positions_gauche)
    n, nb_grp = 0, len(liste_groupes)
    phrase = ""
    
    while (n < nb_grp-1):
        joueur_derriere = liste_groupes[n][-1] # le premier joueur du groupe aspiré
        joueur_devant = liste_groupes[n+1][0] # le dernier joueur du groupe suivant
        p1 = int(dico_positions[joueur_derriere][1:])
        p2 = int(dico_positions[joueur_devant][1:])

        if (p2-p1 == 2): # test : une case vide
            if phrase == "":
                phrase = "Le groupe " + str(liste_groupes[n]) + " a été aspirer par le groupe " + str(liste_groupes[n+1])
            else:
                phrase += ("\n" + "Le groupe " + str(liste_groupes[n]) + " a été aspirer par le groupe " + str(liste_groupes[n+1]))
            
            decale_coureurs(liste_groupes[n],dico_positions,positions_droite,positions_gauche)
            liste_groupes = groupes_coureurs(dico_positions,positions_droite,positions_gauche)
            nb_grp -= 1 # un groupe en moins
        else:
            n += 1 # incrementation du compteur pour traiter les groupes suivants
    return phrase


def tour_de_jeu(
        dico_positions,positions_droite,positions_gauche,dico_paquets,dico_defausses,configurations,
        nb_lignes,taille_seg,terminus,affichage=False):
    if affichage is True:
        print("##### Début du tour #####")

    dico_choix = dict()
    ordre_joueurs = tri_joueurs(dico_positions)
    gagnant = ""

    for j in ordre_joueurs: # choix des cartes pour chaque joueur et les ajouter au dictionnaire
        carte_choisi = choix_deplacement(j,dico_paquets,dico_defausses,configurations,dico_positions,affichage)
        print(f"Le joueur {j} se déplace de {carte_choisi}")
        dico_choix[j] = carte_choisi
    
    for p in ordre_joueurs: # faire déplacer les joueurs dans le bon ordre
        avancee_coureurs(p, dico_positions, positions_droite, positions_gauche, dico_choix[p])
        if test_victoire(nb_lignes,taille_seg,dico_positions,terminus) == True and gagnant == "":
            gagnant = p
    
    distribution_fatigue(dico_positions, positions_droite,dico_defausses)
    if gagnant == "": # pour éviter un bug dans groupe_coureurs
        phrase = aspiration(dico_positions,positions_droite,positions_gauche)
        if phrase != "":
            print(phrase)

    if affichage is True:
        print("##### Fin du tour #####")

    return gagnant
