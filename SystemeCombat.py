import pygame
import sys

class SystemeCombat:
    def __init__(self, musique, rythme):
        self.musique = musique
        self.rythme = rythme
        self.temps_dernier_rythme = 0
        self.en_rythme = False
        self.precision = 0

        # Initialisation de Pygame
        pygame.init()

        # Dimensions de la fenêtre
        self.largeur, self.hauteur = 800, 600
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption("Système de combat basé sur le rythme")

        # Couleurs
        self.blanc = (255, 255, 255)
        self.noir = (0, 0, 0)

        # Police de caractères
        self.font = pygame.font.Font(None, 36)

        # Texte d'instructions
        self.instruction_texte = self.font.render("Appuyez sur une touche au rythme du battement", True, self.blanc)

    def jouer_musique(self):
        pygame.mixer.music.load(self.musique)
        pygame.mixer.music.play()

    def mise_a_jour(self):
        temps_actuel = pygame.time.get_ticks()
        temps_depuis_dernier_rythme = temps_actuel - self.temps_dernier_rythme

        if temps_depuis_dernier_rythme >= self.rythme:
            self.en_rythme = True
            self.temps_dernier_rythme = temps_actuel
        else:
            self.en_rythme = False

        # Gérer les attaques du joueur
        touches = pygame.key.get_pressed()
        if self.en_rythme and touches[pygame.K_SPACE]:
            self.precision = 100  # Attaque réussie au bon rythme
        elif self.en_rythme:
            self.precision = 50  # Attaque effectuée, mais pas au bon rythme
        else:
            self.precision = 0  # Attaque trop tôt ou trop tard

    def afficher(self):
        self.fenetre.fill(self.noir)

        # Afficher les instructions et la précision
        self.fenetre.blit(self.instruction_texte, (self.largeur // 2 - 200, self.hauteur // 2 - 50))
        precision_texte = self.font.render(f"Précision : {self.precision}%", True, self.blanc)
        self.fenetre.blit(precision_texte, (self.largeur // 2 - 100, self.hauteur // 2 + 50))

        pygame.display.flip()

    def executer(self):
        self.jouer_musique()

        en_jeu = True
        while en_jeu:
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    en_jeu = False

            self.mise_a_jour()
            self.afficher()

        # Quitter Pygame
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    musique = 'Musique/menu.mp3'  # Remplacez par le chemin de votre musique
    rythme = 1000  # Une attaque toutes les secondes

    systeme_combat = SystemeCombat(musique, rythme)
    systeme_combat.executer()
