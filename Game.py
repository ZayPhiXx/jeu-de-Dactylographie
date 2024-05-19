import pygame, random, time


# from win import Win
class Game():

    def __init__(self):
        self.background = pygame.image.load("doc/background.jpg")  # image du fond
        self.run = "debut"
        self.screen = pygame.display.set_mode((1000, 1000))
        pygame.font.init()
        self.font30 = pygame.font.Font("doc/arial.ttf", 30)
        self.font20 = pygame.font.Font("doc/arial.ttf", 20)
        self.mot = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789éèà'-&çê"  # liste des caractère disponibles a taper.
        self.color = (255, 255, 255)  # couleur blanche
        self.colorwin = (0, 255, 0)  # couleur verte
        self.c = 0  # Compteur.
        self.g = 0  # compteur du mot de la phrase que l'on doit taper
        self.liste = []  # liste des caractere rentré , est reinitialiser a chaque fois que espace est taper
        self.phrase = []  # liste des mots qui sont rentrés
        self.etape = 2  # debut de test pour laisser l'utilisateur rentrer son nb de mots
        self.rect_ecriture = 320

        # Propriétés de temps
        self.temps_activation = 0
        self.temps_fin = 0
        self.temps_actuel = 0
        self.update_status = False  # Pour valider la condition de début du timer qu'une seule fois.

    def word(self, nb_mot):  # fonction pour prendre une phrase alléatoire
        file = open('doc/dico.txt', 'r+', encoding='utf-8')
        dico = []
        phrase = []
        ligne = file.readline().split(' ')

        for elem in ligne:
            dico.append(elem)

        for i in range(nb_mot):
            mot = dico[random.randint(0, len(dico) - 1)]
            phrase.append(mot)

        return (phrase)

    def dic(self, dico, motv, nb_mot):
        for i in range(
                nb_mot):  # boucle pour avoir les rect des mots
            key = "mot" + str(i + 1)
            elem1 = self.font30.render(motv[i], 1, ((255, 255, 255)))
            dico[key] = elem1
        return dico

    def splitz(self, tab):
        liste = []
        tabX = []

        for elem in tab:

            for cara in elem:
                liste.append(cara)
            tabX.append(liste)
            liste = []

        return tabX

    def mot2(self, motv):
        mot1 = self.font30.render(" ".join(motv), 1, (255, 255, 255))

        return mot1

    def afficher_temps(self, screen, mid_x_screen, temps_f):
        phrase_x13 = self.font30.render("C'EST PARTI !!", True, (50, 255, 50))
        screen.blit(phrase_x13, (mid_x_screen - (phrase_x13.get_width() / 2), 20))

        if self.update_status == True:  # si le chronomètre n'est pas lancé
            self.temps_actuel1 = str(round((time.time() - self.temps_activation), 1))
            phrase_x15 = self.font30.render(f"Temps : {self.temps_actuel1}", True, (255, 255, 255))
            screen.blit(phrase_x15, (mid_x_screen - (phrase_x15.get_width() / 2) , 150))
        else:
            self.temps_actuel1 = 0
            phrase_x15 = self.font30.render(f"Temps : {self.temps_actuel1}", True, (255, 255, 255))
            screen.blit(phrase_x15, (mid_x_screen - (phrase_x15.get_width() / 2) , 150))

    def update(self, motv, screen, tab_cara, dico, nb_mot, mid_x_screen, temps_f,x_screen):
        if self.etape == 1:
            print()

        if self.etape == 2:
            screen.blit(self.font30.render('codé par Samuel ,Thomas et Roméo', True, (255, 255, 255)), (10, 765))
            screen.blit(self.background, (0, 0))
            pygame.draw.rect(screen, self.color,
                             pygame.Rect((mid_x_screen - (self.rect_ecriture / 2)), 90, self.rect_ecriture, 50), 2)
            mot = self.font30.render("".join(self.liste), True, ((255, 255, 255)))
            phrase = []
            for values in dico.values():
                phrase.append(values)
            dico = {}
            for z in range(nb_mot):
                key = 'rect' + str(z)
                elem = phrase[z].get_rect()
                dico[key] = elem
            a = True
            m = x_screen - 200
            w = 50
            for i in range(nb_mot - 3):
                if dico[f"rect{i + 1}"].left < dico[f"rect{i}"].right:
                    dico[f"rect{i + 1}"].left = dico[f"rect{i}"].right + 10
                if dico[f"rect{i}"].right > m:
                    dico[f"rect{i}"].y += w
                    if a:
                        dico[f"rect{i}"].left = 0
                        a = False
                    else:
                        dico[f"rect{i}"].left = dico[f"rect{i - 1}"].right + 15
                        if dico[f"rect{i}"].right > m:
                            a = True
                            w += 50
                    if dico[f"rect{i + 1}"].left < dico[f"rect{i}"].right:
                        dico[f"rect{i + 1}"].left = dico[f"rect{i}"].right + 10

                screen.blit(phrase[i], (dico[f"rect{i}"].left + 70, dico[f"rect{i}"].y + 300))
            # emplacement des mots indiqués a taper
            self.temps_actuel = round((time.time() - self.temps_activation), 1)

            if len(self.liste) == 1 and self.update_status == False and self.c == 0:
                self.temps_activation = time.time()

                self.update_status = True

            self.afficher_temps(screen, mid_x_screen, temps_f)  # Affichage du chronomètre
            screen.blit(mot, (mid_x_screen - ((self.rect_ecriture - 15) / 2), 95))
            phrase_x17 = self.font30.render(f"score : {self.c} / {(nb_mot) - 3}", True, (255, 255, 255))
            screen.blit(phrase_x17, (mid_x_screen - (phrase_x17.get_width() / 2), 200))
            pygame.display.flip()
