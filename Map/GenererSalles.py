import pygame
import pytmx

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
largeur, hauteur = 800, 600

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))

# Charger la carte Tiled
carte = pytmx.load_pygame("") # Mettre La premiere carte

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Afficher la carte Tiled
    for layer in carte.layers:
        if layer.visible:
            for x, y, gid in layer:
                tile = carte.get_tile_image_by_gid(gid)
                if tile:
                    fenetre.blit(tile, (x * carte.tilewidth, y * carte.tileheight))

    pygame.display.flip()

# Quitter Pygame
pygame.quit()
