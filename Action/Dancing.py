import random
import pygame

import Monstre.Ennemi


class Dancing:
    # défini un challenge de dance lancé par les ennemis
    KEY_POOL = [pygame.K_a, pygame.K_z, pygame.K_e, pygame.K_r]
    DIFF = {1: 20, 2: 40, 3: 80}

    def __init__(self, perso, ennemi, fenetre):
        self.personne = perso
        self.ennemi = ennemi
        self.difficulte = ennemi.difficulte_base
        self.ecranCombat = pygame.Surface((600, 400))
        self.fenetre = fenetre
        self.fenetre.blit(self.ecranCombat, (100, 100))
        pygame.display.flip()

    def dance(self):
        #créé la dance et retourne True si la danse a été gagné et False sinon
        boucle = pygame.time.Clock()
        key_seq = []
        score = 0
        font = pygame.font.Font(None, 36)
        for i in range(Dancing.DIFF[self.difficulte]):
            key_seq.append(Dancing.KEY_POOL[random.randint(0, len(Dancing.KEY_POOL) - 1)])
        rouge = pygame.image.load("sprite/indicateurRougex8.png")
        orange = pygame.image.load("sprite/indicateurOrangex8.png")
        vert = pygame.image.load("sprite/indicateurVertx8.png")
        validation = pygame.mixer.Sound("Musique/validation.mp3")
        erreur = pygame.mixer.Sound("Musique/erreur.mp3")
        indicateur = orange
        for touche in key_seq:
            self.ecranCombat.fill("blue")
            touche_texte = font.render("Appuyer sur la touche '" + chr(touche) + "'", True, (255, 255, 255))
            self.ecranCombat.blit(touche_texte, (200, 50))
            self.ecranCombat.blit(indicateur, (260, 260))
            self.ecranCombat.blit(self.personne.image, (50, 50))
            self.ennemi.image = pygame.transform.flip(pygame.transform.scale(self.ennemi.image, (100, 100)),True, False)
            self.ecranCombat.blit(self.ennemi.image, (350, 100))
            self.fenetre.blit(self.ecranCombat, (100, 100))
            pygame.display.flip()
            wait = True
            while wait:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        touches = pygame.key.get_pressed()
                        if touches[touche]:
                            score += 1
                            indicateur = vert
                            validation.play(1, 1000)
                            self.personne.image = pygame.transform.flip(self.personne.image, True, False)
                            self.personne.facing_left = not self.personne.facing_left
                        else:
                            score -= 1
                            indicateur = rouge
                            erreur.play(1, 500)
                        wait = False
                    elif event.type == pygame.QUIT:
                        pygame.quit()
        temps = boucle.tick(60)
        score = score + (Dancing.DIFF[self.difficulte] - temps // 1000)
        return self.resultat(score)

    def resultat(self, score):
        #retourne True si le score est supérieur à la difficulté et False sinon
        print("score : " + str(score))
        if score < Dancing.DIFF[self.difficulte]:
            return False
        else:
            return True
