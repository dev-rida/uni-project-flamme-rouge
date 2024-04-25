import pygame
import time
import os

#pygame.init()
pygame.font.init()
pygame.mixer.init()

NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
ROUGE = (250, 30, 30)
VERT = (80, 200, 50)
BLEU = (0, 80, 220)
TUR = (0,130,130)
BOR = (75,30,45)

def resolution():
    try:
        val = int(input("Sélectionner la taille de la fenêtre (1 pour SD / 2 pour HD) : "))
        if val <= 1:
            return 1
        elif val >= 2:
            return 1.4
    except:
        return 1

control = resolution()

LARG, LONG = 960*control, 540*control
LARG_CASE, LONG_CASE = 25*control, 25*control
TAILLE_FONT = int(20*control)

FEN = pygame.display.set_mode((LARG, LONG))
ICON = pygame.image.load(os.path.join("assets", "flamme-rouge.ico"))
FONT = pygame.font.Font(os.path.join("assets", "police_caractere.ttf"), TAILLE_FONT*3)
FONT2 = pygame.font.Font(os.path.join("assets", "police_caractere.ttf"), TAILLE_FONT)
FONT3 = pygame.font.Font(os.path.join("assets", "police_caractere.ttf"), TAILLE_FONT - TAILLE_FONT//4)
FONT4 = pygame.font.Font(os.path.join("assets", "police_caractere.ttf"), TAILLE_FONT//2)

APLAN = pygame.transform.scale(pygame.image.load(os.path.join("assets", "fond.png")),(LARG, LONG))
CITY = pygame.transform.scale(pygame.image.load(os.path.join("assets", "mode_city.jpg")),(LARG, LONG))
FORET = pygame.transform.scale(pygame.image.load(os.path.join("assets", "mode_foret.jpg")),(LARG, LONG))
DESERT = pygame.transform.scale(pygame.image.load(os.path.join("assets", "mode_desert.jpg")),(LARG, LONG))

START = pygame.transform.scale(pygame.image.load(os.path.join("assets", "start.png")),(LARG_CASE, LONG_CASE))
FINISH = pygame.transform.scale(pygame.image.load(os.path.join("assets", "finish.png")),(LARG_CASE-1, LONG_CASE-1))
CASEG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "route_gauche.png")),(LARG_CASE, LONG_CASE))
CASED = pygame.transform.scale(pygame.image.load(os.path.join("assets", "route_droite.png")),(LARG_CASE, LONG_CASE))
BOT_ALEA = pygame.transform.scale(pygame.image.load(os.path.join("assets", "coureur_alea.png")),(LARG_CASE/1.5, LONG_CASE/1.5))
BOT_IA = pygame.transform.scale(pygame.image.load(os.path.join("assets", "coureur_ia.png")),(LARG_CASE/1.5, LONG_CASE/1.5))
JOUEUR = pygame.transform.scale(pygame.image.load(os.path.join("assets", "coureur_manuel.png")),(LARG_CASE/1.5, LONG_CASE/1.5))

pygame.display.set_caption("La Flamme Rouge")
pygame.display.set_icon(ICON)


def dessine_ligne_droite(positions, dico_config, coord_x, coord_y, start, depart, finish, arrivee):
    for i in range(len(positions)):
        if i == start and depart == True:
            FEN.blit(CASED, (LARG_CASE + coord_x, coord_y + LARG_CASE))
            FEN.blit(START, (LARG_CASE + coord_x, coord_y + LARG_CASE - LARG_CASE/14))
            coord_x += LONG_CASE
        if i == finish and arrivee == True:
            FEN.blit(CASED, (LARG_CASE + coord_x, coord_y + LARG_CASE))
            FEN.blit(FINISH, (LARG_CASE + coord_x, coord_y + LARG_CASE))
            coord_x += LONG_CASE
        if positions[i] == "__":
            FEN.blit(CASED, (LARG_CASE + coord_x, coord_y + LARG_CASE))
            coord_x += LONG_CASE
        elif 'J' in positions[i]:
            FEN.blit(CASED, (LARG_CASE + coord_x, coord_y + LARG_CASE))
            if dico_config[positions[i]] == 'M':
                FEN.blit(JOUEUR, (LARG_CASE + coord_x, coord_y + LARG_CASE + LARG_CASE/6))
            elif dico_config[positions[i]] == 'I':
                FEN.blit(BOT_IA, (LARG_CASE + coord_x, coord_y + LARG_CASE + LARG_CASE/6))
            elif dico_config[positions[i]] == 'A':
                FEN.blit(BOT_ALEA, (LARG_CASE + coord_x, coord_y + LARG_CASE + LARG_CASE/6))
            coord_x += LONG_CASE

