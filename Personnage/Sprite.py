import pygame

largeur = 600
hauteur = 800

sprite_walk1 = pygame.image.load("sprite/perso1.png")
sprite_walk1 = pygame.transform.scale(sprite_walk1, (sprite_walk1.get_width() // 4, sprite_walk1.get_height() // 4))


class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = sprite_walk1
        self.rect = self.image.get_rect()
        self.rect.center = (largeur // 2, hauteur // 3)  # Position initiale du sprite
        self.facing_left = False
        self.last_pos = (self.rect.x, self.rect.y)

        # Créer une hitbox aux pieds du sprite (réduite sur les côtés)
        self.hitbox = pygame.Rect(self.rect.x + self.rect.width * 0.2,  # Décalage à droite
                                  self.rect.y,  # Même position en Y
                                  self.rect.width * 0.6,  # Largeur réduite
                                  self.rect.height * 0.2)  # Hauteur réduite
        self.hitbox.bottom = self.rect.bottom  # Aligner le bas de la hitbox avec le bas du sprite

    def deplacement(self, vitesse):
        touches = pygame.key.get_pressed()
        direction = [0, 0]

        if touches[pygame.K_LEFT]:
            if not self.facing_left:
                self.image = pygame.transform.flip(self.image, True, False)
                self.facing_left = True
            direction[0] = -vitesse
        elif touches[pygame.K_RIGHT]:
            if self.facing_left:
                self.image = pygame.transform.flip(self.image, True, False)
                self.facing_left = False
            direction[0] = vitesse

        if touches[pygame.K_UP]:
            direction[1] = -vitesse
        elif touches[pygame.K_DOWN]:
            direction[1] = vitesse

        self.last_pos = (self.rect.x, self.rect.y)
        self.rect.x += direction[0]
        self.rect.y += direction[1]
        self.hitbox.x = self.rect.x + (self.rect.width * 0.2 if self.facing_left else 0)  # Ajuster le X en fonction du décalage à droite
        self.hitbox.bottom = self.rect.bottom

    def checkCollision(self, carte, type):
        liste_collision = []

        for obj in carte.objects:
            if obj.type == type:
                rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                liste_collision.append(rect)

        if self.hitbox.collidelist(liste_collision) > -1:
            return True
        else:
            return False

    def checkTeleporte(self, carte, type):
        liste_collision = []
        liste_nom = []

        for obj in carte.objects:
            if obj.type == type:
                rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                liste_collision.append(rect)
                liste_nom.append(obj.name)

        id_collision = self.rect.collidelist(liste_collision)
        if id_collision > -1:
            return "Map/" + liste_nom[id_collision]
        else:
            return False
