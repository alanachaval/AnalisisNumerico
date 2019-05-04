import numpy as np
from numpy import matlib


class Ejercicio14:

    # a: matriz de coeficientes
    # x: vector de variables
    # b: vector de resultados
    # s: vector de radios
    # p: vector de permutaciones

    def resolver_lower_upper(self, a, b, p):
        n = len(a)
        x = np.matlib.zeros((n, 1))
        for k in range(n - 1):
            for i in range(k + 1, n):
                b[p[i]] = b[p[i]] - a[p[i], k] * b[p[k]]
        for i in range(n - 1, -1, -1):
            x[i] = (b[p[i]] - sum(a[p[i], j] * x[j] for j in range(i + 1, n))) / a[p[i], i]
        return x

    def calcular_permutacion(self, a, k, p, s):
        pivote = max(range(k, len(a)), key=lambda i: abs(a[p[i], k]) / s[p[i]])
        p[pivote], p[k] = p[k], p[pivote]

    def calcular_radios(self, a):
        return list(max(abs(y) for y in x) for x in a.tolist())

    def descomponer_lower_upper(self, a):
        n = len(a)
        s = self.calcular_radios(a)
        p = list(range(n))
        for k in range(n):
            self.calcular_permutacion(a, k, p, s)
            for i in range(k + 1, n):
                z = a[p[i], k] / a[p[k], k]
                a[p[i], k] = z
                for j in range(k + 1, n):
                    a[p[i], j] -= a[p[k], j] * z
        return a, p

    def ejecucion(self, coeficientes, resultados):
        a = np.matrix(coeficientes)
        b = np.matrix(resultados)
        a, p = self.descomponer_lower_upper(a)
        x = self.resolver_lower_upper(a, b, p)
        print('Matriz de coeficientes\n', a)
        print('Vector de resultados\n', b)
        print('Vector de variables obtenido\n', x)
        variables = np.linalg.solve(coeficientes, resultados)
        print('Vector de variables esperado (numpy.linalg.solve)\n', variables)
