# Créé par ANTOINE, le 15/12/2023 en Python 3.7
import pygame
import sys
import time
from .constants import *
from .board import *
from .button import Button


width = screen.get_width() * 1
height = screen.get_height() * 1
green = (144, 201, 120) #144,201,120
green = (0, 0, 0)

# pygame.init()


#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
IG = pygame.image.load("assets/Image gris.png")
BG = pygame.image.load("assets/AP.png") #Image arriere plan = DD.jpg

scaled_image = pygame.transform.scale(BG, (width, height)) 
scaled_image2 = pygame.transform.scale(IG, (width, height))
centre = width/2
temps_debut = 0
niveau_actuelle = 1 
niveau_reco = 0

clock = pygame.time.Clock() #FPS
FPS = 60  #FPS


def get_font(size): #Ecriture 
    return pygame.font.Font("assets/RaveoVF.ttf", size)

def main_menu_v1(): #MENU
    while True:
        screen.blit(scaled_image, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MENU J1", True, "#03BC00")
        MENU_RECT = MENU_TEXT.get_rect(center=(centre, 90))

        #Front = 75 
        # BOUTON EN DESSOUS
        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(centre, 225), 
                            text_input="JOUER", font=get_font(75), base_color="Cyan", hovering_color="Orange")
        LEVEL_BUTTON = Button(image=pygame.image.load("assets/113.png"), pos=(centre, 375),
                            text_input="dev", font=get_font(75), base_color="Cyan", hovering_color="black") #LEVEL
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(centre, 525), 
                            text_input="OPTIONS", font=get_font(75), base_color="Cyan", hovering_color="White") #OPTIONS
        OTHER_GAME = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(centre, 675),
                            text_input="CHANGER DE JEUX", font=get_font(75), base_color="Cyan", hovering_color="red")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(centre, 825), 
                            text_input="QUITTER", font=get_font(75), base_color="Cyan", hovering_color="red")

        screen.blit(MENU_TEXT, MENU_RECT) 

        for button in [PLAY_BUTTON, LEVEL_BUTTON, OPTIONS_BUTTON, OTHER_GAME, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:    
                """
                Si les coordonnées du clic coincide avec les coordonnées d'un bouton alors :
                """
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS): #JOUER
                    """
                    Si c'est le bouton JOUER, le niveau = niveau_actuelle, ce qui permet de mettre le prochain niveau et non le niveau 1
                     et load_map(niveau) permet de lancer la map selon un niveau 
                    """
                    global niveau 
                    niveau = niveau_actuelle
                    # load_map(niveau)
                    level()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS): #OPTIONS
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS): #QUITTER
                    pygame.quit()
                    sys.exit()
                if LEVEL_BUTTON.checkForInput(MENU_MOUSE_POS): #LEVEL 
                    pass
                if OTHER_GAME.checkForInput(MENU_MOUSE_POS): #Menu principale
                    from main import what_game
                    what_game()
        pygame.display.update()

