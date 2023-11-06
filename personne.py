# Création de la classe "informatique"

import pygame

class Personne:

    # Un personnage est défini par de l'attaque et de la vie
    def __init__(self, attaque, vie):
        self.attaque_base = attaque
        self.vie_base = vie

