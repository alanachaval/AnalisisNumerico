import numpy as np


class Ejercicio11:

    # A: Matriz de coeficientes
    # x: vector de variables
    # b: vector de resultados

    def obtener_indices_pivotes(self, coeficientes):
        pivotes = [0] * len(coeficientes)
        for i in range(0, len(coeficientes)):
            columna = 0
            while coeficientes[i, columna] == 0:
                columna += 1
            pivotes[len(coeficientes) - columna - 1] = i
        return pivotes

    def calcular_variables(self, coeficientes, resultados, pivotes):
        variables = np.zeros(len(coeficientes))
        for i in range(0, len(coeficientes)):
            variables[pivotes[i]] = resultados[pivotes[i]]
            for j in range(0, i):
                variables[pivotes[i]] -= coeficientes[pivotes[i], len(coeficientes) - j - 1] * variables[pivotes[j]]
            variables[pivotes[i]] /= coeficientes[pivotes[i], len(coeficientes) - i - 1]
        return variables

    def ejecucion(self, coeficientes, resultados):
        coeficientes = np.matrix(coeficientes)
        pivotes = self.obtener_indices_pivotes(coeficientes)
        variables = self.calcular_variables(coeficientes, resultados, pivotes)
        print(variables)
        return variables
