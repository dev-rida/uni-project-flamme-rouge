from affichage_jeu import *
from phase_terminale import *

def lire_fichier_son(playlist, numero):
    pygame.mixer.music.load(os.path.join("assets", playlist[numero]))
    pygame.mixer.music.play(-1)

nb_joueurs, nb_lignes, taille_seg, start, terminus = 6, 5, 20, 5, 12

playlist_city = ["musique-menu.mp3", "musique-course1.mp3"]
playlist_foret = ["musique-menu.mp3", "musique-course2.mp3"]
playlist_desert = ["musique-menu.mp3", "musique-course3.mp3"]

liste_joueurs = creer_liste_joueurs(nb_joueurs)
positions_droite, positions_gauche = creer_listes_positions(nb_lignes, taille_seg)

menu_config()
lire_fichier_son(playlist_city, 0)
mode_jeu = choix_mode_jeu()
configurations = configurations_joueurs(liste_joueurs)
menu_config(configurations)

initialiser_jeu_alea(liste_joueurs, positions_droite, positions_gauche, start)

dico_positions = construit_dico_positions(positions_droite, positions_gauche, start)
dico_paquets = dico_paquets_initial(liste_joueurs)
dico_defausses = dico_defausses_initial(liste_joueurs)

pygame.mixer.music.fadeout(2000)

if mode_jeu == "V":
    lire_fichier_son(playlist_city, 1)
elif mode_jeu == "F":
    lire_fichier_son(playlist_foret, 1)
elif mode_jeu == "D":
    lire_fichier_son(playlist_desert, 1)

fenetre_jeu(positions_droite, positions_gauche, configurations, mode_jeu, True)
nb_deplacement = 0
        
while test_victoire(nb_lignes, taille_seg, dico_positions, terminus) is not True:
    res_jeu = tour_de_jeu(dico_positions, positions_droite, positions_gauche, dico_paquets, dico_defausses, configurations, nb_lignes, taille_seg, terminus)
    fenetre_jeu(positions_droite, positions_gauche, configurations, mode_jeu)
    nb_deplacement += 1

pygame.mixer.music.fadeout(8000)        
vainqueur(res_jeu, nb_deplacement)

pygame.quit()