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
        self.rect.center = (largeur // 2, hauteur // 3)  # Position initiale du sprite
        self.facing_left = False
        self.last_pos = (self.rect.x, self.rect.y)
        # Créer une hitbox aux pieds du sprite
        self.hitbox = self.rect.inflate(0, -self.rect.height * 0.8)  # Réduire la hitbox en hauteur
        self.hitbox.bottom = self.rect.bottom  # Aligner le bas de la hitbox avec le bas du sprite

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
        self.hitbox.x = self.rect.x
        self.hitbox.bottom = self.rect.bottom  # Gardez la hitbox alignée avec les pieds

    def checkCollision(self, carte, type):
        liste_collision = []

        for object in carte.objects:
            if object.type == type:
                rect = pygame.Rect(object.x, object.y, object.width, object.height)
                liste_collision.append(rect)
        # Vérifier la collision avec la hitbox
        if self.hitbox.collidelist(liste_collision) > -1:
            return True
        else:
            return False

    def checkTeleporte(self, carte, type):
        liste_collision = []

        for object in carte.objects:
            if object.type == type:
                rect = pygame.Rect(object.x, object.y, object.width, object.height)
                liste_collision.append((rect, object.name))
        id_collision = self.rect.collidelist(liste_collision)
        if id_collision > -1:
            return liste_collision[id_collision][1]
        else:
            return False

