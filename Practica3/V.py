import math


class V:

    def __init__(self, u):
        self.lamda = [0.00277778, 6.40277778, 924.05000000, -34597.92777778, 540321.11111111, -4398346.36666666,
                      21087591.77777770, -63944913.04444440, 127597579.55000000, -170137188.08333300,
                      150327467.03333300, -84592161.50000000, 27478884.76666660, -3925554.96666666]
        self.u = u

    def evaluar(self, tau, y):
        ln_dos = math.log(2)
        p = ln_dos / tau
        return p * sum(self.lamda[j] * self.u.evaluar((j + 1) * p, y) for j in range(len(self.lamda)))
