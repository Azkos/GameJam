import Personne


class InfoCom(Personne):
    def __init__(self):
        super().__init__(attaque=10, vie=80, competence="", image_path="sprite/perso-princ.png")