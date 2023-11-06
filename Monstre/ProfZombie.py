import Ennemi


class ProfZombie(Ennemi):
    def __init__(self):
        super().__init__(attaque=22, vie=50, difficulte=3, image_path="sprit/Prof-Zombie.png")
