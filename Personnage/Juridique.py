import Personne


class Juridique(Personne):
    def __init__(self, genre):
        super().__init__(attaque=6, vie=120, competence="Sommeil", sprite="sprite/perso-princ.png")