def options():
    while True:
        screen.blit(scaled_image, (0,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(100).render("OPTIONS", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(centre, 90)) #Nom Menu Haut Page

        #BOUTON EN DESSOUS
        A_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(370, 250), 
                            text_input="Basique", font=get_font(75), base_color="Cyan", hovering_color="Blue")
        B_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(995, 250), 
                            text_input="Noir", font=get_font(75), base_color="Cyan", hovering_color="Blue")
        C_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(370, 400), 
                            text_input="Losange", font=get_font(75), base_color="Cyan", hovering_color="Blue")
        D_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(995, 400), 
                            text_input="Croix", font=get_font(75), base_color="Cyan", hovering_color="Blue")
        E_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(370, 550), 
                            text_input="Gauche", font=get_font(75), base_color="Cyan", hovering_color="Blue")
        F_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(995, 550), 
                            text_input="Droite", font=get_font(75), base_color="Cyan", hovering_color="Blue")
        RETOUR_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(683, 675), 
                            text_input="RETOUR", font=get_font(75), base_color="Cyan", hovering_color="Red")
        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [RETOUR_BUTTON, A_BUTTON, B_BUTTON, C_BUTTON, D_BUTTON, E_BUTTON, F_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                """
                Si je ferme la page, alors :
                """
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RETOUR_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu_v1()
                if A_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
                if B_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mouse.set_cursor(pygame.cursors.arrow)
                if C_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mouse.set_cursor(pygame.cursors.diamond)
                if D_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mouse.set_system_cursor (pygame.SYSTEM_CURSOR_CROSSHAIR)
                if E_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mouse.set_cursor(pygame.cursors.tri_left)
                if F_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mouse.set_cursor(pygame.cursors.tri_right)
        pygame.display.update() #Permet d'actualiser l'affichage 

def level(): #LEVEL
    global canard, vache, cheval, cochon, poule, carrote, eau
    canard = "red"
    vache = "red"
    cheval = "red"
    cochon = "red"
    poule = "red"
    carrote = "red"
    eau = "red"
    salopette = "red"
    sac = "red"
    pigeon = "red"
    smack  = "red"
    valise = "red"
    oeuf = "red"
    portable = "red"
    teo = "red"

    while True:
        global niveau_actuelle
        screen.blit(scaled_image, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("LEVELS", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(centre, 90)) 
        
        I = Button(image=pygame.image.load("assets/BG T1.png"), pos=(200, 300), 
                            text_input="1", font=get_font(75), base_color="Cyan", hovering_color="green")
        II = Button(image=pygame.image.load("assets/BG T1.png"), pos=(350, 300), #LEVEL 
                            text_input="2", font=get_font(75), base_color="Cyan", hovering_color=canard)
        III = Button(image=pygame.image.load("assets/BG T1.png"), pos=(500, 300), #LEVEL 
                            text_input="3", font=get_font(75), base_color="Cyan", hovering_color=vache)
        IV = Button(image=pygame.image.load("assets/BG T1.png"), pos=(650, 300), #LEVEL 
                            text_input="4", font=get_font(75), base_color="Cyan", hovering_color=cheval)
        V = Button(image=pygame.image.load("assets/BG T1.png"), pos=(800, 300), #LEVEL 
                            text_input="5", font=get_font(75), base_color="Cyan", hovering_color=cochon)
        VI = Button(image=pygame.image.load("assets/BG T1.png"), pos=(950, 300), #LEVEL 
                            text_input="6", font=get_font(75), base_color="Cyan", hovering_color=poule)
        VII = Button(image=pygame.image.load("assets/BG T1.png"), pos=(1100, 300), #LEVEL 
                            text_input="7", font=get_font(75), base_color="Cyan", hovering_color=carrote)
        VIII = Button(image=pygame.image.load("assets/BG T1.png"), pos=(1250, 300), #LEVEL 
                            text_input="8", font=get_font(75), base_color="Cyan", hovering_color=eau) 
        IX = Button(image=pygame.image.load("assets/BG T1.png"), pos=(200, 500), 
                            text_input="9", font=get_font(75), base_color="Cyan", hovering_color=salopette) # Changer a partir d'ici
        X = Button(image=pygame.image.load("assets/BG T1.png"), pos=(350, 500), #LEVEL 
                            text_input="10", font=get_font(75), base_color="Cyan", hovering_color=sac)
        XI = Button(image=pygame.image.load("assets/BG T1.png"), pos=(500, 500), #LEVEL 
                            text_input="11", font=get_font(75), base_color="Cyan", hovering_color=pigeon)
        XII = Button(image=pygame.image.load("assets/BG T1.png"), pos=(650, 500), #LEVEL 
                            text_input="12", font=get_font(75), base_color="Cyan", hovering_color=smack)
        XIII = Button(image=pygame.image.load("assets/BG T1.png"), pos=(800, 500), #LEVEL 
                            text_input="13", font=get_font(75), base_color="Cyan", hovering_color=valise)
        XIV = Button(image=pygame.image.load("assets/BG T1.png"), pos=(950, 500), #LEVEL 
                            text_input="14", font=get_font(75), base_color="Cyan", hovering_color=oeuf)
        XV = Button(image=pygame.image.load("assets/BG T1.png"), pos=(1100, 500), #LEVEL 
                            text_input="15", font=get_font(75), base_color="Cyan", hovering_color=portable)
        XVI = Button(image=pygame.image.load("assets/BG T1.png"), pos=(1250, 500), #LEVEL 
                            text_input="16", font=get_font(75), base_color="Cyan", hovering_color=teo) 
        RETOUR_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(centre, 675), 
                            text_input="RETOUR", font=get_font(75), base_color="Cyan", hovering_color="White")


        screen.blit(MENU_TEXT, MENU_RECT)


        for button in [I, II, III, IV, V, VI, VII, VIII, IX, X, XI, XII, XIII, XIV, XV, XVI, RETOUR_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)            
            
            
            
        def Cadenas(): #Affiche cadenas 
            global niveau_actuelle, canard, vache, cheval, cochon, poule, carrote, eau
            if niveau_actuelle == 1:
                screen.blit(C1, (360,220))
            if niveau_actuelle <= 2:
                """
                Si le niveau du joueur est = ou > au niveau 2, alors on affiche un cadenas.
                ICI le cadeans affiché est le cadenas du niveau 3
                """
                screen.blit(C1, (510,220))
            if niveau_actuelle <= 3:
                screen.blit(C1, (660,220))
            if niveau_actuelle <= 4:
                screen.blit(C1, (810,220))
            if niveau_actuelle <= 5:
                screen.blit(C1, (960,220))
            if niveau_actuelle <= 6:
                screen.blit(C1, (1110,220))
            if niveau_actuelle <= 7:
                screen.blit(C1, (1260,220))

            if niveau_actuelle <= 8:
                screen.blit(C1, (660,420))
            if niveau_actuelle <= 9:
                screen.blit(C1, (810,420))
            if niveau_actuelle <= 10:
                screen.blit(C1, (960,420))
            if niveau_actuelle <= 11:
                screen.blit(C1, (1110,420))
            if niveau_actuelle <= 12:
                screen.blit(C1, (1260,420))

            if niveau_actuelle <= 13:
                screen.blit(C1, (660,420))
            if niveau_actuelle <= 14:
                screen.blit(C1, (810,420))
            if niveau_actuelle <= 15:
                screen.blit(C1, (960,420))
            if niveau_actuelle <= 16:
                screen.blit(C1, (1110,420))
            if niveau_actuelle <= 17:
                screen.blit(C1, (1260,420))
            if niveau_actuelle <= 18:
                screen.blit(C1, (1260,420))

                #Affiche couleur vert si niveau deverouiller
            if niveau_actuelle >= 2:
                canard = "green"
            if niveau_actuelle >= 3:
                """
                Si le niveau du joueur est = ou > au niveau 3, alors on met la couleur green à vache 
                ICI ca correspond à la couleur du bouton du niveau 3
                """
                vache ="green"
            if niveau_actuelle >= 4:
                cheval = "green"
            if niveau_actuelle >= 5:
                cochon = "green"
            if niveau_actuelle >= 6:
                poule = "green"
            if niveau_actuelle >= 7:
                carrote = "green"
            if niveau_actuelle >= 8:
                eau = "green"
            
            

        if 2+1 == 3: #Condition vrai = boucle infinie 
            Cadenas()




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                global niveau
                if I.checkForInput(MENU_MOUSE_POS):
                    niveau = 1
                    load_map(niveau)
                if II.checkForInput(MENU_MOUSE_POS):
                    niveau = 2 #Niveau 2
                    if niveau_actuelle == niveau or niveau_actuelle > niveau:
                        load_map(niveau)
                if III.checkForInput(MENU_MOUSE_POS):
                    niveau = 3
                    if niveau_actuelle == niveau or niveau_actuelle > niveau:
                        load_map(niveau)
                if IV.checkForInput(MENU_MOUSE_POS): #LEVEL 
                    niveau = 4
                    if niveau_actuelle == niveau or niveau_actuelle > niveau:
                        load_map(niveau)
                if V.checkForInput(MENU_MOUSE_POS): #LEVEL 
                    """
                    Pour le niveau 5, si le niveau_actuelle (celui du joueur) est = ou > au niveau 5, on lance le niveau 
                    Sinon rien ne se passe, evite de 
                    """
                    niveau = 5
                    if niveau_actuelle == niveau or niveau_actuelle > niveau:
                        load_map(niveau)
                if VI.checkForInput(MENU_MOUSE_POS): #LEVEL 
                    niveau = 6
                    if niveau_actuelle == niveau or niveau_actuelle > niveau:
                        load_map(niveau)
                if VII.checkForInput(MENU_MOUSE_POS): #LEVEL 
                    niveau = 7
                    if niveau_actuelle == niveau or niveau_actuelle > niveau:
                        load_map(niveau)
                if VIII.checkForInput(MENU_MOUSE_POS): #LEVEL 
                    niveau = 8
                    if niveau_actuelle == niveau or niveau_actuelle > niveau:
                        load_map(niveau)
                if RETOUR_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu_v1()

        pygame.display.update()

def pause():
    #Ne pas prendre en compte le temps passé dans le menu pause 
    a = True
    while a:
        scaled_image2.set_alpha(5)
        

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MENU", True, "#03BC00")
        MENU_RECT = MENU_TEXT.get_rect(center=(centre, 90))



        RESET_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(centre, 225), 
                            text_input="RESET", font=get_font(75), base_color="Cyan", hovering_color="Orange")
        PLAY_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(centre, 375), 
                            text_input="REVENIR", font=get_font(75), base_color="Cyan", hovering_color="blue")
        LEVEL_BUTTON = Button(image=pygame.image.load("assets/113.png"), pos=(centre, 375), #LEVEL #113.png
                            text_input="LEVELS", font=get_font(75), base_color="Cyan", hovering_color="red") #LEVEL
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(centre, 525), 
                            text_input="OPTIONS", font=get_font(75), base_color="Cyan", hovering_color="White")
        MENU_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(centre, 675), 
                            text_input="MENU", font=get_font(75), base_color="Cyan", hovering_color="Green")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(centre, 825), 
                            text_input="QUITTER", font=get_font(75), base_color="Cyan", hovering_color="Black")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [RESET_BUTTON, PLAY_BUTTON, OPTIONS_BUTTON, MENU_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESET_BUTTON.checkForInput(MENU_MOUSE_POS):
                    load_map(niveau) #Charge le niveau
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    jeuxx() #Lance le jeu
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                if LEVEL_BUTTON.checkForInput(MENU_MOUSE_POS): #LEVEL 
                    level() #Lance le menu level
                if MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu_v1()
        pygame.display.update()

def jeuxx():
    global temps_debut, temps_ecoule, clock
    running = True
    #running = False
    temps_debut = 0

    while running:

        for evenement in pygame.event.get():

            if evenement.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_SPACE:
                    pause() 
                if evenement.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if temps_debut == 0: #Permet d'initier le chronometre s'il ne l'etait pas 
                    temps_debut = time.time()
                pos = pygame.mouse.get_pos()
                x = pos[0] // tile_size
                y = pos[1] // tile_size

                try:
                    tile_value = game_map[y][x]  # Obtenez la valeur de la tuile cliqué
                except:
                    break
                collision(x, y, game_map[y][x])

                #INTERACTION
                # if tile_value == PH: #PH
                #     if game_map[y-1][x] == i and game_map[y-2][x] == z:
                #         game_map[y-1][x] = z
                #         game_map[y-2][x] = i
                #         game_map[y][x] = PHO
                #     if game_map[y-1][x] == z:
                #         game_map[y][x] = PHO
                #         game_map[y-1][x] = zz
                # if tile_value == PHO: #PHO
                #     if game_map[y-1][x] == zz:
                #         game_map[y-1][x] = z
                #     game_map[y][x] = PH

        screen.fill(green)

        #Dessine la map
        draw_map(game_map)


        fps_actuel = int(clock.get_fps())
        texte_fps = get_font(50).render(f"FPS: {fps_actuel}", True, (255, 255, 255))
        position_fps = (screen.get_width() - texte_fps.get_width() - 10, 10)
        screen.blit(texte_fps, position_fps)        
        
        # Mettre à jour l'affichage
        pygame.display.flip()

        clock.tick(FPS) #Limite le nombre de FPS

def load_map(niveau):
    global game_map, game_map1, game_map2, game_map3, game_map4, game_map5, game_map6, game_map7, game_map8
    if niveau == 1:
        game_map = [row[:] for row in game_map1] #Sauvegarde de la map
    elif niveau == 2:
        game_map = [row[:] for row in game_map2]
    elif niveau == 3:
        game_map = [row[:] for row in game_map3]
    elif niveau == 4:
        game_map = [row[:] for row in game_map4]
    elif niveau == 5:
        game_map = [row[:] for row in game_map5]
    elif niveau == 6:
        game_map = [row[:] for row in game_map6]
    elif niveau == 7:
        game_map = [row[:] for row in game_map7]
    elif niveau == 8:
        game_map = [row[:] for row in game_map8]
    else:
        print("Niveau non valide")

    draw_map(game_map)
    jeuxx()

def collision(x, y, tile_value):
    print("x: ", x, "y: ", y, "bloc: ", tile_value)
    if tile_value == PH: #PH
        if game_map[y-1][x] == i and game_map[y-2][x] == z:
            game_map[y-1][x] = z
            game_map[y-2][x] = i
            game_map[y][x] = PHO
        if game_map[y-1][x] == z:
            game_map[y][x] = PHO
            game_map[y-1][x] = zz
    if tile_value == PHO: #PHO
        if game_map[y-1][x] == zz:
            game_map[y-1][x] = z
            game_map[y][x] = PH
    
    if tile_value == PD: #PD
        if game_map[y][x+1] == i and game_map[y][x+2] == z:
            game_map[y][x+1] = z
            game_map[y][x+2] = i
            game_map[y][x] = PDO
        if game_map[y][x+1] == z:
            game_map[y][x] = PDO
            game_map[y][x+1] = zz
    if tile_value == PDO: #PDO
        if game_map[y][x+1] == zz:
            game_map[y][x+1] = z
        game_map[y][x] = PD

    if tile_value == PB: #PB
        if game_map[y+1][x] == i and game_map[y+2][x] == z:
            game_map[y+1][x] = z
            game_map[y+2][x] = i
            game_map[y][x] = PBO
        if game_map[y+1][x] == z:
            game_map[y+1][x] = zz
            game_map[y][x] = PBO
    if tile_value == PBO: #PBO
        if game_map[y+1][x] == zz:
            game_map[y+1][x] = z
        game_map[y][x] = PB

    if tile_value == PG: #PG
        if game_map[y][x-1] == i and game_map[y][x-2] == z:
            game_map[y][x-1] = zz
            game_map[y][x-2] = i
            game_map[y][x] = PGO
        if game_map[y][x-1] == z:
            game_map[y][x] = PGO
            game_map[y][x-1] = zz
    if tile_value == PGO: #PGO
        if game_map[y][x-1] == zz:
            game_map[y][x-1] = z
        game_map[y][x] = PG

    if tile_value == PBC:
        if game_map[y+1][x] == i and game_map[y+2][x] == z:
            game_map[y+1][x] = z 
            game_map[y+2][x] = i 
            game_map[y][x] = PBOC
        if game_map[y+1][x] == z:
            game_map[y+1][x] = zz
            game_map[y][x] = PBOC
    if tile_value == PBOC:
        if game_map[y+2][x] != i:
            game_map[y+1][x] = z
            game_map[y][x] = PBC
        if game_map[y+2][x] == i:
            game_map[y+1][x] = i
            game_map[y+2][x] = z 
            game_map[y][x] = PBC

    if tile_value == PHC:
        if game_map[y-1][x] == i and game_map[y-2][x] == z:
            game_map[y-1][x] = z 
            game_map[y-2][x] = i 
            game_map[y][x] = PHOC
        if game_map[y-1][x] == z:
            game_map[y-1][x] = zz
            game_map[y][x] = PHOC
    if tile_value == PHOC:
        if game_map[y-2][x] != i:
            game_map[y-1][x] = z
            game_map[y][x] = PHC
        if game_map[y-2][x] == i:
            game_map[y-1][x] = i
            game_map[y-2][x] = z 
            game_map[y][x] = PHC

    if tile_value == PGC:
        if game_map[y][x-1] == i and game_map[y][x-2] == z:
            game_map[y][x-1] = zz
            game_map[y][x-2] = i
            game_map[y][x] = PGOC
        if game_map[y][x-1] == z:
            game_map[y][x-1] = zz
            game_map[y][x] = PGOC
    if tile_value == PGOC: 
        if game_map[y][x-2] != i:
            game_map[y][x-1] = z
            game_map[y][x] = PGC
        if game_map[y][x-2] == i:
            game_map[y][x-1] = i
            game_map[y][x-2] = z 
            game_map[y][x] = PGC

    if tile_value == PDC:
        if game_map[y][x+1] == i and game_map[y][x+2] == z:
            game_map[y][x+1] = zz
            game_map[y][x+2] = i
            game_map[y][x] = PDOC
        if game_map[y][x+1] == z:
            game_map[y][x+1] = zz
            game_map[y][x] = PDOC
    if tile_value == PDOC: 
        if game_map[y][x+2] != i:
            game_map[y][x+1] = z
            game_map[y][x] = PDC
        if game_map[y][x+2] == i:
            game_map[y][x+1] = i
            game_map[y][x+2] = z 
            game_map[y][x] = PDC
        #LE fait de le mettre dans la boucle while fait que ça calcule à chaque fois les x y du bloc de lumière
        #Mettre dans a chaque boutton appuyé
        #RESOLU
    coordinates = []
    for row in range(len(game_map)):
        for col in range(len(game_map[row])):
            if game_map[row][col] == j:
                coordinates.append((row, col))

    for coord in coordinates:
        l, m = coord
    #print(m,l)


        if game_map[l][m] == j:
            if game_map[l][m+1] == i:
                game_map[l][m] = k
                draw_map(game_map)
                pygame.display.flip()
                win()
            if game_map[l][m-1] == i:
                game_map[l][m] = k
                draw_map(game_map)
                pygame.display.flip()
                win()
            if game_map[l+1][m] == i:
                game_map[l][m] = k
                draw_map(game_map)
                pygame.display.flip()
                win()
            if game_map[l-1][m] == i:
                game_map[l][m] = k
                draw_map(game_map)
                pygame.display.flip()
                win()
        if game_map[l][m] == k:
            if game_map[l][m+1] == i or game_map[l][m-1]== i or game_map[l+1][m] == i or game_map[l-1][m] == i:
                game_map[l][m] = k
            else:
                game_map[l][m] = j
    # x+1 = gauche
    # x-1 = droite
    # y+1 = haut
    # y-1 = bas

def win():
    a = True 
    global niveau, niveau_actuelle, temps_jeu
    if niveau_actuelle == niveau:
        niveau_actuelle = niveau_actuelle + 1
    temps_fin = time.time() #Prends temps 
    temps_jeu = temps_fin - temps_debut #Compare la difference
    while a:
        scaled_image2.set_alpha(5)
        screen.blit(scaled_image2, (0, 0))
        pygame.display.update()


        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(centre, 675), 
                            text_input="MENU", font=get_font(75), base_color="Cyan", hovering_color="Red")
        NEXT_LEVEL = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(centre, 550), 
                            text_input="->", font=get_font(75), base_color="Cyan", hovering_color="Red")

        MENU_TEXT = get_font(100).render("VICTOIRE", True, "#03BC00")
        TIMER_TEXT = get_font(30).render(f"Temps écoulé : {round(temps_jeu, 2)} secondes", True, "#03BC00") #Affiche le temps 

        MENU_RECT = MENU_TEXT.get_rect(center=(centre, 90)) 
        screen.blit(MENU_TEXT, MENU_RECT) 
        TIMER_RECT = TIMER_TEXT.get_rect(center=(centre, 390))
        screen.blit(TIMER_TEXT, TIMER_RECT)

        for button in [MENU_BUTTON, NEXT_LEVEL]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu_v1()
                    pygame.display.update()
                if NEXT_LEVEL.checkForInput(MENU_MOUSE_POS):
                    niveau = niveau + 1
                    load_map(niveau)

def reset():
    load_map(niveau)


print("jeux1  ok")
#main_menu() #Affiche le menu principale
#main_menu_j1()

# main_menu_v1() # a supprimeer