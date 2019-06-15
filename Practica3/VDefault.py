import math

from Practica3.Tau import Tau
from Practica3.UDefault import UDefault


class VDefault:

    def __init__(self, eta, mu, lamda, q, nu_cero, nu_inf, t_, kappa, d_t, solver, rtol):
        self.nu_cero = nu_cero
        self.nu_inf = nu_inf
        self.t_ = t_
        self.kappa = kappa
        self.d_t = d_t
        self.lamda = [0.00277778, -6.40277778, 924.05000000, -34597.92777778, 540321.11111111, -4398346.36666666,
                      21087591.77777770, -63944913.04444440, 127597579.55000000, -170137188.08333300,
                      150327467.03333300, -84592161.50000000, 27478884.76666660, -3925554.96666666]
        self.u = UDefault(eta, mu, lamda, q, solver, rtol)

    def evaluar(self, t, s):
        tau = Tau.evaluar(self.nu_cero, self.nu_inf, self.t_, t, self.kappa)
        y = math.log((s + self.d_t) / self.d_t)
        return (
                math.log(2) / tau *
                sum(
                    self.lamda[j - 1] * self.u.evaluar(j * math.log(2) / tau, y)
                    for j in range(1, len(self.lamda) + 1)
                )
        )
