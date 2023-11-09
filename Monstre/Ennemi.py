import pygame


class Ennemi:
    def __init__(self, difficulte, image_path):
        self.difficulte_base = difficulte
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
