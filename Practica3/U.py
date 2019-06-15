import math

from Practica3.A import A
from Practica3.C import C
from Practica3.Psi import Psi


class U:

    @staticmethod
    def evaluar(p, y, parametros):
        psi = Psi.evaluar(p, parametros)
        c = C.evaluar(p, psi, parametros)
        a = A.evaluar(psi, c, parametros)
        if y <= 0:
            return (
                    c.cero * (math.e ** (psi.cero * y)) +
                    c.uno * (math.e ** (psi.uno * y)) +
                    a.dos * (math.e ** (psi.dos * y)) +
                    a.tres * (math.e ** (psi.tres * y))
            )
        else:
            return (
                    c.dos * (math.e ** (psi.dos * y)) +
                    c.tres * (math.e ** (psi.tres * y)) +
                    a.dos * (math.e ** (psi.dos * y)) +
                    a.tres * (math.e ** (psi.tres * y)) +
                    (math.e ** y - 1.0) / p
            )

    @staticmethod
    def evaluar_default(p, y, parametros):
        psi = Psi.evaluar(p, parametros)
        a = A.evaluar_default(p, psi, parametros)
        return a.dos * (math.e ** (psi.dos * y)) + a.tres * (math.e ** (psi.tres * y)) + 1 / p