def dessine_ligne_gauche(positions, dico_config, coord_x, coord_y, start, depart, finish, arrivee):
    for i in range(len(positions)):
        if i == start and depart == True:
            FEN.blit(CASEG, (LARG_CASE + coord_x, coord_y))
            FEN.blit(START, (LARG_CASE + coord_x, coord_y))
            coord_x += LONG_CASE
        if i == finish and arrivee == True:
            FEN.blit(CASEG, (LARG_CASE + coord_x, coord_y))
            FEN.blit(FINISH, (LARG_CASE + coord_x, coord_y))
            coord_x += LONG_CASE
        if positions[i] == "__":
            FEN.blit(CASEG, (LARG_CASE + coord_x, coord_y))
            coord_x += LONG_CASE
        elif 'J' in positions[i]:
            FEN.blit(CASEG, (LARG_CASE + coord_x, coord_y))
            if dico_config[positions[i]] == 'M':
                FEN.blit(JOUEUR, (LARG_CASE + coord_x, coord_y + LARG_CASE/4))
            elif dico_config[positions[i]] == 'I':
                FEN.blit(BOT_IA, (LARG_CASE + coord_x, coord_y + LARG_CASE/4))
            elif dico_config[positions[i]] == 'A':
                FEN.blit(BOT_ALEA, (LARG_CASE + coord_x, coord_y + LARG_CASE/4))
            coord_x += LONG_CASE

def dessine_ligne_gauche_inverse(positions, dico_config, coord_x, coord_y):
    for i in range(len(positions)):
        if positions[i] == "__":
            FEN.blit(pygame.transform.flip(CASED, True, False), (LARG_CASE + coord_x, coord_y))
            coord_x -= LONG_CASE
        elif 'J' in positions[i]:
            FEN.blit(pygame.transform.flip(CASED, True, False), (LARG_CASE + coord_x, coord_y))
            if dico_config[positions[i]] == 'M':
                FEN.blit(pygame.transform.flip(JOUEUR, True, False), (LARG_CASE + coord_x, coord_y + LARG_CASE/6))
            elif dico_config[positions[i]] == 'I':
                FEN.blit(pygame.transform.flip(BOT_IA, True, False), (LARG_CASE + coord_x, coord_y + LARG_CASE/6))
            elif dico_config[positions[i]] == 'A':
                FEN.blit(pygame.transform.flip(BOT_ALEA, True, False), (LARG_CASE + coord_x, coord_y + LARG_CASE/6))
            coord_x -= LONG_CASE

def dessine_ligne_droite_inverse(positions, dico_config, coord_x, coord_y):
    for i in range(len(positions)):
        if positions[i] == "__":
            FEN.blit(pygame.transform.flip(CASEG, True, False), (LARG_CASE + coord_x, coord_y - LARG_CASE))
            coord_x -= LONG_CASE
        elif 'J' in positions[i]:
            FEN.blit(pygame.transform.flip(CASEG, True, False), (LARG_CASE + coord_x, coord_y - LARG_CASE))
            if dico_config[positions[i]] == 'M':
                FEN.blit(pygame.transform.flip(JOUEUR, True, False), (LARG_CASE + coord_x, coord_y - LARG_CASE + LARG_CASE/4))
            elif dico_config[positions[i]] == 'I':
                FEN.blit(pygame.transform.flip(BOT_IA, True, False), (LARG_CASE + coord_x, coord_y - LARG_CASE + LARG_CASE/4))
            elif dico_config[positions[i]] == 'A':
                FEN.blit(pygame.transform.flip(BOT_ALEA, True, False), (LARG_CASE + coord_x, coord_y - LARG_CASE + LARG_CASE/4))
            coord_x -= LONG_CASE


def dessine_route(positions_droite, positions_gauche, dico_config, point_x, point_y, start=5, depart=False, finish=12, arrivee=False):
    dessine_ligne_droite(positions_droite, dico_config, point_x, point_y, start, depart, finish, arrivee)
    dessine_ligne_gauche(positions_gauche, dico_config, point_x, point_y, start, depart, finish, arrivee)

def dessine_route_inverse(positions_droite, positions_gauche, dico_config, point_x, point_y):
    dessine_ligne_droite_inverse(positions_droite, dico_config, point_x, point_y)
    dessine_ligne_gauche_inverse(positions_gauche, dico_config, point_x, point_y)


