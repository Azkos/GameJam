import pygame

largeur = 600
hauteur = 800
sprite_walk1 = pygame.image.load("sprite/chara-walk1.png")
sprite_walk2 = pygame.image.load("sprite/chara-walk2.png")

sprite_walk1 = pygame.transform.scale(sprite_walk1, (sprite_walk1.get_width() // 5, sprite_walk1.get_height() // 5))
sprite_walk2 = pygame.transform.scale(sprite_walk2, (sprite_walk2.get_width() // 2, sprite_walk2.get_height() // 2))


class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = sprite_walk1
        self.rect = self.image.get_rect()
        self.rect.center = (largeur // 2, hauteur // 2)  # Position initiale du sprite
        self.facing_left = False
        self.last_pos = (self.rect.x, self.rect.y)

    def deplacement(self, vitesse):
        touches = pygame.key.get_pressed()
        direction = [0, 0]

        if touches[pygame.K_LEFT]:
            if not self.facing_left:  # Si le sprite regarde vers la droite, inverser l'image une fois
                self.image = pygame.transform.flip(self.image, True, False)
                self.facing_left = True
            direction[0] = -vitesse  # Déplacer le sprite vers la gauche
        elif touches[pygame.K_RIGHT]:
            if self.facing_left:  # Si le sprite regarde vers la gauche, rétablir l'image normale
                self.image = pygame.transform.flip(self.image, True, False)
                self.facing_left = False
            direction[0] = vitesse  # Déplacer le sprite vers la droite

        if touches[pygame.K_UP]:
            direction[1] = -vitesse  # Déplacer le sprite vers le haut
        elif touches[pygame.K_DOWN]:
            direction[1] = vitesse  # Déplacer le sprite vers le bas

            # Mettre à jour la position du sprite en fonction de la direction
        self.last_pos = (self.rect.x, self.rect.y)
        self.rect.x += direction[0]
        self.rect.y += direction[1]

    def checkCollision(self, carte):
        liste_collision = []

        for object in carte.objects:
            if object.type == "collision":
                rect = pygame.Rect(object.x, object.y, object.width, object.height)
                liste_collision.append(rect)
        if self.rect.collidelist(liste_collision) > -1:
            return True
        else:
            return False
