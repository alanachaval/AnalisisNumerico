import math


class U:

    def __init__(self, c, a, psi):
        self.c = c
        self.a = a
        self.psi = psi

    def evaluar(self, p, y):
        if y <= 0:
            return self.c.cero * (math.e ** (self.psi.cero * y)) + \
                   self.c.uno * (math.e ** (self.psi.uno * y)) + \
                   self.a.dos * (math.e ** (self.psi.dos * y)) + \
                   self.a.tres * (math.e ** (self.psi.tres * y))
        else:
            return self.c.dos * (math.e ** (self.psi.dos * y)) + \
                   self.c.tres * (math.e ** (self.psi.tres * y)) + \
                   self.a.dos * (math.e ** (self.psi.dos * y)) + \
                   self.a.tres * (math.e ** (self.psi.tres * y)) + \
                   (math.e ** y - 1.0) / p
