import pygame
import sys
# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Mon Jeu")

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)

# Police de caractères
font = pygame.font.Font(None, 36)

# Texte de l'écran de titre
titre_texte = font.render("Mon Jeu", True, blanc)
jouer_texte = font.render("Appuyez sur une touche pour jouer", True, blanc)

# Musique de l'écran de titre
pygame.mixer_music.load('Musique/menu.mp3')
pygame.mixer.music.play(-1)

# Boucle principale
en_jeu = False
while not en_jeu:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            pygame.quit()
            pygame.mixer.music.stop()
            sys.exit()
        if evenement.type == pygame.KEYDOWN:
            en_jeu = True

    # Effacer l'écran
    fenetre.fill(noir)

    # Afficher le texte de l'écran de titre
    titre_rect = titre_texte.get_rect(center=(largeur // 2, hauteur // 2 - 50))
    jouer_rect = jouer_texte.get_rect(center=(largeur // 2, hauteur // 2 + 50))

    fenetre.blit(titre_texte, titre_rect)
    fenetre.blit(jouer_texte, jouer_rect)

    pygame.display.flip()

# Votre code de jeu commencera ici une fois que l'utilisateur appuie sur une touche

# Boucle de jeu
en_jeu = True
while en_jeu:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            en_jeu = False

    # Logique de jeu et affichage ici

    fenetre.fill(noir)  # Effacer l'écran de jeu

    # Dessiner le contenu de votre jeu ici

    pygame.display.flip()

# Quitter Pygame
pygame.quit()
sys.exit()
