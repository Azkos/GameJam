import pygame
import sys
import pytmx

from Personnage.Informatique import Informatique
from Personnage.Sprite import Sprite
from Map.GenererSalles import GenererSalles


def afficher_dialogue(fenetre, font, dialogues, dialogue_index, largeur, hauteur, blanc):
    # Affiche la boîte de dialogue avec le texte actuel
    pygame.draw.rect(fenetre, (0, 0, 0), (50, hauteur - 150, largeur - 100, 100))
    texte_dialogue = font.render(dialogues[dialogue_index], True, blanc)
    fenetre.blit(texte_dialogue, (60, hauteur - 140))

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
    scene_actuelle = "titre"
    dialogue_actif = False
    dialogues = [
        "Bonjour, je suis un pingouin !",
        "C'est un beau jour pour une aventure !",
        "N'oubliez pas d'apporter votre équipement !"
    ]
    dialogue_index = 0

    # Création du personnage
    mon_sprite = Sprite()
    sprites = pygame.sprite.Group(mon_sprite)

    # Cartes préchargées
    cartes = {
        "SalleMain": pytmx.util_pygame.load_pygame('Map/SalleMain.tmx'),
        "SalleMainParallele": pytmx.util_pygame.load_pygame('Map/SalleMainParallele.tmx'),
        "SalleAmphiBoss": pytmx.util_pygame.load_pygame('Map/SalleAmphiBoss.tmx'),
        "SalleFace": pytmx.util_pygame.load_pygame('Map/SalleFace.tmx'),
        "SalleCours": pytmx.util_pygame.load_pygame('Map/SalleCours.tmx'),
        "SalleInfo": pytmx.util_pygame.load_pygame('Map/SalleInfo.tmx'),
    }

    # Portes et destinations pour toutes les cartes
    portes_destinations = {
        "SalleMainParallele": {
            (3, 1): ('SalleAmphiBoss', (570, 32)),
            (4, 1): ('SalleAmphiBoss', (570, 32)),
            (5, 1): ('SalleAmphiBoss', (570, 32)),
            (12, 1): ('SalleFace', (330, 500)),
            (13, 1): ('SalleFace', (330, 500)),
            (0, 7): ('SalleCours', (640, 236)),
            (0, 8): ('SalleCours', (640, 236)),
            (23, 4): ('SalleInfo', (32, 224)),
            (23, 5): ('SalleInfo', (32, 224)),
        },
        "SalleAmphiBoss": {
            (23, 4): ("SalleMainParallele", (100, 100)),
            (23, 5): ("SalleMainParallele", (100, 100)),
        },
        "SalleFace": {
            (8, 5): ("SalleMainParallele", (200, 200)),
        },
        "SalleCours": {
            (23, 7): ("SalleMainParallele", (300, 300)),
            (23, 8): ("SalleMainParallele", (300, 300)),
        },
        "SalleInfo": {
            (15, 7): ("SalleMainParallele", (400, 400)),
        },
    }

    # Carte actuelle
    carte_actuelle_nom = "SalleMain"
    carte_actuelle = cartes[carte_actuelle_nom]

    # Boucle principale
    en_jeu = True
    clock = pygame.time.Clock()
    while en_jeu:
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                en_jeu = False
            elif evenement.type == pygame.KEYDOWN:
                if scene_actuelle == "titre" and evenement.key == pygame.K_SPACE:
                    scene_actuelle = "jeu"
                    carte_actuelle_nom = "SalleMain"
                    carte_actuelle = cartes[carte_actuelle_nom]
                elif dialogue_actif and evenement.key == pygame.K_SPACE:
                    dialogue_index += 1
                    if dialogue_index >= len(dialogues):
                        dialogue_actif = False
                        dialogue_index = 0
                        carte_actuelle_nom = "SalleMainParallele"
                        carte_actuelle = cartes[carte_actuelle_nom]

        if scene_actuelle == "titre":
            # Afficher l'arrière-plan de l'écran de titre
            fenetre.blit(fond, (0, 0))
            fenetre.blit(titre_texte, titre_texte.get_rect(center=(largeur // 2, hauteur // 2 - 50)))
            fenetre.blit(jouer_texte, jouer_texte.get_rect(center=(largeur // 2, hauteur // 2 + 50)))

        elif scene_actuelle == "jeu":

            pygame.mixer.music.stop()

            genererSalle = GenererSalles("Map/SalleMain.tmx", fenetre, largeur, hauteur)
            carte = genererSalle.genererSalle()

            mon_sprite.deplacement(8)
            if mon_sprite.checkCollision(carte):
                mon_sprite.rect.x = mon_sprite.last_pos[0]
                mon_sprite.rect.y = mon_sprite.last_pos[1]

            fenetre.blit(mon_sprite.image, mon_sprite.rect)

            carte = pytmx.util_pygame.load_pygame('Map/SalleMain.tmx')

            # Afficher le nom du personnage en haut à gauche
            nom_personnage_texte = font.render(nom_personnage, True, blanc)
            fenetre.blit(nom_personnage_texte, (10, 10))  # Position du texte
            # Affichage de la carte actuelle
            if carte_actuelle:
                for layer in carte_actuelle.visible_layers:
                    for x, y, gid in layer:
                        tile = carte_actuelle.get_tile_image_by_gid(gid)
                        if tile:
                            fenetre.blit(tile, (x * carte_actuelle.tilewidth, y * carte_actuelle.tileheight))

            # Interaction avec le pingouin sur la carte "SalleMain"
            if carte_actuelle_nom == "SalleMain":
                pingouin_rect = pygame.Rect(350, 320, 32, 32)  # Rectangle fictif pour le pingouin
                if mon_sprite.rect.colliderect(pingouin_rect):
                    dialogue_actif = True

            # Affichage du dialogue si actif
            if dialogue_actif:
                afficher_dialogue(fenetre, font, dialogues, dialogue_index, largeur, hauteur, blanc)

            # Détecter la collision avec les portes et changer de carte
            if not dialogue_actif and carte_actuelle_nom in portes_destinations:
                x_personnage, y_personnage = mon_sprite.rect.x // carte_actuelle.tilewidth, mon_sprite.rect.y // carte_actuelle.tileheight
                if (x_personnage, y_personnage) in portes_destinations[carte_actuelle_nom]:
                    nom_carte, position = portes_destinations[carte_actuelle_nom][(x_personnage, y_personnage)]
                    carte_actuelle_nom = nom_carte
                    carte_actuelle = cartes[nom_carte]
                    mon_sprite.rect.x, mon_sprite.rect.y = position

            # Affichage du personnage
            sprites.draw(fenetre)
        print(clock)
        clock.tick(60)

        pygame.display.flip()

    # Quitter Pygame
    pygame.quit()
    sys.exit()


main()