import pygame
import sys

from Personnage.Sprite import Sprite
from Map.GenererSalles import GenererSalles


def main():
    if len(sys.argv) > 1:
        nom_personnage = "Nom : " + sys.argv[1]
    else:
        nom_personnage = "Nom du personnage par défaut"

    # Initialisation de Pygame
    pygame.init()

    # Dimensions de la fenêtre
    largeur, hauteur = 800, 600
    fenetre = pygame.display.set_mode((largeur, hauteur))
    pygame.display.set_caption("Nom du jeu")

    # Couleurs
    blanc = (255, 255, 255)

    # Police de caractères
    font = pygame.font.Font(None, 36)

    # Chargez l'image d'arrière-plan pour le menu
    fond = pygame.image.load("image/v_iut2-rentree-2023_1696500078894-jpg (2)_120x80.png")
    fond = pygame.transform.scale(fond, (largeur, hauteur))

    # Texte de l'écran de titre
    titre_texte = font.render("Mon Jeu", True, blanc)
    jouer_texte = font.render("Appuyez sur une touche pour commencer le jeu", True, blanc)

    # Musique de l'écran de titre
    pygame.mixer.music.load('Musique/menu.mp3')
    pygame.mixer.music.play(-1)

    # Variable d'état de la scène
    scene_actuelle = "jeu"

    # Création du personnage
    mon_sprite = Sprite()
    sprites = pygame.sprite.Group(mon_sprite)

    # Boucle principale
    en_jeu = True
    clock = pygame.time.Clock()  # Créez une horloge pour contrôler la fréquence de rafraîchissement
    while en_jeu:
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                en_jeu = False
            if evenement.type == pygame.KEYDOWN:
                if scene_actuelle == "titre":
                    scene_actuelle = "jeu"  # Passer à la scène de jeu lorsque n'importe quelle touche est enfoncée

        if scene_actuelle == "titre":
            # Afficher l'arrière-plan de l'écran de titre
            fenetre.blit(fond, (0, 0))

            # Afficher le texte de l'écran de titre
            titre_rect = titre_texte.get_rect(center=(largeur // 2, hauteur // 2 - 50))
            jouer_rect = jouer_texte.get_rect(center=(largeur // 2, hauteur // 2 + 50))

            fenetre.blit(titre_texte, titre_rect)
            fenetre.blit(jouer_texte, jouer_rect)

        elif scene_actuelle == "jeu":

            pygame.mixer.music.stop()

            genererSalle = GenererSalles("Map/SalleMain.tmx", fenetre, largeur, hauteur)
            carte = genererSalle.genererSalle()

            mon_sprite.deplacement(8)
            if mon_sprite.checkCollision(carte):
                mon_sprite.rect.x = mon_sprite.last_pos[0]
                mon_sprite.rect.y = mon_sprite.last_pos[1]

            fenetre.blit(mon_sprite.image, mon_sprite.rect)


            # Afficher le nom du personnage en haut à gauche
            nom_personnage_texte = font.render(nom_personnage, True, blanc)
            fenetre.blit(nom_personnage_texte, (10, 10))  # Position du texte

            sprites.draw(fenetre)
        clock.tick(60)

        pygame.display.flip()

    # Quitter Pygame
    pygame.quit()
    sys.exit()


main()
