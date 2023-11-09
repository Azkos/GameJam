from Monstre import Ennemi


class LivreMutant(Ennemi):
    def __init__(self):
        super().__init__(difficulte=1, image_path="sprit/livre.png")
