

class Combat:
    #Défini un combat par une difficulté reliée à un tempo et les
    diff = {1 : 60, 2 : 90, 3 : 120}


    def __init__(self, difficulte, personne, ennemi):
        self.difficulte = difficulte
        self.personne = personne
        self.ennemi = ennemi


    def tour_de_combat(self):

    def est_fini(self):
        #test la fin du combat
        if self.personne.vie_base <= 0:
            return True
        elif self.ennemi.vie <= 0:
            return True
        else :
            return False

