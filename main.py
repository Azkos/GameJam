import pygame
import sys
import pytmx

from Personnage.Informatique import Informatique
from Personnage.Sprite import Sprite
import Action.Combat as comb
from Monstre.Ennemi import Ennemi
from Monstre.ProfZombie import ProfZombie


def main():
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
    scene_actuelle = "titre"

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


            mon_sprite.deplacement(5)

            mon_sprite.update()
            fenetre.blit(mon_sprite.image, mon_sprite.rect)

            carte = pytmx.util_pygame.load_pygame('Map/SalleMain.tmx')

            # Afficher la carte Tiled
            for layer in carte.visible_layers:
                for x, y, gid in layer:
                    tile = carte.get_tile_image_by_gid(gid)
                    if tile:
                        fenetre.blit(tile, (x * carte.tilewidth, y * carte.tileheight))

            sprites.draw(fenetre)
        clock.tick(60)

        pygame.display.flip()

    # Quitter Pygame
    pygame.quit()
    sys.exit()


main()
