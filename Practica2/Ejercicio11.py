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
        variables = np.zeros(n)
        for i in range(n):
            variables[pivotes[i]] = b[pivotes[i]]
            for j in range(0, i):
                variables[pivotes[i]] -= a[pivotes[i], n - j - 1] * variables[pivotes[j]]
            variables[pivotes[i]] /= a[pivotes[i], n - i - 1]
        return variables

    def ejecucion(self, coeficientes, resultados):
        a = np.matrix(coeficientes)
        b = np.matrix(resultados)
        pivotes = self.obtener_indices_pivotes(a)
        x = self.calcular_variables(a, b, pivotes)
        print(x)
        return x
