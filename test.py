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
fond = pygame.image.load("image/iut2.png")
fond = pygame.transform.scale(fond, (largeur, hauteur))

# Texte de l'écran de titre
titre_texte = font.render("Mon Jeu", True, blanc)
jouer_texte = font.render("Appuyez sur une touche pour jouer", True, blanc)

# Musique de l'écran de titre
pygame.mixer.music.load('Musique/menu.mp3')
pygame.mixer.music.play(-1)

# Chargez vos images de sprite pour les états "chara-walk1" et "chara-walk2"
sprite_walk1 = pygame.image.load("sprite/chara-walk1.png")
sprite_walk2 = pygame.image.load("sprite/chara-walk2.png")

# Redimensionnez le sprite à la moitié de sa taille d'origine
sprite_walk1 = pygame.transform.scale(sprite_walk1, (sprite_walk1.get_width() // 2, sprite_walk1.get_height() // 2))
sprite_walk2 = pygame.transform.scale(sprite_walk2, (sprite_walk2.get_width() // 2, sprite_walk2.get_height() // 2))

# Créez un objet sprite avec l'état "chara-walk1"
class MonSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = sprite_walk1
        self.rect = self.image.get_rect()
        self.rect.center = (largeur // 2, hauteur // 2)  # Position initiale du sprite

mon_sprite = MonSprite()
sprites = pygame.sprite.Group(mon_sprite)

# Vitesse de déplacement du sprite
vitesse = 1

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
direction = (0, 0)  # Direction de déplacement du sprite (horizontal, vertical)

while en_jeu:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            en_jeu = False

    # Logique de jeu et affichage ici

    # Mise à jour de la position du sprite en fonction des entrées de l'utilisateur
    touches = pygame.key.get_pressed()

    if touches[pygame.K_LEFT]:
        direction = (-vitesse, direction[1])  # Déplacer le sprite vers la gauche
    elif touches[pygame.K_RIGHT]:
        direction = (vitesse, direction[1])  # Déplacer le sprite vers la droite
    else:
        direction = (0, direction[1])

    if touches[pygame.K_UP]:
        direction = (direction[0], -vitesse)  # Déplacer le sprite vers le haut
    elif touches[pygame.K_DOWN]:
        direction = (direction[0], vitesse)  # Déplacer the sprite vers le bas
    else:
        direction = (direction[0], 0)

    # Changer l'image du sprite en alternant entre "chara-walk1" et "chara-walk2"
    if direction != (0, 0):
        if mon_sprite.image == sprite_walk1:
            mon_sprite.image = sprite_walk2
        else:
            mon_sprite.image = sprite_walk1

    # Limiter le déplacement du sprite aux bordures de l'écran
    mon_sprite.rect.x = max(0, min(mon_sprite.rect.x + direction[0], largeur - mon_sprite.rect.width))
    mon_sprite.rect.y = max(0, min(mon_sprite.rect.y + direction[1], hauteur - mon_sprite.rect.height))

    # Afficher l'arrière-plan du jeu
    fenetre.blit(fond, (0, 0))

    # Afficher le sprite
    sprites.draw(fenetre)

    pygame.display.flip()

# Quitter Pygame
pygame.quit()
sys.exit()
