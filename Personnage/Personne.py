# Création de la classe "informatique"

import pygame

class Personne:

    # Un personnage est défini par de l'attaque et de la vie
    def __init__(self, attaque, vie, competence):
        self.attaque_base = attaque
        self.vie_base = vie
        self.competence_base = competence

