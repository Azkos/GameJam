import random
import pygame

import Monstre.Ennemi
import Personnage.Personne

#Classe en stand-by, plus utilisée pour l'instant

class Combat:
    # Défini un combat par une difficulté reliée à un tempo et les
    DIFF = {1: 10, 2: 20, 3: 30}

    def __init__(self, personne: Personnage.Personne, ennemi: Monstre.Ennemi, fenetre: pygame.display):
        self.personne = personne
        self.ennemi = ennemi
        self.difficulte = ennemi.difficulte_base
        self.nbEsquive = 0
        self.ecranCombat = pygame.Surface((600, 400))
        self.ecranCombat.fill("blue")
        self.fenetre = fenetre
        self.fenetre.blit(self.ecranCombat, (100, 100))
        pygame.display.flip()

    def combat(self):
        # met en place un tour de combat. Si il y a eu 2 esquives de suite, lance une attaque
        if self.est_fini():
            if self.ennemi.vie_base <= 0:
                print("tu as gagné le combat!")
            else:
                print("tu as perdu!")
        else:
            action = random.randint(1, 2)  # 1 pour une esquive et 2 pour une attaque
            if self.nbEsquive == 2 or action == 2:
                self.nbEsquive = 0
                score = self.clique(pygame.K_a)
            else:
                self.nbEsquive += 1
                score = self.clique(pygame.K_e)
            self.calcul_score(score, action)
            self.combat()

    def clique(self, touche):
        # gere le temps du clique et retourne un score basé sur le temps mis à appuyer sur la touche.
        self.ecranCombat.fill("blue")
        temps_boucle = (60000 // Combat.DIFF[self.difficulte])
        temps_phase = temps_boucle // 4
        boucle = pygame.time.Clock()
        rouge = pygame.image.load("sprite/indicateurRougex8.png")
        orange = pygame.image.load("sprite/indicateurOrangex8.png")
        vert = pygame.image.load("sprite/indicateurVertx8.png")
        font = pygame.font.Font(None, 36)
        if touche == pygame.K_e:
            touche_texte = font.render("Appuyer sur la touche 'E'", True, (255, 255, 255))
        else:
            touche_texte = font.render("Appuyer sur la touche 'A'", True, (255, 255, 255))
        self.ecranCombat.blit(touche_texte, (200, 50))
        indicateur = [rouge, orange, vert]
        boucle.tick(60)
        self.ecranCombat.blit(indicateur[0], (50, 50))
        self.fenetre.blit(self.ecranCombat, (100, 50))
        pygame.display.flip()
        pygame.time.delay(temps_phase * 2)
        self.ecranCombat.blit(indicateur[1], (50, 50))
        self.fenetre.blit(self.ecranCombat, (100, 50))
        pygame.display.flip()
        pygame.time.delay(temps_phase)
        self.ecranCombat.blit(indicateur[2], (50, 50))
        self.fenetre.blit(self.ecranCombat, (100, 50))
        pygame.display.flip()
        res = 0
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                touches = pygame.key.get_pressed()
                temps_clic = boucle.tick(60)
                if touches[touche]:
                    if temps_clic < temps_phase // 2:
                        res = 2
                    elif temps_clic < temps_phase:
                        res = 1
        pygame.time.delay(temps_phase)
        pygame.display.update()
        print(res)
        return res


    def calcul_score(self, score, action):
        # determine les nouveaux points de vie du personnage et de l'ennemi à partir du score
        if action == 1:
            if score == 1:
                self.personne.vie_base = self.personne.vie_base - self.ennemi.attaque_base / 2
            elif score == 0:
                self.personne.vie_base = self.personne.vie_base - self.ennemi.attaque_base
        else:
            if score == 2:
                self.ennemi.vie_base = self.ennemi.vie_base - self.personne.attaque_base
            elif score == 1:
                self.ennemi.vie_base = self.ennemi.vie_base - self.personne.attaque_base / 2
        print("Perso : " + str(self.personne.vie_base) + "; Ennemi : " + str(self.ennemi.vie_base))

    def est_fini(self):
        # test la fin du combat
        if self.personne.vie_base <= 0:
            return True
        elif self.ennemi.vie_base <= 0:
            return True
        else:
            return False
