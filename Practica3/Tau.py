import math


class Tau:

    @staticmethod
    def evaluar(t, parametros):
        nu = parametros.nu
        t_ = parametros.t_
        kappa = parametros.kappa
        return nu.inf * (t_ - t) + (nu.cero - nu.inf) * ((1 - math.e ** (-kappa * t_)) / kappa)
