import math

from Practica3.A import A
from Practica3.C import C
from Practica3.Psi import Psi


class U:

    #    def __init__(self, eta, mu, lamda, q, b, solver, rtol):
    #        self.eta = eta
    #        self.mu = mu
    #        self.lamda = lamda
    #        self.q = q
    #        self.b = b
    #        self.solver = solver
    #        self.rtol = rtol

    def evaluar(self, p, y):
        psi = Psi(self.eta, self.mu, self.lamda, self.q, p, self.solver, self.rtol)
        c = C(self.eta, p, psi)
        a = A(self.eta, self.b, psi, c)
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
