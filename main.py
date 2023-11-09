import pygame
import sys
import pytmx

from Personnage.Sprite import Sprite
from Map.GenererSalles import GenererSalles


def afficher_dialogue(fenetre, font, dialogues, dialogue_index, largeur, hauteur, couleur):
    # Affiche la boîte de dialogue avec le texte actuel
    pygame.draw.rect(fenetre, (0, 0, 0), (50, hauteur - 150, largeur - 100, 100))
    texte_dialogue = font.render(dialogues[dialogue_index], True, couleur)
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
    couleur_titre = (0, 0, 0)
    couleur_dialogue = (255, 255, 255)

    # Police de caractères
    font = pygame.font.Font(None, 36)

    # Chargez l'image d'arrière-plan pour le menu
    fond = pygame.image.load("image/iut2.png")
    fond = pygame.transform.scale(fond, (largeur, hauteur))

    # Texte de l'écran de titre
    titre_texte = font.render("Mon Jeu", True, couleur_titre)
    jouer_texte = font.render("Appuyez sur une touche pour commencer le jeu", True, couleur_titre)
    credit_texte = font.render("Appuez sur 'c' pour ouvrir les crédits", True, couleur_titre)

    # Musique de l'écran de titre
    pygame.mixer.music.load('Musique/menu.mp3')
    pygame.mixer.music.play(-1)

    # Variable d'état de la scène
    scene_actuelle = "titre"
    dialogue_actif = False
    dialogues = [
        "Bonjour, je suis ici pour vous préparer à vos épreuves",
        "Vous devez rester en forme pour être au maximum ",
        "Vous allez passer 3 épreuves de bases puis une final",
        "Ces épreuves constitueront de danser au bon rythme ",
        "Puis vous serez dans le rythme mieux ce sera",
        "Je vais vous téléporter dans une dimension rythmé",
        "Vous êtes prêt ? C'est parti !!!!!!"

    ]
    dialogue_index = 0

    # Création du personnage
    mon_sprite = Sprite()
    sprites = pygame.sprite.Group(mon_sprite)

    # Cartes préchargées
    spawn = {
        "Map/SalleMain.tmx": (570, 32),
        'Map/SalleMainParallele.tmx': (100, 100),
        'Map/SalleAmphiBoss.tmx': (570, 32),
        'Map/SalleFace.tmx': (330, 500),
        'Map/SalleCours.tmx': (640, 236),
        'Map/SalleInfo.tmx': (32, 224),
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
    carte_actuelle_nom = "Map/SalleMain.tmx"

    # Boucle principale
    en_jeu = True
    clock = pygame.time.Clock()
    while en_jeu:
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                en_jeu = False
            elif evenement.type == pygame.KEYDOWN:
                if scene_actuelle == "titre":
                    if evenement.key == pygame.K_c:
                        scene_actuelle = "credit"
                    else:
                        scene_actuelle = "jeu"
                        carte_actuelle_nom = "Map/SalleMain.tmx"
                elif scene_actuelle == "credit":
                    if evenement.key == pygame.K_ESCAPE:
                        scene_actuelle = "titre"
                elif dialogue_actif and evenement.key == pygame.K_SPACE:
                    dialogue_index += 1
                    if dialogue_index >= len(dialogues):
                        dialogue_actif = False
                        dialogue_index = 0
                        carte_actuelle_nom = "Map/SalleMainParallele.tmx"

        if scene_actuelle == "titre":
            # Afficher l'arrière-plan de l'écran de titre
            fenetre.blit(fond, (0, 0))
            fenetre.blit(titre_texte, titre_texte.get_rect(center=(largeur // 2, hauteur // 2 - 50)))
            fenetre.blit(jouer_texte, jouer_texte.get_rect(center=(largeur // 2, hauteur // 2 + 50)))
            fenetre.blit(credit_texte, credit_texte.get_rect(center=(largeur // 2, hauteur // 2 + 100)))

        elif scene_actuelle == "credit":
            fenetre.fill("black")
            cred_textes = ["Alexis Rebelo : Leader",
                           "Yvain Dalban : Chargé du core-game",
                           "Kevin Zheng : Level Designer",
                           "Théo Besset : Scénariste",
                           "Musiques et Bruitages : https://lasonotheque.org",
                           "https://iut2.univ-grenoble-alpes.fr",
                           "Images et Sprites : "]
            pos_x = 50
            pos_y = 50
            for texte in cred_textes:
                fenetre.blit(font.render(texte, True, "white"), (pos_x, pos_y))
                pos_y += 50
            fenetre.blit(font.render("Echap pour sortir", True, "white"), (20, hauteur - 50))

        elif scene_actuelle == "jeu":

            pygame.mixer.music.stop()

            genererSalle = GenererSalles(carte_actuelle_nom, fenetre, largeur, hauteur)
            carte = genererSalle.genererSalle()

            mon_sprite.update()

            mon_sprite.deplacement(8)
            if mon_sprite.checkCollision(carte, "collision"):
                mon_sprite.rect.x = mon_sprite.last_pos[0]
                mon_sprite.rect.y = mon_sprite.last_pos[1]

            fenetre.blit(mon_sprite.image, mon_sprite.rect)

            # Afficher le nom du personnage en haut à gauche
            nom_personnage_texte = font.render(nom_personnage, True, couleur_titre)
            fenetre.blit(nom_personnage_texte, (10, 10))  # Position du texte

            # Interaction avec le pingouin sur la carte "SalleMain"
            if carte_actuelle_nom == "Map/SalleMain.tmx":
                if mon_sprite.checkCollision(carte, "dialogue"):
                    dialogue_actif = True

            # Affichage du dialogue si actif
            if dialogue_actif:
                afficher_dialogue(fenetre, font, dialogues, dialogue_index, largeur, hauteur, couleur_dialogue)


            teleport = mon_sprite.checkTeleporte(carte, "Teleporte")
            if teleport:
                carte_actuelle_nom = teleport
                mon_sprite.rect.x = spawn[carte_actuelle_nom][0]
                mon_sprite.rect.y = spawn[carte_actuelle_nom][1]

            # Affichage du personnage
            sprites.draw(fenetre)
        print(clock)
        clock.tick(60)

        pygame.display.flip()

    # Quitter Pygame
    pygame.quit()
    sys.exit()


main()
