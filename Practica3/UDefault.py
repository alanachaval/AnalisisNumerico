import math

from Practica3.ADefault import ADefault
from Practica3.Psi import Psi


class UDefault:

    def __init__(self, eta, mu, lamda, q, solver, rtol):
        self.eta = eta
        self.mu = mu
        self.lamda = lamda
        self.q = q
        self.solver = solver
        self.rtol = rtol

    def evaluar(self, p, y):
        psi = Psi(self.eta, self.mu, self.lamda, self.q, p, self.solver, self.rtol)
        a = ADefault(self.eta, p, psi)
        return a.dos * (math.e ** (psi.dos * y)) + a.tres * (math.e ** (psi.tres * y)) + 1 / p
