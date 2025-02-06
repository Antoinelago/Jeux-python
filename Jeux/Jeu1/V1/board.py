import pygame
from constants import *

# pygame.init()

clock = pygame.time.Clock()
fps = 60

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# 50 20 200 500 500
cell_size = 59 #screen.get_width()   #77 /60 pour 13/// 59
tile_size = 59 #screen.get_height()   #77 /60 pour 13/// 59
cols = 20
margin = 200
screen_width = screen.get_width()
screen_height = screen.get_height() 

# 12 horizontale pour 64

pygame.display.set_caption('Jeu Python')



PH = 13 #PH
PHO = 17 #PHO
PD = 14 #PD
PDO = 18 #PDO
PB = 15 #PB
PBO = 19 #PBO
PG = 16 #PG
PGO = 20 #PGO

PHC = 21
PHOC = 25
PDC = 22
PDOC = 26
PBC = 23
PBOC = 27
PGC = 24
PGOC = 28

i = 4 #BR
j = 2 #LE
k = 3 #LA
p = 30
cf = 31

zz = 0
z = 1 #sol
game_map = [
    [0,0],
    [0,0]
]
#13 verticale    23 horizontale 


game_map1  = [ #OK 1er niv
    [8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,7],
    [11,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,j,z,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,i,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,PH,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [6,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,5,z]
]

game_map2  = [ #OK 2 Niv
    [8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,7],
    [11,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,j,z,z,PG,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,PD,i,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,z,z,PH,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [6,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,5,z]
]

game_map3  = [ #OK 3 niv Intro PBC
    [8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,7],
    [11,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,z,z,PBC,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,z,PDO,zz,z,j,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,z,z,z,zz,PGO,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,z,PDO,zz,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,z,z,i,PH,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,z,z,PH,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [6,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,5,z]
]

game_map4 = [ #OK Niv 4
    [8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,7],
    [11,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,z,PBC,z,j,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,PD,z,z,z,PGC,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,PBC,PD,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,PD,z,z,z,PGC,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,i,PHC,PHC,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [6,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,5,z]
]

game_map5 = [ #OK 5 Niv
    [8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,7],
    [11,z,z,z,PB,z,z,z,z,z,z,z,z,z,z,z,z,z,PB,z,z,z,12,z],
    [11,z,PD,i,z,PB,z,z,z,z,z,z,z,z,z,z,z,PB,z,i,PG,z,12,z],
    [11,z,z,PD,z,z,PB,z,z,z,z,z,z,z,z,z,PB,z,z,PG,z,z,12,z],
    [11,z,z,z,PD,z,z,PB,z,z,z,z,z,z,z,PB,z,z,PG,z,z,z,12,z],
    [11,z,z,z,z,PD,z,z,PB,z,z,z,z,z,PB,z,z,PG,z,z,z,z,12,z],
    [11,z,z,z,z,z,PD,z,z,PB,z,z,z,PB,z,z,PG,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,PD,z,z,PB,z,PB,z,z,PG,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,PD,z,z,PB,z,z,PG,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,z,PD,z,z,z,PG,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,z,z,PD,j,PG,z,z,z,z,z,z,z,z,z,12,z],    
    [6,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,5,z]
]

game_map6 = [ #OK  Niv 6
    [8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,7],
    [11,z,PD,z,z,z,PGC,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,PD,i,z,PD,z,z,PB,z,z,PBC,z,PB,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,PH,z,PHC,z,z,PGC,PD,z,z,z,PGC,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,PHC,z,PB,z,z,PGC,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,PD,z,z,z,PGC,z,j,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,PHC,z,PH,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,PDC,z,z,PH,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,PDC,z,z,PHC,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,PDC,z,z,PHC,z,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,j,PH,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [6,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,5,z]
]

game_map7  = [ #OK  7 niv
    [8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,7],
    [11,z,z,z,z,z,z,z,z,z,PBC,z,PB,z,z,z,z,z,z,z,z,z,12,z],
    [11,z,z,z,z,z,PB,z,z,PD,z,z,z,PGC,z,z,PB,z,z,z,z,z,12,z],
    [11,z,PBC,PD,z,z,z,PGC,PBC,z,z,PD,z,z,PD,z,z,z,PGC,z,z,z,12,z],
    [11,PD,z,z,z,PGC,z,PD,z,z,z,PGC,PD,z,z,z,PGC,j,z,z,z,z,12,z],
    [11,z,z,PBC,PH,PD,z,z,z,PGC,PH,z,z,PHC,z,PH,z,z,PBC,z,z,z,12,z],
    [11,z,z,z,PG,z,PHC,PD,z,z,PB,z,z,PBC,z,PB,z,z,z,PG,z,z,12,z],
    [11,z,PH,z,z,PG,z,z,PHC,z,z,PGC,PD,z,z,z,PGC,PH,z,z,PGC,z,12,z],
    [11,z,PD,z,z,z,z,z,z,PHC,z,z,z,z,PGC,z,PD,z,z,z,PGC,z,12,z],
    [11,PD,z,z,PH,z,z,z,z,PD,z,z,z,PGC,PD,z,z,z,PGC,PH,z,z,12,z],
    [11,z,i,PH,z,z,z,z,z,z,PHC,z,PH,z,z,PHC,z,PH,z,z,z,z,12,z],
    [11,z,PH,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,z,12,z],
    [6,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,5,z]
]

game_map8 = [ # OK 8 niv
	[8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,7],
	[11,z,PBC,z,z,z,z,z,z,z,j,PBC,z,z,z,z,PBC,z,PB,PDC,z,i,12], #1
	[11,j,z,PBC,z,z,z,z,z,PDC,z,z,PBC,z,z,z,z,PDC,z,z,z,PG,12], #2
	[11,PDC,z,z,PBC,z,z,z,z,z,PD,z,z,PBC,z,PDC,z,z,z,PG,PHC,z,12], #3
	[11,z,PDC,z,z,PBC,z,z,z,z,z,PDC,z,z,PBC,PD,z,z,z,PGC,PB,z,12], #4
	[11,z,z,PDC,z,z,PBC,z,z,z,z,z,PDC,z,z,PBC,PHC,PD,z,z,z,PGC,12], #5
	[11,z,z,z,PDC,z,z,PBC,z,z,z,z,z,PDC,z,z,PBC,z,PHC,z,z,z,12], #6
	[11,z,z,z,z,PDC,z,z,PBC,z,z,z,PBC,z,PDC,z,z,PDC,z,z,z,PG,12], #7
	[11,z,z,z,z,z,PDC,z,z,PDC,z,z,z,PGC,PB,PDC,z,z,z,PG,PHC,z,12], #8
	[11,z,z,z,z,z,z,PDC,z,z,z,PG,z,PDC,z,z,z,PG,PHC,z,z,z,12], #9
	[11,z,z,z,z,z,z,z,z,z,PHC,PDC,z,z,z,PG,PHC,z,z,z,z,z,12], #10 
	[11,z,z,z,z,z,z,z,z,z,z,z,PHC,z,PHC,z,z,z,z,z,z,z,12], # 11
	[6,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,5]
]


def draw_map(game_map): #Dessine la map en fonction du game_map
    for row in range(len(game_map)):
        for col in range(len(game_map[0])):
            x = col * cell_size 
            y = row * cell_size 
            #x = 1336 % 23
            #y = 1336 / 23
            if game_map[row][col] == 1:
                img = pygame.transform.scale(Sol, (tile_size, tile_size))
                screen.blit(img, (x, y))
            if game_map[row][col] == 2:
                img = pygame.transform.scale(Le, (tile_size, tile_size))
                screen.blit(img, (x, y))
            if game_map[row][col] == 3:
                img = pygame.transform.scale(La, (tile_size, tile_size))
                screen.blit(img, (x, y))
            if game_map[row][col] == 4:
                img = pygame.transform.scale(Br, (tile_size, tile_size))
                screen.blit(img, (x, y))
            if game_map[row][col] == 5:
                img = pygame.transform.scale(Mcbd, (tile_size, tile_size))
                screen.blit(img, (x, y))
            if game_map[row][col] == 6:
                img = pygame.transform.scale(Mcbg, (tile_size, tile_size))
                screen.blit(img, (x, y))
            if game_map[row][col] == 7:
                img = pygame.transform.scale(Mchd, (tile_size, tile_size))
                screen.blit(img, (x, y))
            if game_map[row][col] == 8:
                img = pygame.transform.scale(Mchg, (tile_size, tile_size))
                screen.blit(img, (x, y))
            if game_map[row][col] == 9:
                img = pygame.transform.scale(Mh, (tile_size, tile_size))
                screen.blit(img, (x, y))
            if game_map[row][col] == 10:
                img = pygame.transform.scale(Mhr, (tile_size, tile_size))
                screen.blit(img, (x, y))
            if game_map[row][col] == 11:
                img = pygame.transform.scale(Mv, (tile_size, tile_size))
                screen.blit(img, (x, y))
            if game_map[row][col] == 12:
                img = pygame.transform.scale(Mvr, (tile_size, tile_size))
                screen.blit(img, (x, y))
            if game_map[row][col] == 13:
                img = pygame.transform.scale(Ph, (tile_size, tile_size))
                screen.blit(img, (x, y))
            if game_map[row][col] == 14:
                img = pygame.transform.scale(Pd, (tile_size, tile_size))
                screen.blit(img, (x, y))
            if game_map[row][col] == 15:
                img = pygame.transform.scale(Pb, (tile_size, tile_size))
                screen.blit(img, (x, y))
            if game_map[row][col] == 16:
                img = pygame.transform.scale(Pg, (tile_size, tile_size))
                screen.blit(img, (x, y))
            if game_map[row][col] == 17:
                img = pygame.transform.scale(Pho, (tile_size, tile_size * 2))
                screen.blit(img, (x, y - tile_size))
            if game_map[row][col] == 18: #ICI PDO PROBLEME bloc droit non transparent
                img = pygame.transform.scale(Pdo, (tile_size * 2, tile_size))
                screen.blit(img, (x, y))
            if game_map[row][col] == 19: #ICI PBO PROBLEME bloc bas non transparent
                img = pygame.transform.scale(Pbo, (tile_size, tile_size * 2))
                screen.blit(img, (x, y))
            if game_map[row][col] == 20:
                img = pygame.transform.scale(Pgo, (tile_size * 2, tile_size))
                screen.blit(img, (x - tile_size, y))
            if game_map[row][col] == 21:
                img = pygame.transform.scale(Phc, (tile_size, tile_size))
                screen.blit(img, (x, y))
            if game_map[row][col] == 22:
                img = pygame.transform.scale(Pdc, (tile_size, tile_size))
                screen.blit(img, (x, y))
            if game_map[row][col] == 23:
                img = pygame.transform.scale(Pbc, (tile_size, tile_size))
                screen.blit(img, (x, y))
            if game_map[row][col] == 24:
                img = pygame.transform.scale(Pgc, (tile_size, tile_size))
                screen.blit(img, (x, y))
            if game_map[row][col] == 25:
                img = pygame.transform.scale(Phoc, (tile_size, tile_size * 2))
                screen.blit(img, (x, y - tile_size))
            if game_map[row][col] == 26:
                img = pygame.transform.scale(Pdoc, (tile_size * 2, tile_size))
                screen.blit(img, (x, y))
            if game_map[row][col] == 27:
                img = pygame.transform.scale(Pboc, (tile_size, tile_size * 2))
                screen.blit(img, (x, y))
            if game_map[row][col] == 28:
                img = pygame.transform.scale(Pgoc, (tile_size * 2, tile_size))
                screen.blit(img, (x - tile_size, y))
            if game_map[row][col] == 29:
                img = pygame.transform.scale(Sol, (tile_size, tile_size))
                screen.blit(img, (x, y))
            if game_map[row][col] == 30:
                img = pygame.transform.scale(P, (tile_size, tile_size))
                screen.blit(img, (x, y))
            #if game_map[row][col] == 31:
            #    img = pygame.transform.scale(CF, (tile_size, tile_size))
            #    screen.blit(img, (x, y))
                
print("board ok")