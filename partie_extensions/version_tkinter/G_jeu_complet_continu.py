import time
import tkinter as tk
from threading import *
from A_affichage_str import *
from E_phase_terminale import *

def entete(numero_etape = 12, depart = "Aurillac", arrivee = "Villeneuve-sur-Lot"):
    chaine = "#" * 100 + "\n"
    chaine += "#"*41 + " LA FLAMME ROUGE " + "#"*42 + "\n"
    chaine += "#" * 100 + "\n" + "\n"
    chaine += "Bienvenue sur l'étape " + str(numero_etape) + " "
    chaine += "du Tour de France 2024 reliant " + depart + " "
    chaine += "à " + arrivee + " ! Bonne chance !!!"
    chaine += "\n" + "\n"
    return chaine

def partie_jeu_graphique(nb_joueurs,nb_lignes,taille_seg,start = 4,terminus = 10):
    fen = tk.Tk()
    fen.geometry('960x540')
    fen.title("La Flamme Rouge")
    label = tk.Label(fen, text="L'étape va bientôt commencer !!")
    label.pack()
    bouton = tk.Button(fen, text="Commencer la partie !", command=lambda: jeu_thread(nb_joueurs, nb_lignes, taille_seg, label, bouton, fen, start, terminus))
    bouton.pack(side=tk.BOTTOM, padx=10, pady=10)
    fen.mainloop()

def jeu_thread(nb_joueurs, nb_lignes, taille_seg, label, bouton, fen, start = 4, terminus = 10):
    Thread(target=lancer_jeu_graphique, args = (nb_joueurs,nb_lignes,taille_seg,label,bouton,fen,start,terminus)).start()

def lancer_jeu_graphique(nb_joueurs,nb_lignes,taille_seg,label,bouton,fen,start = 4,terminus = 10):
    bouton.pack_forget()
    print(entete(63, "Riom", "Issoire"))

    positions_droite, positions_gauche = creer_listes_positions(nb_lignes,taille_seg)
    liste_joueurs = creer_liste_joueurs(nb_joueurs)
    configurations = configurations_joueurs(liste_joueurs)

    initialiser_jeu_alea(liste_joueurs,positions_droite,positions_gauche,start)

    dico_positions = construit_dico_positions(positions_droite,positions_gauche,start)
    dico_paquets = dico_paquets_initial(liste_joueurs)
    dico_defausses = dico_defausses_initial(liste_joueurs)

    label.config(text = affichage_route(nb_lignes, taille_seg, positions_droite, positions_gauche, start, terminus))
    delay = 3
    res_jeu = 0
    deplacements = 0

    while not test_victoire(nb_lignes,taille_seg,dico_positions,terminus):
        time.sleep(delay)
        res_jeu = tour_de_jeu(dico_positions, positions_droite, positions_gauche, dico_paquets, dico_defausses, configurations, nb_lignes, taille_seg, terminus, True)
        label.config(text = affichage_route(nb_lignes, taille_seg, positions_droite, positions_gauche, start, terminus))
        deplacements += 1
        delay = 1

    print(f"Le vainqueur de l'étape est {res_jeu} avec {deplacements} déplacements !!")

    bouton.config(text = "Quitter", command = fen.destroy)
    bouton.pack()

if __name__ == "__main__":
    partie_jeu_graphique(6,5,20,5,12)