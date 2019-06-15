import math


class Tau:

    # @staticmethod
    # def evaluar(t, nu_0):
    #    return t * nu_0
    @staticmethod
    def evaluar(nu_cero, nu_inf, t, kappa):
        return nu_inf * t + (nu_cero - nu_inf) * ((1 - math.e ** (-kappa * t)) / kappa)
