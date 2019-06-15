import math

from Practica3.Tau import Tau
from Practica3.V import V


class W:

    def __init__(self, eta, mu, lamda, q, b, d_cero, d_t, kappa, r, nu_cero, nu_inf, solver):
        self.d_cero = d_cero
        self.d_t = d_t
        self.kappa = kappa
        self.r = r
        self.nu_cero = nu_cero
        self.nu_inf = nu_inf
        self.v = V(eta, mu, lamda, q, b, solver)

    def evaluar(self, t, s):
        tau = Tau.evaluar(self.nu_cero, self.nu_inf, t, self.kappa)
        x = math.log((s + self.d_cero) / self.d_cero)
        a = math.log((self.kappa + self.d_t) / self.d_t)
        y = x - a
        return (self.d_t + self.kappa) * (math.e ** -(self.r * t)) * self.v.evaluar(tau, y)
