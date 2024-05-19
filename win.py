from Game import Game
import pygame, time


class Win(Game()):
    def __init__(self):
        self.run = False
        self.screen = pygame.display.set_mode((1920, 1080))
        self.font = pygame.font.Font("arial.ttf", 30)
        self.color = (255, 255, 255)
        self.colorwin = (0, 255, 0)
        self.background = pygame.image.load("doc/background.jpg")  # Définition de l'image de background
        self.score = self.c
        self.score_en_pourcentage = (self.c * nb_de_mots) * 100
        self.confettie = pygame.image.load("doc/confetti.gif")

    def update(self, motv, screen, tab_cara):
        screen.blit(self.background, (0, 0))
        if self.score_en_pourcentage == 100:
            self.text = font.render("You win !", True, BLACK)
            screen.blit(self.text, (100, 200))
        if self.score_en_pourcentage >= 50:
            self.text = font.render("you're good", True, BLACK)
            screen.blit(self.text, (100, 200))
        if self.score_en_pourcentage <= 50 and score > 10
            self.text = font.render("you can do better", True, BLACK)
            screen.blit(self.text, (100, 200))
        else:
            self.text = font.render("you're a piece of shit", True, BLACK)
            screen.blit(self.text, (100, 200))
        screen.blit(self.score_en_pourcentage, (150, 200))
        screen.blit(self.confettie, (100, 200))

        pygame.display.flip()



