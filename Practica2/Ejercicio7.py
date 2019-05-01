import numpy as np


class Ejercicio7:

    def formula_cerrada(self, matriz):
        return max(sum(x) for x in matriz)

    def estimar_norma(self, matriz, intentos):
        m = np.matrix(matriz)
        n = len(m)
        return max(max(m * np.random.uniform(-1, 1, (n, 1)))[0, 0] for i in range(intentos))

    def ejecucion(self, matriz, intentos):
        print('cerrada: ', self.formula_cerrada(matriz))
        print('estimacion: ', self.estimar_norma(matriz, intentos))
