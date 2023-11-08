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
