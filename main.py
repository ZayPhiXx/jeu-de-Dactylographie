import pygame, time, random  # time
from Game import Game  # permet d'importer le fichier Game.py

pygame.init()  # initialisation de pygame
pygame.mixer.init()

pygame.init()  # initialisation de pygame
pygame.mixer.init()
game = Game()  # creation d'une instance de la class Game
nb_mot = 23  # nombre de mot afficher
x_screen = 1000
y_screen = 720
mid_x_screen = x_screen / 2
screen = pygame.display.set_mode((x_screen, y_screen),pygame.RESIZABLE)  # création d'un écran de 850 par 800
button = pygame.image.load("doc/buttton.png")  # image du boutton de demarage
button2 = pygame.image.load("doc/button2.png")  # image du boutton de retour au menu
buttonremove = pygame.image.load("doc/buttonrem.png")  # image du boutton pour diminuer le nombre de mot
buttonremove_rect = buttonremove.get_rect()  # recuperation du rectangle du boutton
buttonremove_rect.x = mid_x_screen - (
            buttonremove_rect.width / 2) - 71 # definition des coordonées en x du rectangle du boutton
buttonremove_rect.y = 310  # definition des coordonées en y du rectangle du boutton

buttonadd = pygame.image.load("doc/buttonadd1.png")  # image du boutton pour augmenter le nombre de mot
buttonadd_rect = buttonadd.get_rect()
buttonadd_rect.x = mid_x_screen - (buttonadd_rect.width / 2) + 81
buttonadd_rect.y = 310

nbmot = game.font30.render(str(nb_mot - 3), 1, (255, 255, 255))  # mise en surface du nombre de mot
nbmotx = mid_x_screen - 10  # coordonées en x du nombre de mot
nbmoty = 325  # coordonées en y du nombre de mot

button_rect = button.get_rect()
button_rect.x = mid_x_screen - (button_rect.width / 2)
button_rect.y = 450
running = True
button2_rect = button2.get_rect()
button2_rect.x = mid_x_screen - (button2_rect.width / 2)
button2_rect.y = 380
music_playing = False
dico = {}  # definition du dictionnaire de mot
music_playing = False
tab_musiques = [0.0, 435.0, 902.0, 999.0, 1434.0, 1902.0, 2435.0, 2968.0, 3435.0, 3902.0, 3998.0] #Liste de temps dans la musique qui correspondent au commencement d'un nouveau morceau.

