import math

from Practica3.D import D
from Practica3.Tau import Tau
from Practica3.V import V


class W:

    @staticmethod
    def evaluar(t, s, parametros):
        tau = Tau.evaluar(t, parametros)
        d_cero = parametros.d_cero
        r = parametros.r
        t_ = parametros.t_
        k = parametros.k
        d_t = D.evaluar(t, parametros)
        x = math.log((s + d_cero) / d_cero)
        a = math.log((k + d_t) / d_t)
        parametros.b = -a
        y = x - a
        return (d_t + k) * (math.e ** -(r * (t_ - t))) * V.evaluar(tau, y, parametros)

    @staticmethod
    def evaluar_default(t, s, parametros):
        tau = Tau.evaluar(t, parametros)
        d_cero = parametros.d_cero
        y = math.log((s + d_cero) / d_cero)
        return V.evaluar_default(tau, y, parametros)
