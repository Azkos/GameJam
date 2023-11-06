import Personne


class CarriereSociale(Personne):
    def __init__(self):
        super().__init__(attaque=6, vie=100, competence="Compassion", sprite="sprite/perso-princ.png")