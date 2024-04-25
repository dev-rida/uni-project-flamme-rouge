######### SECTION : AFFICHAGE DU JEU ##########
###############################################


def ligne_vers_droite(positions):
    aff = ">"  # debut de la ligne
    for e in positions:  # boucle for pour dessiner la ligne
        aff += " " + e + " |"
    return aff


def route_vers_droite(positions_droite, positions_gauche):
    aff = (ligne_vers_droite(positions_gauche) + "\n" + ligne_vers_droite(positions_droite))
    # variable pour afficher les deux slots
    return aff


def inverse(ligne):
    return ligne[:0:-1] + "<"


def route_vers_gauche(positions_droite, positions_gauche):
    aff = (inverse(ligne_vers_droite(positions_droite))+ "\n" + inverse(ligne_vers_droite(positions_gauche)))
    # variable pour afficher les deux slots inverse
    return aff


def ligne_depart(positions, start):
    aff = ">>>>>"  # debut de la ligne
    for e in range(len(positions)):  # boucle for pour dessiner la ligne
        if e == start - 1:
            aff += " " + positions[e] + " X"  # case depart
        else:
            aff += " " + positions[e] + " |"  # cases standards
    return aff


def route_depart(positions_droite, positions_gauche, start):
    aff = (ligne_depart(positions_gauche, start) + "\n" + ligne_depart(positions_droite, start))
    # variable pour afficher les slots
    return aff


def ligne_arrivee_vers_droite(positions, terminus):
    aff = ">"  # debut de la ligne
    for e in range(len(positions)):
        if e + 1 == terminus:
            aff += " " + positions[e] + " |XXXX|"  # ligne d'arrivée
        else:
            aff += " " + positions[e] + " |"  # cases standards
    return aff


def route_arrivee_vers_droite(positions_droite, positions_gauche, terminus):
    aff = (ligne_arrivee_vers_droite(positions_gauche, terminus) + "\n" + ligne_arrivee_vers_droite(positions_droite, terminus))
    # variable pour afficher les slots
    return aff


def route_arrivee_vers_gauche(positions_droite, positions_gauche, terminus):
    aff = (inverse(ligne_arrivee_vers_droite(positions_droite, terminus)) + "\n" + inverse(ligne_arrivee_vers_droite(positions_gauche, terminus)))
    # variable pour afficher les slots
    return aff


def affichage_route(nb_lignes, taille_seg, positions_droite, positions_gauche, start=4, terminus=10):
    def decoupage(lst, n):
        res = list()
        for i in range(0, len(lst), n): # boucle pour decouper la liste en parties egale
            res.append(lst[i:i+n])
        return res
    pos_droite,pos_gauche = decoupage(positions_droite,taille_seg),decoupage(positions_gauche,taille_seg) # taille voulue
    r = 0 # init var du while
    aff = route_depart(pos_droite[r], pos_gauche[r], start) + "\n\n"
    if nb_lignes > 2: # test nb lignes
        while r < (nb_lignes-2): # boucle pour alterner route droite/gauche
            if r % 2 == 0: # test parite pour route
                aff += route_vers_gauche(pos_droite[r+1], pos_gauche[r+1]) + "\n\n"
            else:
                aff += route_vers_droite(pos_droite[r+1], pos_gauche[r+1]) + "\n\n"
            r += 1
    if r % 2 == 0: # test parite pour arrivee
        aff += route_arrivee_vers_gauche(pos_droite[r+1], pos_gauche[r+1], terminus)
    else:
        aff += route_arrivee_vers_droite(pos_droite[r+1], pos_gauche[r+1], terminus)
    return aff # renvoie la route finale
