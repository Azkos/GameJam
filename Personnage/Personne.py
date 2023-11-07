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


