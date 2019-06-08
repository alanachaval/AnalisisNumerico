import math


class C:

    def __init__(self, b_cero, r, d):
        self.b_cero = b_cero
        self.r = r
        self.d = d

    def evaluar(self, t):
        return self.b_cero * (math.e ** (t * (self.r - self.d)))
