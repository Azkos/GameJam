import pygame


class Personne:
    # Un personnage est défini par de l'attaque, de la vie, une competence, un sprite
    def __init__(self, attaque, vie, competence, image_path):
        self.attaque_base = attaque
        self.vie_base = vie
        self.competence_base = competence
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

    #TODO : infliger les dégats selon la précision
    #def damage(self, adversaire):

    #TODO :
    #def soin(self, montant):

    #TODO :
    def deplacement(self, vitesse):
        touches = pygame.key.get_pressed()
        direction = (0, 0)

        if touches[pygame.K_LEFT]:
            direction = (-vitesse, direction[1])  # Déplacer le sprite vers la gauche
        elif touches[pygame.K_RIGHT]:
            direction = (vitesse, direction[1])  # Déplacer le sprite vers la droite
        else:
            direction = (0, direction[1])

        if touches[pygame.K_UP]:
            direction = (direction[0], -vitesse)  # Déplacer le sprite vers le haut
        elif touches[pygame.K_DOWN]:
            direction = (direction[0], vitesse)  # Déplacer the sprite vers le bas
        else:
            direction = (direction[0], 0)
