import Personne


class Juridique(Personne):
    def __init__(self):
        super().__init__(attaque=6, vie=120, competence="Coupable", sprite="sprite/perso-princ.png")