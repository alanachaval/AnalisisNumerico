import math


class W:

    def __init__(self, d, k, t, r, v):
        self.d = d
        self.k = k
        self.t = t
        self.r = r
        self.v = v

    def evaluar(self, t, s):
        tau = 0  # PENDIENTE
        x = math.log((s + self.d(0)) / self.d(0))
        a = math.log((self.k + self.d(t)) / self.d(t))
        return (self.d(self.t) + self.k) * (math.e ** -self.r(t)) * self.v(tau, x - a)
