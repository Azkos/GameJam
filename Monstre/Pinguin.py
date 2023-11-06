import Ennemi


class Pinguin(Ennemi):
    def __init__(self):
        super().__init__(attaque=30, vie=70, difficulte=4, image_path="sprit/pinguin.png")
