import numpy as np
from numpy import matlib


class Ejercicio14:

    # A: Matriz de coeficientes
    # x: vector de variables
    # b: vector de resultados

    def calcular_radios(self, matriz):
        radios = []
        for i in range(0, len(matriz)):
            maximo = abs(matriz[i, 0])
            for j in range(1, len(matriz)):
                if abs(matriz[i, j]) > maximo:
                    maximo = abs(matriz[i, j])
            radios.append(maximo)
        return radios

    def obtener_pivote(self, coeficientes, columna, radios, filas_restantes):
        mayor_radio = coeficientes[filas_restantes[0], columna] / radios[filas_restantes[0]]
        index = 0
        for i, fila in enumerate(filas_restantes[1:]):
            radio = coeficientes[fila, columna] / radios[fila]
            if radio > mayor_radio:
                mayor_radio = radio
                index = i + 1
        return filas_restantes.pop(index)

    def calcular_operaciones(self, coeficientes, pivote, filas_restantes, columna):
        pivote = coeficientes[pivote, columna]
        operaciones = []
        for fila in filas_restantes:
            operaciones.append(coeficientes[fila, columna] / pivote)
        return operaciones

    def restar_filas(self, coeficientes, pivote, fila, operacion):
        coeficientes[fila] = coeficientes[fila] - coeficientes[pivote] * operacion
        return coeficientes

    def descomponer_lower_upper(self, coeficientes):
        n = len(coeficientes)
        radios = self.calcular_radios(coeficientes)
        pivotes = []
        permutaciones = list(np.arange(n))
        filas_restantes = list(np.arange(n))
        upper = coeficientes.copy()
        lower = np.matlib.zeros((n, n))
        for i in range(0, n):
            lower[i, i] = 1
        for columna in range(0, n - 1):
            pivote = self.obtener_pivote(upper, columna, radios, filas_restantes)
            permutaciones[columna], permutaciones[permutaciones[pivote]] = \
                permutaciones[permutaciones[pivote]], permutaciones[columna]
            pivotes.append(pivote)
            operaciones = self.calcular_operaciones(upper, pivote, filas_restantes, columna)
            for i, fila in enumerate(filas_restantes):
                lower[n - i - 1, columna] = operaciones[i]
                self.restar_filas(upper, pivote, fila, operaciones[i])

        # Permutar upper
        for i, permutacion in enumerate(permutaciones):
            if i < permutacion:
                upper[i], upper[permutacion] = upper[permutacion], np.copy(upper[i])

        return lower, upper, permutaciones

    def calcular_variables_lower(self, coeficientes, resultados):
        n = len(coeficientes)
        variables = np.zeros(n)
        for i in range(0, n):
            variables[i] = resultados[i]
            for j in range(0, i):
                variables[i] -= coeficientes[i, n - j - 1] * variables[j]
            variables[i] /= coeficientes[i, i]
        return variables

    def calcular_variables_upper(self, coeficientes, resultados):
        n = len(coeficientes)
        variables = np.zeros(n)
        for i in range(n - 1, -1, -1):
            variables[i] = resultados[i]
            for j in range(n - 1, i, - 1):
                variables[i] -= coeficientes[i, j] * variables[j]
            variables[i] /= coeficientes[i, i]
        return variables

    def ejecucion(self, coeficientes, resultados):
        lower, upper, permutaciones = self.descomponer_lower_upper(coeficientes)
        print('lower\n', lower)
        print('upper\n', upper)
        print('permutaciones\n', permutaciones)
        y = self.calcular_variables_lower(lower, resultados)
        print('y (Ly=b)\n', y)
        variables = self.calcular_variables_upper(upper, y)
        print('variables\n', variables)
