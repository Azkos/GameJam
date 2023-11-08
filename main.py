import pygame
import sys
import pytmx

from Personnage.Informatique import Informatique
from Personnage.Sprite import Sprite
import Action.Combat as comb
import Action.Dancing as dan
from Monstre.Ennemi import Ennemi
from Monstre.ProfZombie import ProfZombie

def afficher_dialogue(fenetre, font, dialogues, dialogue_index, largeur, hauteur, blanc):
    # Affiche la boîte de dialogue avec le texte actuel
    pygame.draw.rect(fenetre, (0, 0, 0), (50, hauteur - 150, largeur - 100, 100))
    texte_dialogue = font.render(dialogues[dialogue_index], True, blanc)
    fenetre.blit(texte_dialogue, (60, hauteur - 140))

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

    # Vitesse de déplacement du sprite
    vitesse_deplacement = 5

    parallele = pytmx.util_pygame.load_pygame('Map/SalleMainParallele.tmx')
    # Cartes préchargées
    cartes = {
        "SalleMainParallele": parallele,
        "SalleAmphiBoss": pytmx.util_pygame.load_pygame('Map/SalleAmphiBoss.tmx'),
        "SalleFace": pytmx.util_pygame.load_pygame('Map/SalleFace.tmx'),
        "SalleCours": pytmx.util_pygame.load_pygame('Map/SalleCours.tmx'),
        "SalleInfo": pytmx.util_pygame.load_pygame('Map/SalleInfo.tmx'),
    }

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
    clock = pygame.time.Clock()  # Créez une horloge pour contrôler la fréquence de rafraîchissement
    while en_jeu:
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                en_jeu = False
            elif evenement.type == pygame.KEYDOWN:
                if scene_actuelle == "titre" and evenement.key == pygame.K_SPACE:
                    scene_actuelle = "jeu"
                elif dialogue_actif and evenement.key == pygame.K_SPACE:
                    dialogue_index += 1
                    if dialogue_index >= len(dialogues):
                        dialogue_actif = False
                        dialogue_index = 0
                elif evenement.key == pygame.K_RETURN:
                    dialogue_actif = not dialogue_actif
                    dialogue_index = 0


        if scene_actuelle == "titre":
            # Afficher l'arrière-plan de l'écran de titre
            fenetre.blit(fond, (0, 0))
            fenetre.blit(titre_texte, titre_texte.get_rect(center=(largeur // 2, hauteur // 2 - 50)))
            fenetre.blit(jouer_texte, jouer_texte.get_rect(center=(largeur // 2, hauteur // 2 + 50)))

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

            pingouin = pygame.Rect(390, 365, 32, 32)
            if mon_sprite.rect.colliderect(pingouin):
                dialogue_actif = True

            if dialogue_actif:
                afficher_dialogue(fenetre, font, dialogues, dialogue_index, largeur, hauteur, blanc)

                # Détecter la collision avec les portes et changer de carte
                x_personnage, y_personnage = mon_sprite.rect.x // carte.tilewidth, mon_sprite.rect.y // carte.tileheight
                if (x_personnage, y_personnage) in portes_destinations:
                    nom_carte, position = portes_destinations[(x_personnage, y_personnage)]
                    # carte_actuelle = cartes[nom_carte]
                    mon_sprite.rect.x, mon_sprite.rect.y = position

            # Affichage du personnage
            sprites.draw(fenetre)
        clock.tick(60)

        pygame.display.flip()

    # Quitter Pygame
    pygame.quit()
    sys.exit()


main()