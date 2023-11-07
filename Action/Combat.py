import random
import pygame


class Combat:
    # Défini un combat par une difficulté reliée à un tempo et les
    DIFF = {1: 30, 2: 60, 3: 90}

    def __init__(self, personne, ennemi, fenetre):
        self.difficulte = ennemi.difficulte_base
        self.personne = personne
        self.ennemi = ennemi
        self.nbEsquive = 0
        self.ecranCombat = pygame.Surface((600, 400))
        self.ecranCombat.fill("blue")
        fenetre.blit(self.ecranCombat)

    def combat(self):
        # met en place un tour de combat. Si il y a eu 2 esquives de suite, lance une attaque
        if self.est_fini():
            if(self.ennemi.vie_base == 0):
                print("le joueur à gagné")
            else:
                print("tu as perdu!")
        else:
            action = random.randint(1, 2) # 1 pour une esquive et 2 pour une attaque
            if self.nbEsquive == 2 or action == 2:
                self.nbEsquive = 0
                score = self.clique(pygame.K_a)
            else:
                self.nbEsquive += 1
                score = self.clique(pygame.K_e)
            self.calcul_score(score, action)
            self.combat()



    def clique(self, touche):
        #gere le temps du clique et retourne un score basé sur le temps mis à appuyer sur la touche.
        temps_boucle = (60000 // Combat.DIFF[self.difficulte])
        temps_phase = temps_boucle // 4
        boucle = pygame.time.Clock()
        rouge = pygame.image.load("../sprite/indicateurRougex8.png")
        orange = pygame.image.load("../sprite/indicateurOrangex8.png")
        vert = pygame.image.load("../sprite/indicateurVertx8.png")
        it = 0
        indicateur = [rouge, orange, vert]
        self.ecranCombat.blit(indicateur[it], (50, 50))
        it = (it + 1) % 3
        pygame.time.delay(temps_phase*2)
        self.ecranCombat.blit(indicateur[it], (50, 50))
        it = (it + 1) % 3
        pygame.time.delay(temps_phase)
        self.ecranCombat.blit(indicateur[it], (50, 50))
        it = (it + 1) % 3
        boucle.tick(60)
        for event in pygame.event.get():
            if touche:
                temps_clic = boucle.tick(60)
                if temps_clic < temps_phase//2:
                    return 2
                elif temps_clic < temps_phase:
                    return 1
                else:
                    return 0
            else:
                return 0


    def calcul_score(self, score, action):
        #determine les nouveaux points de vie du personnage et de l'ennemi à partir du score
        if action == 1:
            if score == 1:
                self.personne.vie_base = self.personne.vie_base - self.ennemi.attaque_base/2
            elif score == 0:
                self.personne.vie_base = self.personne.vie_base - self.ennemi.attaque_base
        else:
            if score == 2:
                self.ennemi.vie_base = self.ennemi.vie_base - self.personne.attaque_base
            elif score == 1:
                self.ennemi.vie_base = self.ennemi.vie_base - self.personne.attaque_base/2








    def est_fini(self):
        # test la fin du combat
        if self.personne.vie_base <= 0:
            return True
        elif self.ennemi.vie_base <= 0:
            return True
        else:
            return False
