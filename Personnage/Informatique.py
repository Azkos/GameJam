from Personnage.Personne import Personne


class Informatique(Personne):
    def __init__(self):
        super().__init__(attaque=8, vie=100, competence="Hacking", image_path="sprite/perso-princ.png")
