import numpy as np


class Ejercicio11:

    # a: Matriz de coeficientes
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
        x = np.zeros(n)
        for i in range(n):
            x[pivotes[i]] = b[pivotes[i]]
            for j in range(0, i):
                x[pivotes[i]] -= a[pivotes[i], n - j - 1] * x[pivotes[j]]
            x[pivotes[i]] /= a[pivotes[i], n - i - 1]
        return x

    def ejecucion(self, coeficientes, resultados):
        a = np.matrix(coeficientes)
        b = np.matrix(resultados)
        pivotes = self.obtener_indices_pivotes(a)
        variables = self.calcular_variables(a, b, pivotes)
        print(variables)
        return variables
