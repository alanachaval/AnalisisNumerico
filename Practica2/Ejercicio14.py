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
            operaciones.append(-(coeficientes[fila, columna] / pivote))
        return operaciones

    def restar_filas(self, coeficientes, pivote, fila, operacion):
        coeficientes[fila] = coeficientes[fila] + coeficientes[pivote] * operacion
        return coeficientes

    def descomponer_lower_upper(self, coeficientes):
        n = len(coeficientes)
        radios = self.calcular_radios(coeficientes)
        pivotes = []
        filas_restantes = np.arange(n).tolist()
        # lista con los "E" aplicados
        operaciones = []
        for columna in range(0, n - 1):
            pivote = self.obtener_pivote(coeficientes, columna, radios, filas_restantes)
            pivotes.append(pivote)
            operaciones.append(self.calcular_operaciones(coeficientes, pivote, filas_restantes, columna))
            print(operaciones)
            for i, fila in enumerate(filas_restantes):
                self.restar_filas(coeficientes, pivote, fila, operaciones[columna][i])
            print(coeficientes)
        return coeficientes

    def ejecucion(self, coeficientes, resultados):
        self.descomponer_lower_upper(coeficientes)
