import numpy as np
from numpy import matlib


class Ejercicio11:

    # a: matriz de coeficientes
    # x: vector de variables
    # b: vector de resultados

    def obtener_indices_pivotes(self, a):
        n = len(a)
        pivotes = [0] * n
        for i in range(n):
            columna = 0
            while a[i, columna] == 0:
                columna += 1
            pivotes[n - columna - 1] = i
        return pivotes

    def calcular_variables(self, a, b, pivotes):
        n = len(a)
        x = np.matlib.zeros((n, 1))
        for i in range(n):
            x[i] = b[pivotes[i]]
            for j in range(0, i):
                x[i] -= a[pivotes[i], n - j - 1] * x[j]
            x[i] /= a[pivotes[i], n - i - 1]
        x = np.flip(x)
        return x

    def ejecucion(self, coeficientes, resultados):
        a = np.matrix(coeficientes)
        print('coeficientes\n', a)
        b = np.matrix(resultados)
        pivotes = self.obtener_indices_pivotes(a)
        x = self.calcular_variables(a, b, pivotes)
        print('variables\n', x)
        print('resultado esperado\n', b)
        print('resultado obtenido (coeficientes * variables)\n', a * x)
        return x
