import pygame
import pytmx

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
largeur, hauteur = 800, 608

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))


class GenererSalles:
    def __init__(self, nomFichier, fenetre, largeur, hauteur):
        self.nomFichier = nomFichier
        self.fenetre = fenetre
        self.largeur = largeur
        self.hauteur = hauteur

    def genererSalle(self):
        carte = pytmx.util_pygame.load_pygame(self.nomFichier)

        # Afficher la carte Tiled
        for layer in carte.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = carte.get_tile_image_by_gid(gid)
                    if tile:
                        fenetre.blit(tile, (x * carte.tilewidth, y * carte.tileheight))

        return carte
