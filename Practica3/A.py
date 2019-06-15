import math


class A:

    def __init__(self, eta, b, psi, c):
        self.dos = (1 + psi.dos * eta.n) / (psi.tres - psi.dos) * (
                ((psi.cero - psi.tres) * c.cero * (math.e ** ((psi.cero - psi.dos) * b))) / (psi.cero * eta.n + 1) +
                ((psi.uno - psi.tres) * c.uno * (math.e ** ((psi.uno - psi.dos) * b))) / (psi.uno * eta.n + 1)
        )
        self.tres = -(1 + psi.tres * eta.n) / (psi.tres - psi.dos) * (
                ((psi.cero - psi.dos) * c.cero * (math.e ** ((psi.cero - psi.tres) * b))) / (psi.cero * eta.n + 1) +
                ((psi.uno - psi.dos) * c.uno * (math.e ** ((psi.uno - psi.tres) * b))) / (psi.uno * eta.n + 1)
        )
