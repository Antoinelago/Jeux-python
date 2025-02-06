# Créé par ANTOINE, le 08/12/2023 en Python 3.7
import pygame
import os
#760 *2, 8 *2
Width, Height = 1000, 1000
Rows, Cols = 8,8
Square = Width//Rows
path = "images"
pathmur = "images/murs"
pathpiston = "images/Piston/PISTON"
pathpistonc = "images/Piston/PISTON COLLANT"
pathassets = "assets"

#arrierejeu_img = pygame.image.load("images/sol.png") # A supprimer

Sol = pygame.transform.scale(pygame.image.load(os.path.join(path, "sol.png")), (Square, Square ))
Le = pygame.transform.scale(pygame.image.load(os.path.join(path, "lampe éteinte.png")), (Square, Square ))
La = pygame.transform.scale(pygame.image.load(os.path.join(path, "lampe allumée.png")), (Square, Square ))
Br = pygame.transform.scale(pygame.image.load(os.path.join(path, "bloque de redstone.png")), (Square, Square ))
P = pygame.transform.scale(pygame.image.load(os.path.join(pathassets, "PAPER.jpg")), (Square, Square ))
#MUR
Mcbd = pygame.transform.scale(pygame.image.load(os.path.join(pathmur, "MCBD.png")), (Square, Square ))
Mcbg = pygame.transform.scale(pygame.image.load(os.path.join(pathmur, "mur coin bas gauche.png")), (Square, Square ))
Mchd = pygame.transform.scale(pygame.image.load(os.path.join(pathmur, "mur coin haut droit.png")), (Square, Square ))
Mchg = pygame.transform.scale(pygame.image.load(os.path.join(pathmur, "mur coin haut gauche.png")), (Square, Square ))
Mh = pygame.transform.scale(pygame.image.load(os.path.join(pathmur, "mur horizontal.png")), (Square, Square ))
Mhr = pygame.transform.scale(pygame.image.load(os.path.join(pathmur, "mur horizontal retourné.png")), (Square, Square ))
Mv = pygame.transform.scale(pygame.image.load(os.path.join(pathmur, "mur vertical.png")), (Square, Square ))
Mvr = pygame.transform.scale(pygame.image.load(os.path.join(pathmur, "mur vertical retourné.png")), (Square, Square ))
#PISTON
Ph = pygame.transform.scale(pygame.image.load(os.path.join(pathpiston, "piston haut fermé.png")), (Square, Square ))
Pd = pygame.transform.scale(pygame.image.load(os.path.join(pathpiston, "piston droit fermé.png")), (Square, Square ))
Pb = pygame.transform.scale(pygame.image.load(os.path.join(pathpiston, "piston bas fermé.png")), (Square, Square ))
Pg = pygame.transform.scale(pygame.image.load(os.path.join(pathpiston, "piston gauche fermé.png")), (Square, Square ))
Pho = pygame.transform.scale(pygame.image.load(os.path.join(pathpiston, "piston haut ouvert.png")), (Square, Square ))
Pdo = pygame.transform.scale(pygame.image.load(os.path.join(pathpiston, "piston droit ouvert.png")), (Square, Square ))
Pbo = pygame.transform.scale(pygame.image.load(os.path.join(pathpiston, "piston bas ouvert.png")), (Square, Square ))
Pgo = pygame.transform.scale(pygame.image.load(os.path.join(pathpiston, "piston gauche ouvert.png")), (Square, Square ))
#PISTON COLLANT
Phc = pygame.transform.scale(pygame.image.load(os.path.join(pathpistonc, "piston colant haut fermé.png")), (Square, Square ))
Pdc = pygame.transform.scale(pygame.image.load(os.path.join(pathpistonc, "piston colant droit fermé.png")), (Square, Square ))
Pbc = pygame.transform.scale(pygame.image.load(os.path.join(pathpistonc, "piston colant bas fermé.png")), (Square, Square ))
Pgc = pygame.transform.scale(pygame.image.load(os.path.join(pathpistonc, "piston colant gauche fermé.png")), (Square, Square ))
Phoc = pygame.transform.scale(pygame.image.load(os.path.join(pathpistonc, "piston colant haut ouvert.png")), (Square, Square ))
Pdoc = pygame.transform.scale(pygame.image.load(os.path.join(pathpistonc, "piston colant droit ouvert.png")), (Square, Square ))
Pboc = pygame.transform.scale(pygame.image.load(os.path.join(pathpistonc, "piston colant bas ouvert.png")), (Square, Square ))
Pgoc = pygame.transform.scale(pygame.image.load(os.path.join(pathpistonc, "piston colant gauche ouvert.png")), (Square, Square ))
#CADENAS Fermé
C1 = pygame.image.load(os.path.join(pathassets, "C4.png"))
C2 = pygame.image.load(os.path.join(pathassets, "C4.png"))
C3 = pygame.image.load(os.path.join(pathassets, "C4.png"))
C4 = pygame.image.load(os.path.join(pathassets, "C4.png"))
C5 = pygame.image.load(os.path.join(pathassets, "C4.png"))
C6 = pygame.image.load(os.path.join(pathassets, "C4.png"))
C7 = pygame.image.load(os.path.join(pathassets, "C4.png"))

print("constants ok")