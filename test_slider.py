from pygame import *


class Slider:  # La classe du slider

    def __init__(self,
                 size,  # La taille du slider (de type tuple : (x, y))
                 bg_color,  # La couleur du fond du slider (de type tuple : (r, g, b))
                 slide_color,  # La couleur du "slide" du slider (de type tuple : (r, g, b))
                 cursor_color,  # La couleur du curseur du "slide" (de type tuple : (r, g, b))
                 val_color,  # La couleur de la valeur affichée sur le curseur (de type : (r, g, b))
                 min_val,  # La valeur minimale du slider (de type int)
                 max_val,  # La valeur maximale du slider (de type int)
                 margin_x,  # La marge en x entre le "slide" et les bords du slider (de type float)
                 margin_y,  # La marge en y entre le "slide" et les bords du slider (de type float)
                 hover_light):  # Est-ce que le slider doit avoir de la surbrillance quand on passe la souris dessus ? (de type bool)

        self.surface = Surface(size)  # La surface est le rendu du slider qui sera affiché
        self.hover_light = hover_light  # Est-ce que le slider doit avoir de la surbrillance quand on passe la souris dessus ?
        self.bg_color = bg_color  # La couleur du fond
        self.surface.fill(self.bg_color)  # On remplie la surface avec la couleur du fond
        self.display_rect = self.surface.get_rect().copy()  # Ce rectangle servira pour l'affichage du slider
        self.max_ran = 0  # Les coordonnées maximales du slider qui sera définie dans click()
        self.min_ran = 0  # Les coordonnées minimales du slider qui sera définie dans click()
        self.cursor_pos = 0, 0  # Les coordonnées du curseur
        self.min_val = min_val  # La valeur minimale du slider
        self.max_val = max_val  # La valeur maximale du slider
        self.value = self.min_val  # La valeur actuelle du slider (par défaut sur la valeur minimale)
        self.horizontal = size[0] >= size[1]  # Est-ce que le slider est horizontal (c'est un booléen)
        self.slide_color = slide_color  # La couleur du "slide"
        self.val_color = val_color  # La couleur de la valeur du curseur
        self.cursor_color = cursor_color  # La couleur du curseur
        self.margin_x = margin_x  # La marge en x
        self.margin_y = margin_y  # La marge en y
        self.slide = Surface(self.surface.get_rect().inflate(- self.margin_x,
                                                             - self.margin_y).size)  # La "slide" du silder qui est une surface de taille réduite par rapport au slider en fonction des marges avec "inflate"
        self.slide.fill(self.slide_color)  # On remplie la "slide" avec sa couleur
        self.cursor = Surface((self.slide.get_height(),) * 2 if self.horizontal else (
                                                                                     self.slide.get_width(),) * 2)  # Le curseur est un carré de la largeur de la "slide", qui change en fonction de self.horizontal
        self.cursor.fill(cursor_color)  # On remplie le curseur avec sa couleur
        self.display(
            True)  # On appelle click() avec True pour le forcer à s'exécuter même si la souris n'a pas été cliquée

    def is_hovered(self):  # Est-ce que la souris passe dessus le slider ? (renvoi un booléen)
        return self.display_rect.collidepoint(mouse.get_pos())

    def is_clicked(self):  # Est-ce que la souris à cliqué sur le slider ? (renvoi un booléen)
        return self.is_hovered() and (mouse.get_pressed()[0] or mouse.get_pressed()[2])

    def display(self,  # Action à faire pour créer l'affichage du slider
                force=False):  # Force l'affiche même si le slider n'a pas été cliqué (de type bool) (par défaut à False)

        if not (
                self.is_clicked() or force):  # Si la souris n'a pas cliqué sur le slider OU On ne force pas le display avec force
            return  # On arrête l'exécution de la méthode

        self.slide.fill(self.slide_color)  # On reset la "slide" en le remplissant de sa couleur
        mouse_pos = mouse.get_pos()  # On prend les coordonnées de la souris
        mouse_pos = (0, 0) if force else (mouse_pos[0] - self.display_rect.x - self.margin_x / 2, mouse_pos[
            1] - self.display_rect.y - self.margin_y / 2)  # On calcul les coordonées de la souris dans le slider (si force == True alors elles sont mises à 0)
        self.cursor_pos = self.slide.get_rect().center  # On défini les coordonnées du curseur
        self.cursor_pos = (mouse_pos[0], self.cursor_pos[1]) if self.horizontal else (self.cursor_pos[0], mouse_pos[
            1])  # On redéfinit les coordonnées du curseur en fonction de la position de la souris
        temp = self.display_rect.inflate(- self.margin_x, - self.margin_y)  # Donne un rectangle représentant la "slide"
        self.max_ran = temp.x - self.display_rect.x + temp.width - self.margin_x / 2 - self.cursor.get_width() / 2 if self.horizontal else temp.y - self.display_rect.y + temp.height + self.margin_y / 2 - self.cursor.get_height() / 2  # On calcule les coordonnées minimales de la "slide"
        self.min_ran = temp.x - self.display_rect.x - self.margin_x / 2 + self.cursor.get_width() / 2 if self.horizontal else temp.y - self.display_rect.y + self.margin_y / 2 + self.cursor.get_height() / 2  # On calcule les coordonnées maximales de la "slide"
        if self.horizontal:  # Si le slider est horizontal
            if mouse_pos[0] > self.max_ran:  # Si la souris est en dehors des coordonnées maximales
                self.cursor_pos = self.max_ran, self.cursor_pos[
                    1]  # On replace le curseur (pour éviter que le curseur ne sorte du slider ce qui n'aurait aucun sens)
            elif mouse_pos[0] < self.min_ran:  # Si la souris est en dehors des coordonnées minimales
                self.cursor_pos = self.min_ran, self.cursor_pos[1]  # On replace le curseur
        else:  # Sinon (si le slider est verical)
            if mouse_pos[1] > self.max_ran:  # On fait tout pareil qu'en haut mais en vertical
                self.cursor_pos = self.cursor_pos[0], self.max_ran
            elif mouse_pos[1] < self.min_ran:
                self.cursor_pos = self.cursor_pos[0], self.min_ran
        temp = self.max_ran - self.min_ran  # On définit une valeur temporaire qui est égale à la différence entre le maximum et le mininum de la "silde"
        temp_ = temp - (self.max_ran - self.cursor_pos[0] if self.horizontal else self.max_ran - self.cursor_pos[
            1])  # On définit une autre valeur temporaire qui est égale à la différence de coordonnées entre le curseur et le maximum
        self.value = round(temp_ / temp * (
                    self.max_val - self.min_val) + self.min_val)  # On calcul la valeur du slider en fonction des deux variables temp et temp_ en haut, en prenant en compte la valeur minimale et maximale du slider
        self.cursor.fill(self.cursor_color)  # On reset le curseur en le remplissant de sa couleur
        render = font.Font(None, round(self.cursor.get_width() / 2)).render(str(self.value), True,
                                                                            self.val_color)  # On crée une surface qui affiche la valeur du slider
        self.cursor.blit(render, render.get_rect(
            center=self.cursor.get_rect().center))  # On place cette valeur au centre du curseur
        self.slide.blit(self.cursor, self.cursor.get_rect(
            center=self.cursor_pos))  # On place le curseur dans la "slide" à la bonne position
        self.surface.blit(self.slide, self.slide.get_rect(
            center=self.surface.get_rect().center))  # On place la "slide" dans le slider

    def update(self,  # Permet d'afficher le slider à l'écran
               screen,  # L'écran où on doit l'afficher (de type pygame.Surface)
               x,  # La coordonnée x où on doit afficher le slider
               y):  # La coordonnée y où on doit afficher le slider

        self.display()  # On crée l'affichage du slider

        self.display_rect = self.surface.get_rect().copy()  # On met à jour son rectangle qui permet de l'afficher
        self.display_rect.x = x  # On met les bonnes coordonnées dans le rectangle
        self.display_rect.y = y
        screen.blit(self.surface,
                    self.display_rect)  # On affiche la surface du slider sur le screen grace à son display_rect
        if self.is_hovered() and self.hover_light:  # Si le slider est surpassé par le souris est si la lumière de surbrillance est activée
            light = Surface(self.display_rect.size)  # On crée une surface de surbrillance de la taille du slider
            light.fill((255, 255, 255))  # On la remplie en blanc
            light.set_alpha(128)  # On la met à moitié transparente
            screen.blit(light, self.display_rect)  # On l'ajoute par dessus le slider


# Exemple d'exécution :

init()  # Démarrage de pygame

display.set_caption("Wordpy")  # Création du display
screen = display.set_mode((1920 / 2, 1080 / 2))  # Création de la fenêtre "screen" en plein écran

size = (600, 100)
bg_color = (23, 89, 156)  # Bleu
slide_color = (35, 35, 35)  # Gris foncé
cursor_color = (128, 128, 128)  # Gris
val_color = (255, 255, 255)  # Blanc
min_val = 0  # Valeur minimale = 10
max_val = 30  # Valeur maximale = 100
margin_x = 30  # La marge x est de 30
margin_y = 30  # La marge y est de 30
hover_light = False  # La surbrillance est activée

slider_test = Slider(size, bg_color, slide_color, cursor_color, val_color, min_val, max_val, margin_x, margin_y,
                     hover_light)

run = True
while run:

    slider_test.update(screen, screen.get_width() / 2 - slider_test.surface.get_width() / 2,
                       screen.get_height() / 2 - slider_test.surface.get_height() / 2)
    display.flip()

    for e in event.get():  # Détection des events de pygame

        if e.type == QUIT:  # Permet de fermer la fenêtre quand on clique sur la croix rouge
            quit()
            run = False
