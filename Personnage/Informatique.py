import Personne


class Informatique(Personne):
    def __init__(self, genre):
        super().__init__(attaque=8, vie=100, competence="Programmation", image_path="sprite/perso-princ.png",
                         genre=genre)
