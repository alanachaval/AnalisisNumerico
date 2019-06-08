import numpy as np


class C:

    def __init__(self, psi, eta, p, solver):
        coeficientes = np.array(
            [(1, 1, -1, -1),
             (psi.cero, psi.uno, -psi.dos, -psi.tres),
             (1.0 / (psi.cero * eta.n + 1), 1.0 / (psi.uno * eta.n + 1),
              -1.0 / (psi.dos * eta.n + 1), -1.0 / (psi.tres * eta.n + 1)),
             (1.0 / (psi.cero * eta.p - 1), 1.0 / (psi.uno * eta.p - 1),
              -1.0 / (psi.dos * eta.p - 1), -1.0 / (psi.tres * eta.p - 1))])
        resultados = np.array([0, 1.0 / p, 1.0 / (p * (eta.n + 1)) - 1.0 / p, 1.0 / (p * (eta.p - 1)) + 1.0 / p])
        variables = solver(coeficientes, resultados)
        self.cero = variables[0]
        self.uno = variables[1]
        self.dos = variables[2]
        self.tres = variables[3]
