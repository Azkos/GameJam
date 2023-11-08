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

    # Chargement de l'image d'arrière-plan pour le menu
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

    # Vitesse de déplacement du sprite
    vitesse_deplacement = 5

    # Cartes préchargées
    cartes = {
        "SalleMainParallele": pytmx.util_pygame.load_pygame('Map/SalleMainParallele.tmx'),
        "SalleAmphiBoss": pytmx.util_pygame.load_pygame('Map/SalleAmphiBoss.tmx'),
        "SalleFace": pytmx.util_pygame.load_pygame('Map/SalleFace.tmx'),
        "SalleCours": pytmx.util_pygame.load_pygame('Map/SalleCours.tmx'),
        "SalleInfo": pytmx.util_pygame.load_pygame('Map/SalleInfo.tmx'),
    }

    # Carte actuelle
    carte_actuelle = None

    # Portes et destinations
    portes_destinations = {
        (1, 0): ('SalleAmphiBoss', (570, 32)),  # Coordonnées de la nouvelle position à ajuster
        (2, 0): ('SalleAmphiBoss', (570, 32)),
        (3, 0): ('SalleAmphiBoss', (570, 32)),
        (11, 0): ('SalleFace', (330, 500)),
        (12, 0): ('SalleFace', (330, 500)),
        (0, 6): ('SalleCours', (640, 236)),
        (0, 7): ('SalleCours', (640, 236)),
        (20, 2): ('SalleInfo', (32, 224)),
        (21, 3): ('SalleInfo', (32, 224))
    }

    # Boucle principale
    en_jeu = True
    clock = pygame.time.Clock()
    while en_jeu:
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                en_jeu = False
            if evenement.type == pygame.KEYDOWN:
                if scene_actuelle == "titre":
                    scene_actuelle = "jeu"
                    carte_actuelle = cartes["SalleMainParallele"]

        if scene_actuelle == "titre":
            fenetre.blit(fond, (0, 0))
            fenetre.blit(titre_texte, titre_texte.get_rect(center=(largeur // 2, hauteur // 2 - 50)))
            fenetre.blit(jouer_texte, jouer_texte.get_rect(center=(largeur // 2, hauteur // 2 + 50)))

        elif scene_actuelle == "jeu":
            pygame.mixer.music.stop()

            # Call the deplacement method with the speed argument
            mon_sprite.deplacement(vitesse_deplacement)
            mon_sprite.update()

            # Affichage de la carte actuelle
            for layer in carte_actuelle.visible_layers:
                for x, y, gid in layer:
                    tile = carte_actuelle.get_tile_image_by_gid(gid)
                    if tile:
                        fenetre.blit(tile, (x * carte_actuelle.tilewidth, y * carte_actuelle.tileheight))

            # Détecter la collision avec les portes et changer de carte
            # Détecter la collision avec les portes et changer de carte
            x_personnage, y_personnage = mon_sprite.rect.x // carte_actuelle.tilewidth, mon_sprite.rect.y // carte_actuelle.tileheight
            if (x_personnage, y_personnage) in portes_destinations:
                nom_carte, position = portes_destinations[(x_personnage, y_personnage)]
                print(f"Téléportation vers {nom_carte} aux coordonnées {position}")  # Instruction de débogage
                carte_actuelle = cartes[nom_carte]
                mon_sprite.rect.x, mon_sprite.rect.y = position

            # Affichage du personnage
            sprites.draw(fenetre)

            # Empêcher le personnage de sortir de la carte
            if mon_sprite.rect.left < 0:
                mon_sprite.rect.left = 0
            if mon_sprite.rect.right > largeur:
                mon_sprite.rect.right = largeur
            if mon_sprite.rect.top < 0:
                mon_sprite.rect.top = 0
            if mon_sprite.rect.bottom > hauteur:
                mon_sprite.rect.bottom = hauteur

        clock.tick(60)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
