import math


class D:

    @staticmethod
    def evaluar(d_cero, r_, div, t_, t):
        return d_cero * (math.e ** ((t_ - t) * (r_ - div)))
