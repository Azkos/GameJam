import pygame
import sys
import pytmx
from Personnage.Sprite import Sprite
# ... (assurez-vous que tous les imports nécessaires sont présents)

def afficher_dialogue(fenetre, font, dialogues, dialogue_index, largeur, hauteur, blanc):
    # Affiche la boîte de dialogue avec le texte actuel
    pygame.draw.rect(fenetre, (0, 0, 0), (50, hauteur - 150, largeur - 100, 100))
    texte_dialogue = font.render(dialogues[dialogue_index], True, blanc)
    fenetre.blit(texte_dialogue, (60, hauteur - 140))

def main():
    pygame.init()

    largeur, hauteur = 800, 600
    fenetre = pygame.display.set_mode((largeur, hauteur))
    pygame.display.set_caption("Nom du jeu")

    blanc = (255, 255, 255)
    font = pygame.font.Font(None, 36)

    fond = pygame.image.load("image/v_iut2-rentree-2023_1696500078894-jpg (2)_120x80.png")
    fond = pygame.transform.scale(fond, (largeur, hauteur))

    titre_texte = font.render("Mon Jeu", True, blanc)
    jouer_texte = font.render("Appuyez sur une touche pour commencer le jeu", True, blanc)

    pygame.mixer.music.load('Musique/menu.mp3')
    pygame.mixer.music.play(-1)

    scene_actuelle = "titre"
    dialogue_actif = False
    dialogues = [
        "Bonjour, je suis un pingouin !",
        "C'est un beau jour pour une aventure !",
        "N'oubliez pas d'apporter votre équipement !"
    ]
    dialogue_index = 0

    mon_sprite = Sprite()
    sprites = pygame.sprite.Group(mon_sprite)

    en_jeu = True
    clock = pygame.time.Clock()

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

        touches = pygame.key.get_pressed()

        if scene_actuelle == "titre":
            fenetre.blit(fond, (0, 0))
            titre_rect = titre_texte.get_rect(center=(largeur // 2, hauteur // 2 - 50))
            jouer_rect = jouer_texte.get_rect(center=(largeur // 2, hauteur // 2 + 50))
            fenetre.blit(titre_texte, titre_rect)
            fenetre.blit(jouer_texte, jouer_rect)
        elif scene_actuelle == "jeu":
            pygame.mixer.music.stop()
            mon_sprite.deplacement(5)
            mon_sprite.update()
            fenetre.blit(mon_sprite.image, mon_sprite.rect)

            carte = pytmx.util_pygame.load_pygame('Map/SalleMain.tmx')
            for layer in carte.visible_layers:
                for x, y, gid, in layer:
                    tile = carte.get_tile_image_by_gid(gid)
                    if tile:
                        fenetre.blit(tile, (x * carte.tilewidth, y * carte.tileheight))

            pingouin = pygame.Rect(390, 365, 32, 32)
            if mon_sprite.rect.colliderect(pingouin):
                dialogue_actif = True

            if dialogue_actif:
                afficher_dialogue(fenetre, font, dialogues, dialogue_index, largeur, hauteur, blanc)

            sprites.draw(fenetre)

        clock.tick(60)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
