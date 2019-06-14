import math


class W:

    def __init__(self, d_cero, d_t, k, t, r, v):
        self.d_cero = d_cero
        self.d_t = d_t
        self.k = k
        self.t = t
        self.r = r
        self.v = v

    def evaluar(self, t, s):
        tau = 0  # PENDIENTE
        x = math.log((s + self.d_cero) / self.d_cero)
        a = math.log((self.k + self.d(t)) / self.d(t))
        return (self.d_t + self.k) * (math.e ** -self.r(t)) * self.v(tau, x - a)
