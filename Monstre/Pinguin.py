import Ennemi


class Pinguin(Ennemi):
    def __init__(self):
        super().__init__(difficulte=3, image_path="sprit/pinguin.png")
