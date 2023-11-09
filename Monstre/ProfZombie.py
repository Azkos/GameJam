from Monstre.Ennemi import Ennemi


class ProfZombie(Ennemi):
    def __init__(self):
        super().__init__(difficulte=2, image_path="sprite/Prof-Zombie.png")
