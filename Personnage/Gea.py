import Personne


class Gea(Personne):
    def __init__(self):
        super().__init__(attaque=6, vie=80, competence="Réduction", image_path="sprite/perso-princ.png")
