import Ennemi


class EcranPasContent(Ennemi):
    def __init__(self):
        super().__init__(attaque=18, vie=42, difficulte=1, image_path="sprit/Mob.png")
