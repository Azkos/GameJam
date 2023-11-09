import pygame
import sys
import Action.Dancing as Dan
import Monstre.Ennemi as En
from Personnage.Sprite import Sprite
from Map.GenererSalles import GenererSalles


# Fonction pour afficher la boîte de dialogue
def afficher_dialogue(fenetre, font, dialogues, dialogue_index, largeur, hauteur, couleur):
    pygame.draw.rect(fenetre, (0, 0, 0), (50, hauteur - 150, largeur - 100, 100))
    texte_dialogue = font.render(dialogues[dialogue_index], True, couleur)
    fenetre.blit(texte_dialogue, (60, hauteur - 140))


# Fonction pour lancer la danse
def lancer_dance(fenetre, carte_nom, sprite, dance):
    res = True
    if not dance[carte_nom]:
        # Créer un ennemi en fonction de la carte
        if carte_nom == "Map/SalleAmphiBoss.tmx":
            ennemi = En.Ennemi(3, "sprite/pinguin2.png")
        elif carte_nom == "Map/SalleFace.tmx":
            ennemi = En.Ennemi(2, "sprite/perso4.png")
        elif carte_nom == "Map/SalleCours.tmx":
            ennemi = En.Ennemi(1, "sprite/perso3.png")
        elif carte_nom == "Map/SalleInfo.tmx":
            ennemi = En.Ennemi(1, "sprite/perso2.png")

        # Lancer la danse
        dance = Dan.Dancing(sprite, ennemi, fenetre)
        res = dance.dance()

    return res


