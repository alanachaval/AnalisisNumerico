import math


class Tau:

    @staticmethod
    def evaluar(nu_cero, nu_inf, t_, t, kappa):
        return nu_inf * (t_ - t) - (nu_cero - nu_inf) * ((1 - math.e ** (-kappa * t_)) / kappa)
