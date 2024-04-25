from F_jeu_complet import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #############################################
    ####### Tests A_affichage_str #######
    #############################################

    # print(ligne_vers_droite(["A", "A", "B", "C", "D"]))
    # print(ligne_vers_droite(["__"]*15))
    # print(route_vers_droite(["A", "A", "B", "C", "D"],["A", "A", "B", "C", "G"]))
    # print(route_vers_droite(["__"]*15,["__"]*15))
    # print(route_vers_gauche(["A", "A", "B", "C", "D"],["A", "A", "B", "C", "G"]))
    # print(ligne_depart(["__"]*15,start = 8))
    # print(ligne_depart(["__"]*15))
    # print(route_depart(["__"]*14 + ["D_"],["__"]*14 + ["G_"], 4))
    # print(ligne_arrivee_vers_droite(["__"]*8 + ["J2"] + ["__"]*6, 10))
    # print(ligne_arrivee_vers_droite(["__"] * 8 + ["J2"] + ["__"] * 6,8))
    # print(route_arrivee_vers_droite(["__"] * 8 + ["J2"] + ["__"] * 6, ["__"] * 6 + ["J4"] + ["__"] * 8,8))
    # print(route_arrivee_vers_gauche(["__"] * 8 + ["J2"] + ["__"] * 6, ["__"] * 6 + ["J4"] + ["__"] * 8, 8))
    #
    # print(affichage_route(4,15,["__"]*60,["AA"]*60))
    # print(affichage_route(3, 20, ["__"] * 60, ["AA"] * 60))

    #############################################
    ####### Tests B_initialisation_course #######
    #############################################

    # print(creer_liste_joueurs(5))
    # print(creer_listes_positions(3,5)[0])
    # print("nombre de cases :", len(creer_listes_positions(3, 5)[1]))
    #
    # l = ["G0","G1","D0","D1"]
    # j = placer_joueur_alea(l)
    # print("vérification (True):", j in ["G0","G1","D0","D1"])
    # print("vérification 2 (False):", j in l)
    #
    # joueurs = creer_liste_joueurs(4)
    # positions_droite, positions_gauche = creer_listes_positions(2,15)
    # initialiser_jeu_alea(joueurs, positions_droite, positions_gauche, 4)
    # print(affichage_route(2,15,positions_droite,positions_gauche))
    #
    # print(construit_dico_positions(["__","J2","__","J0"],["__","__","J1","__"],4))


    #############################################
    ####### Tests C_gestion_cartes #######
    #############################################

    # print(dico_paquets_initial(["J0","J1"]))
    #
    # print(configurations_joueurs(["J0","J1","J2","J3"]))
    #
    # print(choix_carte_alea([2, 9, 3, 5]))
    # print(choix_carte_alea([2, 9, 3, 5]))
    # print(choix_carte_alea([2, 9, 3, 5]))
    # print(choix_carte_manuel("J2",[2, 9, 3, 5]))
    #
    # dico_paquets = {"J0" : [2,5,6,9,3,3,2], "J1" : [2,6,4]}
    # dico_defausses = {"J0" : [2,2,3,4], "J1" : [9,3,2,2,5,2,5,3,9]}
    # print("Main J0 :", pioche_main_joueur("J0",dico_paquets,dico_defausses))
    # print("Main J1 :", pioche_main_joueur("J1",dico_paquets,dico_defausses))
    # print("Paquet J0 :", dico_paquets["J0"])
    # print("Paquet J1 :", dico_paquets["J1"])
    # print("Defausse J1 :", dico_defausses["J1"])
    #
    # dico_paquets = {"J0": [2, 5, 6, 9, 3, 3, 2], "J1": [2, 6, 4, 2, 5]}
    # dico_defausses = {"J0": [2, 2, 3, 4], "J1": [9, 3, 2, 2, 5, 3, 9]}
    # c = choix_deplacement("J1", dico_paquets, dico_defausses, {"J0": "A", "J1": "M"}, affichage=True)
    # print("Carte déplacement choisie :", c)
    #
    # dico_paquets = {"J0" : [2,5,6,9,3,3,2], "J1" : [2,6,4]}
    # dico_defausses = {"J0" : [2,2,3,4], "J1" : [9,3,2,2,5,2,5,3,9]}
    # print(choix_deplacement("J1",dico_paquets,dico_defausses,{"J0": "A", "J1":"M"},affichage = True))

    #############################################
    ####### Tests D_deplacement_coureurs #######
    #############################################

    ####Bloc de test #1 pour avancee_coureurs
    # positions_droite = ["__"]*60
    # positions_gauche = ["__"]*60
    # dico_positions = {"J0" : "D31", "J1" : "D32", "J2" : "G35","J3" : "D35"}
    # positions_droite[31] = "J0"
    # positions_droite[32] = "J1"
    # positions_gauche[35] = "J2"
    # positions_droite[35] = "J3"
    # print(affichage_route(4, 15, positions_droite, positions_gauche))
    # avancee_coureur("J0", dico_positions,positions_droite,positions_gauche,3)
    # print(affichage_route(4,15,positions_droite,positions_gauche))

    ####Bloc de test #2 pour avancee_coureurs
    # positions_droite = ["__"]*60
    # positions_gauche = ["__"]*60
    # dico_positions = {"J0" : "D31", "J1" : "D32", "J2" : "G34","J3" : "D34"}
    # positions_droite[31] = "J0"
    # positions_droite[32] = "J1"
    # positions_gauche[34] = "J2"
    # positions_droite[34] = "J3"
    # print(affichage_route(4, 15, positions_droite, positions_gauche))
    # avancee_coureur("J0", dico_positions,positions_droite,positions_gauche,3)
    # print(affichage_route(4,15,positions_droite,positions_gauche))

    ####Bloc de test #3 pour avancee_coureurs
    # positions_droite = ["__"]*60
    # positions_gauche = ["__"]*60
    # dico_positions = {"J0" : "D31", "J1" : "D33", "J2" : "G34","J3" : "D34","J4" : "G33", "J5" : "D32"}
    # positions_droite[31] = "J0"
    # positions_droite[32] = "J5"
    # positions_gauche[33] = "J4"
    # positions_droite[33] = "J1"
    # positions_gauche[34] = "J2"
    # positions_droite[34] = "J3"
    # print(affichage_route(4, 15, positions_droite, positions_gauche))
    # avancee_coureur("J0", dico_positions,positions_droite,positions_gauche,3)
    # print(affichage_route(4,15,positions_droite,positions_gauche))

    # print(premiere_case_apres_arrivee(4,15,10))
    #
    # print(test_victoire(4,15,{"J0" : "D55"},terminus = 10))
    # print(test_victoire(4, 15, {"J0": "D55"}, terminus=11))


    #############################################
    ####### Tests E_phase_terminale #######
    #############################################

    # dico_defausses = {"J0" : [6,4], "J1" : [3]}
    # positions_droite = ["__"]*60
    # positions_droite[24] = "J0"
    # positions_droite[25] = "J1"
    # distribution_fatigue({"J0" : "D24", "J1" : "D25"},positions_droite,dico_defausses)
    # print(dico_defausses)
    #
    # positions_droite = ["__"]*60
    # positions_gauche = ["__"]*60
    # positions_droite[23] = "J3"
    # positions_droite[24] = "J0"
    # positions_gauche[24] = "J2"
    # positions_droite[26] = "J1"
    # dico_positions = {"J0" : "D24", "J1" : "D26", "J2" : "G24", "J3" : "D23"}
    # print(affichage_route(4,15,positions_droite,positions_gauche))
    # aspiration(dico_positions,positions_droite,positions_gauche)
    # print(affichage_route(4, 15, positions_droite, positions_gauche))

    #############################################
    ####### Tests F_jeu_complet #######
    #############################################

    # partie_jeu(6,5,20,affichage = True)

    print()