# Fonction principale du jeu
def main():
    # Initialisation de Pygame
    pygame.init()

    # Récupére l'argument correspondant au nom du joueur
    if len(sys.argv) > 1:
        nom_personnage = "Nom : " + sys.argv[1]
    else:
        nom_personnage = "Nom : no idea"

    # Dimensions de la fenêtre
    largeur, hauteur = 800, 600
    fenetre = pygame.display.set_mode((largeur, hauteur))
    pygame.display.set_caption("IUT Rythm Quest")

    # progression dans le jeu
    dance_reussi = 0
    dance = {
        'Map/SalleAmphiBoss.tmx': False,
        'Map/SalleFace.tmx': False,
        'Map/SalleCours.tmx': False,
        'Map/SalleInfo.tmx': False,
    }

    # Couleurs
    couleur_titre = (0, 0, 0)
    couleur_dialogue = (255, 255, 255)

    # Police de caractères
    font = pygame.font.Font(None, 36)

    # Chargez l'image d'arrière-plan pour le menu
    fond = pygame.image.load("image/iut2.png")
    fond = pygame.transform.scale(fond, (largeur, hauteur))

    # Texte de l'écran de titre
    titre_texte = font.render("IUT Rythm Quest", True, couleur_titre)
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
        "Ces épreuves consisteront en danser sans se tromper",
        "Appuyez sur les touches demandées",
        "Le plus rapidement pour réussir",
        "Je vais vous téléporter dans une dimension rythmé",
        "Vous êtes prêt ? C'est parti !!!!!!"

    ]
    dialogue_index = 0

    # Création du personnage
    mon_sprite = Sprite()
    sprites = pygame.sprite.Group()
    mon_sprite.add(sprites)

    # Cartes préchargées
    spawn = {
        "Map/SalleMain.tmx": (300, 300),
        'Map/SalleMainParallele.tmx': (300, 300),
        'Map/SalleAmphiBoss.tmx': (550, 32),
        'Map/SalleFace.tmx': (330, 500),
        'Map/SalleCours.tmx': (670, 300),
        'Map/SalleInfo.tmx': (90, 224),
    }

    # Carte actuelle
    carte_actuelle_nom = "Map/SalleMain.tmx"

    # Boucle principale
    en_jeu = True
    clock = pygame.time.Clock()
    while en_jeu:
        for evenement in pygame.event.get():
            # Gestion des événements
            if evenement.type == pygame.QUIT:
                en_jeu = False
            elif evenement.type == pygame.KEYDOWN:
                if scene_actuelle == "titre":
                    if evenement.key == pygame.K_c:
                        scene_actuelle = "credit"
                    else:
                        scene_actuelle = "jeu"
                        carte_actuelle_nom = "Map/SalleMain.tmx"
                        pygame.mixer_music.load("Musique/musique.mp3")
                        pygame.mixer_music.play(-1)

                elif scene_actuelle == "credit":
                    if evenement.key == pygame.K_ESCAPE:
                        scene_actuelle = "titre"
                elif scene_actuelle == "fin" or scene_actuelle == "victoire":
                    if evenement.key == pygame.K_SPACE:
                        scene_actuelle = "titre"
                elif dialogue_actif and evenement.key == pygame.K_SPACE:
                    pygame.mixer_music.load("Musique/bruit_parler.mp3")
                    pygame.mixer_music.play()
                    dialogue_index += 1
                    if dialogue_index >= len(dialogues):
                        dialogue_actif = False
                        pygame.mixer_music.stop()
                        dialogue_index = 0
                        carte_actuelle_nom = "Map/SalleMainParallele.tmx"
                        pygame.mixer_music.load("Musique/musique.mp3")
                        pygame.mixer_music.play(-1)

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
                           "My Life for Witherlimb de Will Savino",
                           "Voix : Sans de Undertale",
                           "Images et Sprites : https://iut2.univ-grenoble-alpes.fr",
                           "https://ccrgeek.wordpress.com/2016/01/01/mv-school-tile-set/",
                           "https://fallinlovewithyou-raura.blogspot.com/2021/01/pixel-art-character-generator-please.html"]
            pos_x = 50
            pos_y = 50
            for texte in cred_textes:
                fenetre.blit(font.render(texte, True, "white"), (pos_x, pos_y))
                pos_y += 50
            fenetre.blit(font.render("Echap pour sortir", True, "white"), (20, hauteur - 50))

        elif scene_actuelle == "jeu":

            genererSalle = GenererSalles(carte_actuelle_nom, fenetre, largeur, hauteur)
            carte = genererSalle.genererSalle()

            mon_sprite.update()

            mon_sprite.deplacement(10)
            if mon_sprite.checkCollision(carte, "collision"):
                mon_sprite.rect.x = mon_sprite.last_pos[0]
                mon_sprite.rect.y = mon_sprite.last_pos[1]

            fenetre.blit(mon_sprite.image, mon_sprite.rect)

            if carte_actuelle_nom != "Map/SalleMain.tmx":
                del genererSalle

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
                pygame.mixer_music.load("Musique/musique.mp3")
                pygame.mixer_music.play(-1)

            if mon_sprite.checkCollision(carte, "dance"):
                if lancer_dance(fenetre, carte_actuelle_nom, mon_sprite, dance):
                    dance[carte_actuelle_nom] = True
                    fini = True
                    for e in dance:
                        if not dance[e]:
                            fini = False
                    if fini:
                        # affichage victoire
                        scene_actuelle = "victoire"
                        pygame.mixer_music.load("Musique/win.mp3")
                        pygame.mixer_music.play()
                        dance_reussi = 0
                    else:
                        # dialogue félicitation et continuer
                        felicitation = ["Explore les autres salles pour finir ton entrainement"]
                        for i in range(len(felicitation)):
                            afficher_dialogue(fenetre, font, felicitation, i, largeur, hauteur, couleur_dialogue)


                else:
                    # affichage écran de défaite
                    scene_actuelle = "fin"
                    pygame.mixer_music.load("Musique/loose.mp3")
                    pygame.mixer_music.play()
                    dance_reussi = 0

            # Affichage du personnage
            sprites.draw(fenetre)

        elif scene_actuelle == "fin":
            fenetre.fill("black")
            fin_textes = ["Vous avez perdu !", "Vous aurez plus de chance la prochaine fois",
                          "Appuyez sur espace pour revenir au menu pricipal"]
            fin_font = []
            for texte in fin_textes:
                fin_font.append(font.render(texte, True, "red"))
            pos_y = 50
            for elem in fin_font:
                fenetre.blit(elem, (largeur // 2 - elem.get_rect().center[0], pos_y))
                pos_y += 50


        elif scene_actuelle == "victoire":
            fenetre.fill("white")
            victoire_textes = ["Bien joué !",
                               "Vous êtes parvenu au bout de toutes les dances",
                               "et êtes maintenant prêt pour passer vos examens",
                               "Appuyez sur espace pour revenir au menu principal",
                               "ou sur la croix en haut à droite pour quitter le jeu"]
            vict_font = []
            for texte in victoire_textes:
                vict_font.append(font.render(texte, True, "black"))
            pos_y = 50
            for elem in vict_font:
                fenetre.blit(elem, (largeur // 2 - elem.get_rect().center[0], pos_y))
                pos_y += 50

        clock.tick(60)

        pygame.display.flip()

    # Quitter Pygame
    pygame.quit()
    sys.exit()


main()
