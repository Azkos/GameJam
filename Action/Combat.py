import random
import pygame


class Combat:
    #Défini un combat par une difficulté reliée à un tempo et les
    diff = {1 : 60, 2 : 90, 3 : 120}


    def __init__(self, difficulte, personne, ennemi, fenetre):
        self.difficulte = difficulte
        self.personne = personne
        self.ennemi = ennemi
        self.nbEsquive = 0
        self.fenetre = fenetre

²


    def tour_de_combat(self):
        action = random.randrange(1)
        if self.nbEsquive == 2 or action == 1 :
            self.nbEsquive = 0
        else :
            self.nbEsquive += 1

    def est_fini(self):
        #test la fin du combat
        if self.personne.vie_base <= 0:
            return True
        elif self.ennemi.vie <= 0:
            return True
        else :
            return False

