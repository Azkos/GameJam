import Ennemi


class LivreMutant(Ennemi):
    def __init__(self):
        super().__init__(attaque=15, vie=35, difficulte=1, image_path="sprit/livre.png")
