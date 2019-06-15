import numpy as np


class C:

    def __init__(self, cero, uno, dos, tres):
        self.cero = cero
        self.uno = uno
        self.dos = dos
        self.tres = tres

    @staticmethod
    def evaluar(parametros):
        psi = parametros.psi
        eta = parametros.eta
        p = parametros.p

        coeficientes = np.array(
            [(1, 1, -1, -1),
             (psi.cero, psi.uno, -psi.dos, -psi.tres),
             (1.0 / (psi.cero * eta.n + 1), 1.0 / (psi.uno * eta.n + 1),
              -1.0 / (psi.dos * eta.n + 1), -1.0 / (psi.tres * eta.n + 1)),
             (1.0 / (psi.cero * eta.p - 1), 1.0 / (psi.uno * eta.p - 1),
              -1.0 / (psi.dos * eta.p - 1), -1.0 / (psi.tres * eta.p - 1))])
        resultados = np.array([0, 1.0 / p, 1.0 / (p * (eta.n + 1)) - 1.0 / p, 1.0 / (p * (eta.p - 1)) + 1.0 / p])
        variables = np.linalg.solve(coeficientes, resultados)

        return C(variables[0], variables[1], variables[2], variables[3])
