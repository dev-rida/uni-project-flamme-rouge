from C_gestion_cartes import *
from B_initialisation_course import *

######### SECTION : DEPLACEMENT DES COUREURS #################
##############################################################


def le_plus_eloigne(dico_positions):
    max_case = -1
    epsilon = 0.5 #pour avantager les coureurs placés à droite
    max_joueur = ""
    for joueur in dico_positions:
        case = numero_de_case(joueur,dico_positions)
        if dico_positions[joueur][0] == "D":
            case += epsilon
        if case > max_case:
            max_joueur = joueur
            max_case = case
    return max_joueur


def le_moins_eloigne(dico_positions,positions_droite):
    min_case = len(positions_droite)
    epsilon = 0.5 #pour avantager les coureurs placés à droite
    min_joueur = ""
    for joueur in dico_positions:
        case = numero_de_case(joueur,dico_positions)
        if dico_positions[joueur][0] == "D":
            case += epsilon
        if case < min_case:
            min_joueur = joueur
            min_case = case
    return min_joueur


def tri_joueurs(dico_positions):
    copie_dico = dict(dico_positions)
    ordre_joueurs = []
    while len(copie_dico) > 0:
        prochain_joueur = le_plus_eloigne(copie_dico)
        ordre_joueurs.append(prochain_joueur)
        del copie_dico[prochain_joueur]
    return ordre_joueurs


def avancee_coureurs(nom_joueur, dico_positions, positions_droite, positions_gauche, distance):
    old_pos = dico_positions[nom_joueur]
    indice_pos_joueur = int(old_pos[1:])
    indice_cible = indice_pos_joueur + distance
    nouv_pos = ""

    if indice_cible < len(positions_droite) and indice_cible < len(positions_gauche):
        # si aucune position libre ni à droite ni à gauche, chercher les cases précédentes
        for i in range(indice_cible, indice_pos_joueur, -1):
            # vérifier s'il ya de la place à droite
            if positions_droite[i] == "__":
                nouv_pos = "D" + str(i)
                break
            # sinon, chercher à gauche
            elif positions_gauche[i] == "__":
                nouv_pos = "G" + str(i)
                break
        
        # supprimer la position précédente
        if old_pos[0] == 'D':
            positions_droite[int(old_pos[1:])] = "__"
        elif old_pos[0] == 'G':
            positions_gauche[int(old_pos[1:])] = "__"

        # ajouter la nouvelle position
        if nouv_pos[0] == 'D':
            positions_droite[int(nouv_pos[1:])] = nom_joueur
        elif nouv_pos[0] == 'G':
            positions_gauche[int(nouv_pos[1:])] = nom_joueur

        dico_positions[nom_joueur] = nouv_pos
    else:
        avancee_coureurs(nom_joueur, dico_positions, positions_droite, positions_gauche, distance-1)


def premiere_case_apres_arrivee(nb_lignes,taille_seg,terminus):
    route = ["__"] * (nb_lignes-1) * taille_seg # la route sans l'arrivée
    return len(route) + terminus # la case après le terminus


def test_victoire(nb_lignes, taille_seg, dico_positions, terminus):
    res = False # init booléen
    for j in dico_positions:
        if premiere_case_apres_arrivee(nb_lignes,taille_seg,terminus) <= int(dico_positions[j][1:]):
            res = True # un joueur a franchi la ligne d’arrivée
    return res


def tour_de_jeu_sans_effet(
        dico_positions, positions_droite, positions_gauche, dico_paquets, dico_defausses, configurations, affichage=False):
    if affichage is True:
        print("##### Début du tour #####")

    dico_choix = dict()
    ordre_joueurs = tri_joueurs(dico_positions)

    for j in ordre_joueurs: # choix des cartes pour chaque joueur et les ajouter au dictionnaire
        carte_choisi = choix_deplacement(j,dico_paquets,dico_defausses,configurations,affichage)
        print(f"Le joueur {j} se déplace de {carte_choisi}")
        dico_choix[j] = carte_choisi
    
    for p in ordre_joueurs: # faire déplacer les joueurs dans le bon ordre
        avancee_coureurs(p, dico_positions, positions_droite, positions_gauche, dico_choix[p])

    if affichage is True:
        print("##### Fin du tour #####")
