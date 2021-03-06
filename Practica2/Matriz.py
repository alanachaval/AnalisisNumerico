import numpy as np
from numpy import matlib


class Matriz:

    @staticmethod
    def descomponer_lower_upper(matriz):
        n = len(matriz)
        lower = np.matlib.zeros((n, n))
        upper = np.matlib.zeros((n, n))
        for i in range(n):
            lower[i, i] = 1
        for i in range(0, n):
            for j in range(0, i):
                lower[i, j] = matriz[i, j]
                for k in range(0, j):
                    lower[i, j] -= lower[i, k] * upper[k, j]
                lower[i, j] /= upper[j, j]
            for j in range(i, n):
                upper[i, j] = matriz[i, j]
                for k in range(0, i):
                    upper[i, j] -= lower[i, k] * upper[k, j]
        return lower, upper


_matriz = np.matrix([[-1, 1, -4],
                     [2, 2, 0],
                     [3, 3, 2]])
_lower, _upper = Matriz.descomponer_lower_upper(_matriz)
print('lower:\n', _lower)
print('upper:\n', _upper)
print('matriz original\n', _matriz)
print('matriz lower * upper\n', _lower * _upper)
