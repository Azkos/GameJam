import pygame


class Ennemi:
    def __init__(self, attaque, vie, difficulte, image_path):
        self.attaque_base = attaque
        self.vie_base = vie
        self.difficulte_base = difficulte
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

