import pygame

largeur = 600
hauteur = 800
sprite_walk1 = pygame.image.load("sprite/pinguin.png")


class Sprite(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = sprite_walk1
        self.rect = self.image.get_rect()
        self.rect.center = (largeur // 2, hauteur // 2)  # Position initiale du sprite

    def deplacement(self, vitesse):
        touches = pygame.key.get_pressed()
        direction = [0, 0]

        if touches[pygame.K_LEFT]:
            direction[0] = -vitesse  # Déplacer le sprite vers la gauche
        elif touches[pygame.K_RIGHT]:
            direction[0] = vitesse  # Déplacer le sprite vers la droite

        if touches[pygame.K_UP]:
            direction[1] = -vitesse  # Déplacer le sprite vers le haut
        elif touches[pygame.K_DOWN]:
            direction[1] = vitesse  # Déplacer le sprite vers le bas

        # Mettre à jour la position du sprite en fonction de la direction
        self.rect.x += direction[0]
        self.rect.y += direction[1]

