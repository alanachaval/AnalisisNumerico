import math


class A:

    def __init__(self, dos, tres):
        self.dos = dos
        self.tres = tres

    @staticmethod
    def evaluar(parametros):
        psi = parametros.psi
        eta = parametros.eta
        b = parametros.b

        dos = (1 + psi.dos * eta.n) / (psi.tres - psi.dos) * (
                ((psi.cero - psi.tres) * c.cero * (math.e ** ((psi.cero - psi.dos) * b))) / (psi.cero * eta.n + 1) +
                ((psi.uno - psi.tres) * c.uno * (math.e ** ((psi.uno - psi.dos) * b))) / (psi.uno * eta.n + 1)
        )
        tres = -(1 + psi.tres * eta.n) / (psi.tres - psi.dos) * (
                ((psi.cero - psi.dos) * c.cero * (math.e ** ((psi.cero - psi.tres) * b))) / (psi.cero * eta.n + 1) +
                ((psi.uno - psi.dos) * c.uno * (math.e ** ((psi.uno - psi.tres) * b))) / (psi.uno * eta.n + 1)
        )

        return A(dos, tres)

    @staticmethod
    def evaluar_default(p, psi, parametros):
        eta = parametros.eta

        dos = - (1 / p) * psi.tres * (1 + eta.n * psi.dos) / (psi.tres - psi.dos)
        tres = (1 / p) * psi.dos * (1 + eta.n * psi.tres) / (psi.tres - psi.dos)

        return A(dos, tres)
