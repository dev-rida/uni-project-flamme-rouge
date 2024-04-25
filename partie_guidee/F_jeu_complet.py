from A_affichage_str import *
from E_phase_terminale import *
import tkinter as tk

#Affichage de l'entete du jeu dans la console
def entete(numero_etape = 12, depart = "Aurillac", arrivee = "Villeneuve-sur-Lot"):
    chaine = "#" * 100 + "\n"
    chaine += "#"*41 + " LA FLAMME ROUGE " + "#"*42 + "\n"
    chaine += "#" * 100 + "\n" + "\n"
    chaine += "Bienvenue sur l'étape " + str(numero_etape) + " "
    chaine += "du Tour de France 2024 reliant " + depart + " "
    chaine += "à " + arrivee + " ! Bonne chance !!!"
    chaine += "\n" + "\n"
    return chaine

#Affichage de la route dans une fenêtre graphique
def afficher_fenetre(chaine, taille_fen = '600x300+50+10'):
    fen = tk.Tk()
    fen.geometry(taille_fen)
    fen.title("La Flamme Rouge")
    bouton = tk.Button(fen, text="Tour suivant", command=fen.destroy)
    tk.Label(fen, text=chaine).pack()
    bouton.pack(side=tk.LEFT, padx=5, pady=5)
    fen.mainloop()

def partie_jeu(nb_joueurs,nb_lignes,taille_seg,start=4,terminus=10,affichage=False):
    print(entete(63, "Riom", "Issoire"))

    liste_joueurs = creer_liste_joueurs(nb_joueurs)
    positions_droite, positions_gauche = creer_listes_positions(nb_lignes, taille_seg)
    configurations = configurations_joueurs(liste_joueurs)

    initialiser_jeu_alea(liste_joueurs, positions_droite, positions_gauche, start)
    afficher_fenetre(affichage_route(nb_lignes, taille_seg, positions_droite, positions_gauche, start, terminus))

    dico_positions = construit_dico_positions(positions_droite, positions_gauche, start)
    dico_paquets = dico_paquets_initial(liste_joueurs)
    dico_defausses = dico_defausses_initial(liste_joueurs)

    while test_victoire(nb_lignes, taille_seg, dico_positions, terminus) is not True:
        tour_de_jeu(dico_positions, positions_droite, positions_gauche, dico_paquets, dico_defausses, configurations, affichage)
        afficher_fenetre(affichage_route(nb_lignes, taille_seg, positions_droite, positions_gauche, start, terminus))    
    
    print(f"Le vainqueur de l'étape est {le_plus_eloigne(dico_positions)} !!")