while running:  # condition pour maintenir la fenetre pygame ouverte

    pygame.display.flip()  # rafraichir l'écran
    if game.run == "debut":  # ecran de bienvenue
        temps_f = 0
        game.phrase = []
        game.c = 0
        menu = True  # variable qui permet de mettre en avant le boutton de notre choix
        motv = game.word(nb_mot)  # choix mots aléatoire
        tab_cara = game.splitz(motv)
        mot_raté = 0  # compteur pour le mode de jeu avec du temps
        mot1 = game.mot2(motv)
        dico = game.dic(dico, motv, nb_mot)
        MDJ = 2  # mode de jeu

        i = 1
        x = 0
        screen.blit(game.background, (0, 0))  # Création du background
        phrase_x1 = game.font30.render('Bienvenue dans ce jeu de dactylographie.', True,
                                       (100, 255, 100))  # titre principal
        screen.blit(phrase_x1, (mid_x_screen - (phrase_x1.get_width() / 2), 70))
        phrase_x2 = game.font30.render('Le but du jeu est de taper des mots', True, (255, 140, 0))
        screen.blit(phrase_x2, (mid_x_screen - (phrase_x2.get_width() / 2), 120))
        phrase_x3 = game.font30.render('le plus rapidement possible', True, (255, 140, 0))
        screen.blit(phrase_x3, (mid_x_screen - (phrase_x3.get_width() / 2), 170))
        phrase_x4 = game.font30.render('Séléctionner votre nombre de mots :', True, (255, 255, 255))
        screen.blit(phrase_x4, (mid_x_screen - (phrase_x4.get_width() / 2), 260))
        phrase_x5 = game.font30.render('Cliquez ici pour lancer le jeu :', True, (255, 255, 255))
        screen.blit(phrase_x5, (mid_x_screen - (phrase_x5.get_width() / 2), 400))
        screen.blit(game.font30.render('codé par Samuel ,Thomas et Roméo', True, (255, 255, 255)),
                    (10, (y_screen - 45)))
        screen.blit(button, (button_rect.x, button_rect.y))
        screen.blit(buttonadd, (buttonadd_rect.x, buttonadd_rect.y))
        screen.blit(buttonremove, (buttonremove_rect.x, buttonremove_rect.y))
        screen.blit(nbmot, (nbmotx, nbmoty))
        pygame.display.flip()
    if game.run == "play":  # ecrans de jeu (voir Game.py)
        screen.fill("black")  # Effaçage
        game.update(motv, screen, tab_cara, dico, nb_mot, mid_x_screen, temps_f,x_screen)  # Update
        if music_playing == False:
            file = "music/Jazz.mp3" #demarrage de la musique de fond
            pygame.mixer.music.load(file)
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play(start = tab_musiques[random.randint(0, len(tab_musiques))-1], loops = 0)
            music_playing = True

    if game.run == "fin":  # ecran de fin
        screen.blit(game.background, (0, 0))
        phrase_x7 = game.font30.render('Appreciation :', True, (255, 255, 255))
        screen.blit(phrase_x7, (mid_x_screen - (phrase_x7.get_width() / 2), 100))
        screen.blit(appreciation, (mid_x_screen - (appreciation.get_width() / 2), 150))
        phrase_x8 = game.font30.render(f'Score : {score} / {(nb_mot) - 3}  ({score_en_pourcentage} %)', True,
                                       (255, 255, 255))
        screen.blit(phrase_x8, (mid_x_screen - (phrase_x8.get_width() / 2), 240))
        phrase_x9 = game.font30.render(f'Temps : {round(temps_f, 1)} s', True, (255, 255, 255))
        screen.blit(phrase_x9, (mid_x_screen - (phrase_x9.get_width() / 2), 200))
        phrase_x10 = game.font30.render("Cliquez ici pour retourner au menu :", True, (255, 255, 255))
        screen.blit(phrase_x10, (mid_x_screen - (phrase_x10.get_width() / 2), 360))
        screen.blit(button2, (button2_rect.x, button2_rect.y))
        phrase_x11 = game.font20.render("Pour finir le jeu (le programme) appuyez un dernière fois sur espace", True,
                                        (255, 255, 255))
        screen.blit(phrase_x11, (mid_x_screen - (phrase_x11.get_width() / 2), 600))
        phrase_x16 = game.font30.render(f"score en mot par minutes : {score_WPM}", True, (255, 255, 255))
        screen.blit(phrase_x16, (mid_x_screen - (phrase_x16.get_width() / 2), 285))
        menu = False
        screen.blit(game.font30.render('codé par Samuel ,Thomas et Roméo', True, (255, 255, 255)),
                    (10, (y_screen - 45)))
        pygame.display.flip()  # Refresh


    for event in pygame.event.get():

        if event.type == pygame.QUIT:  # Permet de fermer la fenêtre quand on clique sur la croix rouge
            quit()
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            if button_rect.collidepoint(
                    pygame.mouse.get_pos()) and menu == True:  # Si l'utilisateur appuie sur le bouton pour jouer
                game.run = "play"  # Le jeu est défini sur True donc le jeu commence (Voir fichier Game.py )
                # gamer = False     ca sert a quoi ???
            if buttonadd_rect.collidepoint(pygame.mouse.get_pos()):
                nb_mot += 5  # choix du nombre de mots
                nbmot = game.font30.render(str(nb_mot - 3), 1, (255, 255, 255))
                screen.blit(nbmot, (nbmotx, nbmoty))
                pygame.display.flip()
                if nb_mot >= 48:
                    nb_mot = 48
                    nbmot = game.font30.render(str(nb_mot - 3), 1, (255, 255, 255))
                    screen.blit(nbmot, (nbmotx, nbmoty))
            if buttonremove_rect.collidepoint(pygame.mouse.get_pos()):
                nb_mot -= 5
                nbmot = game.font30.render(str(nb_mot - 3), 1, (255, 255, 255))
                screen.blit(nbmot, (nbmotx, nbmoty))
                if nb_mot <= 8:
                    nb_mot = 8
                    nbmot = game.font30.render(str(nb_mot - 3), 1, (255, 255, 255))
                    screen.blit(nbmot, (nbmotx, nbmoty))
            if button2_rect.collidepoint(pygame.mouse.get_pos()) and menu == False:
                pygame.mixer.music.stop()
                music_playing = False
                game.run = "debut"

        if event.type == pygame.TEXTINPUT:

            if event.text in game.mot:
                game.liste.append(event.text)

        if event.type == pygame.KEYDOWN:
            game.afficher_temps(screen, mid_x_screen,temps_f)  # chronometre

            if event.key == pygame.K_BACKSPACE:

                if game.liste != []:

                    del game.liste[len(game.liste) - 1]

                    if game.liste == []:
                        game.liste = []

            if event.key == pygame.K_SPACE:  # quand l'on appuis sur espace
                phrase_complete = "".join(game.liste)
                game.phrase.append(phrase_complete)
                game.liste = []


                if len(game.phrase) == (nb_mot) - 2:
                    pygame.quit()
                    running = False
                    break

                if motv[x] == game.phrase[x] and len(game.phrase) != (nb_mot) - 2: #met les mots en verts
                    game.c += 1
                    pygame.display.flip()
                    game.liste = []
                    game.g += 1
                    dico[f"mot{i}"] = game.font30.render(motv[i - 1], 1, (0, 255, 0))


                    if game.liste != []:
                        game.liste = []

                if motv[x] != game.phrase[x] and len(game.phrase) != (nb_mot) - 2: # met les mots en rouge
                    pygame.display.flip()
                    game.liste = []
                    dico[f"mot{i}"] = game.font30.render(motv[i - 1], 1, (255, 0, 0))
                    mot_raté += 1

                    if game.liste != []:
                        game.liste = []

                i += 1
                x += 1




                if MDJ == 2 and len(game.phrase) == (nb_mot) - 3:
                    game.update_status = False
                    game.temps_fin = time.time()
                    temps_f = game.temps_fin - game.temps_activation
                    # parti ecran win
                    score = game.c
                    score_en_pourcentage = (score / ((nb_mot) - 3)) * 100
                    score_en_pourcentage = round(score_en_pourcentage)
                    score_WPM = game.c * 60 / temps_f  # Affichage du nombre de mots par minute.
                    score_WPM = round(score_WPM)
                    # differentes conditons pour avoir differentes appreciations en fonctions du pourcentage de reusite
                    if score_WPM < 10:
                        appreciation = game.font30.render(f"Dans les -1%... Peut mieux faire!", True, (255, 255, 255))
                        file = "music/rick.mp3"
                        pygame.mixer.music.load(file)
                        pygame.mixer.music.set_volume(0.2)
                        pygame.mixer.music.play()

                    elif score_WPM > 10 and score_WPM < 30:
                        appreciation = game.font30.render(f"C'est tout ce que tu peux faire ?!", True, (255, 255, 255))
                        file = "music/Iphone.mp3"
                        pygame.mixer.music.load(file)
                        pygame.mixer.music.set_volume(0.2)
                        pygame.mixer.music.play()

                    elif score_WPM > 30 and score_WPM < 60:
                        appreciation = game.font30.render(f"Pas mal!", True, (255, 255, 255))
                        file = "music/clap.mp3"
                        pygame.mixer.music.load(file)
                        pygame.mixer.music.set_volume(0.2)
                        pygame.mixer.music.play()


                    elif score_WPM > 60 and score_WPM < 90:
                        appreciation = game.font30.render(f"Perfect !", True, (255, 255, 255))
                        file = "music/initial_d.mp3"
                        pygame.mixer.music.load(file)
                        pygame.mixer.music.set_volume(0.2)
                        pygame.mixer.music.play()

                    elif score_WPM > 90 and score_WPM < 120:
                        appreciation = game.font30.render(f"Niveau profesionnel !", True, (255, 255, 255))
                        file = "music/initial_d.mp3"
                        pygame.mixer.music.load(file)
                        pygame.mixer.music.set_volume(0.2)
                        pygame.mixer.music.play()

                    elif score_WPM > 120 and score_WPM < 150:
                        appreciation = game.font30.render(f"ON FIRE !", True, (255, 255, 255))
                        file = "music/initial_d.mp3"
                        pygame.mixer.music.load(file)
                        pygame.mixer.music.set_volume(0.2)
                        pygame.mixer.music.play()

                    else:
                        appreciation = game.font30.render(
                            "Il y a un petit probleme... ", True,
                            (255, 255, 255))
                    x += 2  # si on réappuis sur espace apres la fin du jeu ca permet de stop le programme
                    game.run = "fin"






