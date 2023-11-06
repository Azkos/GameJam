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

# Chargez l'image d'arrière-plan
fond = pygame.image.load("image/v_iut2-rentree-2023_1696500078894-jpg (2)_120x80.png")  # Remplacez par le chemin de votre image d'arrière-plan
fond = pygame.transform.scale(fond, (largeur, hauteur))

# Texte de l'écran de titre
titre_texte = font.render("Mon Jeu", True, blanc)
jouer_texte = font.render("Appuyez sur une touche pour jouer", True, blanc)

# Musique de l'écran de titre
pygame.mixer.music.load('Musique/menu.mp3')
pygame.mixer.music.play(-1)

# Chargez votre propre image de sprite
votre_sprite = pygame.image.load("sprite/perso-princ.png")  # Remplacez par le chemin de votre image de sprite
votre_sprite = pygame.transform.scale(votre_sprite, (50, 50))  # Redimensionnez le sprite si nécessaire

# Créez un objet sprite pour votre sprite personnalisé
class MonSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = votre_sprite
        self.rect = self.image.get_rect()
        self.rect.center = (largeur // 2, hauteur // 2)  # Position initiale de votre sprite

# Créez un groupe de sprites
sprites = pygame.sprite.Group()
mon_sprite = MonSprite()
sprites.add(mon_sprite)

# Boucle principale pour l'écran de titre
en_jeu = False
while not en_jeu:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            pygame.quit()
            pygame.mixer.music.stop()
            sys.exit()
        if evenement.type == pygame.KEYDOWN:
            en_jeu = True

    # Afficher l'arrière-plan de l'écran de titre
    fenetre.blit(fond, (0, 0))

    # Afficher le texte de l'écran de titre
    titre_rect = titre_texte.get_rect(center=(largeur // 2, hauteur // 2 - 50))
    jouer_rect = jouer_texte.get_rect(center=(largeur // 2, hauteur // 2 + 50))

    fenetre.blit(titre_texte, titre_rect)
    fenetre.blit(jouer_texte, jouer_rect)

    pygame.display.flip()

# Boucle de jeu
en_jeu = True
while en_jeu:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            en_jeu = False

    # Logique de jeu et affichage ici

    # Mise à jour de la position de votre sprite en fonction des entrées de l'utilisateur
    touches = pygame.key.get_pressed()
    vitesse = 1
    if touches[pygame.K_LEFT]:
        mon_sprite.rect.x -= vitesse
    if touches[pygame.K_RIGHT]:
        mon_sprite.rect.x += vitesse
    if touches[pygame.K_UP]:
        mon_sprite.rect.y -= vitesse
    if touches[pygame.K_DOWN]:
        mon_sprite.rect.y += vitesse

    # Afficher l'arrière-plan du jeu
    fenetre.blit(fond, (0, 0))

    # Afficher votre sprite
    sprites.draw(fenetre)

    pygame.display.flip()

# Quitter Pygame
pygame.quit()
sys.exit()
