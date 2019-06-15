import math

from Practica3.Tau import Tau
from Practica3.V import V


class W:

    def __init__(self, eta, mu, lamda, q, b, d_cero, d_t, kappa, r, nu_0, solver):
        self.d_cero = d_cero
        self.d_t = d_t
        self.kappa = kappa
        self.r = r
        self.nu_0 = nu_0
        self.v = V(eta, mu, lamda, q, b, solver)

    def evaluar(self, t, s):
        tau = Tau.evaluar(t, self.nu_0)
        x = math.log((s + self.d_cero) / self.d_cero)
        a = math.log((self.kappa + self.d_t) / self.d_t)
        y = x - a
        return (self.d_t + self.kappa) * (math.e ** -(self.r * t)) * self.v.evaluar(tau, y)
