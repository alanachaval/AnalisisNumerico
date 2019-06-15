import math


class D:

    @staticmethod
    def evaluar(t, parametros):
        d_cero = parametros.d_cero
        t_ = parametros.t_
        r_ = parametros.r_
        div = parametros.div
        return d_cero * (math.e ** ((t_ - t) * (r_ - div)))