def decoupage(liste, n):
    res = list()
    for i in range(0, len(liste), n):
        res.append(liste[i:i+n])
    return res

def dessine_circuit(positions_droite, positions_gauche, dico_config):
    nb_lignes, taille_seg = 4, 20
    pos_droite, pos_gauche = decoupage(positions_droite,taille_seg), decoupage(positions_gauche,taille_seg)
    point_x, point_y = LARG_CASE, LONG_CASE*2
    dessine_route(pos_droite[0], pos_gauche[0], dico_config, (point_x*2)-(LARG_CASE/2), point_y, depart=True)
    for n in range(1, nb_lignes):
        if n % 2 != 0:
            point_y += LONG_CASE*4
            dessine_route_inverse(pos_droite[n], pos_gauche[n], dico_config, point_x*(taille_seg+1), point_y)
        else:
            point_y += LONG_CASE*2
            dessine_route(pos_droite[n], pos_gauche[n], dico_config, point_x*2, point_y)
    point_y += LONG_CASE*2
    dessine_route(pos_droite[nb_lignes], pos_gauche[nb_lignes], dico_config, (point_x*2)-(LARG_CASE/2), point_y, arrivee=True)


def menu_config(dico_config = None):
    FEN.blit(APLAN, (0,0))
    FEN.blit(FONT2.render("Bienvenue sur l'étape 63 du Tour de France 2024 !", True, NOIR), (LARG/20, LONG/14))
    FEN.blit(FONT2.render("Veuillez saisir vos choix de configurations dans le terminal", True, NOIR), (LARG/20, LONG/4.2))
    FEN.blit(FONT2.render("Choix de la map du jeu : Saisir < V > pour ville, < F > pour fôret ou < D > pour désert", True, NOIR), (LARG/20, LONG/3))
    FEN.blit(FONT2.render("Choix des modes des joueurs : Saisir < A > pour aléatoire, < I > pour IA ou < M > pour manuel", True, NOIR), (LARG/20, LONG/2.5))
    FEN.blit(FONT4.render("POUR QUITTER LE JEU APPUYER SUR CTRL + C", True, ROUGE), (LARG - LARG/4, LONG/30))
    pygame.display.update()

    if isinstance(dico_config, dict):
        coord_y = LONG/1.8
        for j in dico_config:
            if dico_config[j] == 'M':
                FEN.blit(FONT2.render(str(j) + " est un coureur manuel !", True, TUR), (LARG/10, coord_y))
                coord_y += TAILLE_FONT*1.5
            elif dico_config[j] == 'I':
                FEN.blit(FONT2.render(str(j) + " est une IA !", True, BLEU), (LARG/10, coord_y))
                coord_y += TAILLE_FONT*1.5
            elif dico_config[j] == 'A':
                FEN.blit(FONT2.render(str(j) + " est un bot aléatoire !", True, BOR), (LARG/10, coord_y))
                coord_y += TAILLE_FONT*1.5
        pygame.display.update()
        time.sleep(5)


def compteur():
    coord_x = LARG_CASE*4
    for n in range(3,0,-1):
        FEN.blit(FONT.render(str(n), True, ROUGE), (coord_x, LONG - LONG/6))
        pygame.display.update()
        time.sleep(1)
        coord_x += LARG_CASE*3
    FEN.blit(FONT.render("GO!", True, VERT), (coord_x*1.3, LONG - LONG/6))
    pygame.display.update()

def fenetre_jeu(positions_droite, positions_gauche, dico_config, mode_jeu, compt=False):
    if mode_jeu == 'V':
        FEN.blit(CITY, (0,0))
    elif mode_jeu == 'F':
        FEN.blit(FORET, (0,0))
    elif mode_jeu == 'D':
        FEN.blit(DESERT, (0,0))
    dessine_circuit(positions_droite, positions_gauche, dico_config)
    pygame.display.update()
    if compt is True:
        compteur()

def vainqueur(resultat, deplacements):
    for n in range(1,5):
        if (n % 2 != 0):
            FEN.blit(FONT2.render(str(resultat) + " GAGNE AVEC " + str(deplacements) + " DEPLACEMENTS", True, NOIR), (LARG_CASE*5, LONG - LONG/4 + LONG_CASE*n))
        else:
            FEN.blit(FONT2.render(str(resultat) + " GAGNE AVEC " + str(deplacements) + " DEPLACEMENTS", True, BLANC), (LARG_CASE*6, LONG - LONG/4 + LONG_CASE*n))
    pygame.display.update()
    time.sleep(10)
