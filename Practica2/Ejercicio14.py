import numpy as np


class Ejercicio14:

    # A: Matriz de coeficientes
    # x: vector de variables
    # b: vector de resultados

    # def calcularRadios(X):
    #	return max(X) #maximo de cada fila

    def restar_columnas(self, coeficientes, pivot, fila, ratio):
        coeficientes[fila] = coeficientes[fila] + coeficientes[pivot] * ratio
        return coeficientes

    def calcular_ratios(self, coeficientes, pivot, Rr, columna):
        ratios = [0] * (len(coeficientes) - len(Rr))
        for i in range(len(Rr), len(coeficientes)):
            ratios[i - len(Rr)] = - (coeficientes[i, columna] / pivot)
        return ratios

    def obtener_pivote(self, coeficientes, Rr):
        return len(Rr)

    def diagonalizar_matriz(self, coeficientes):
        Rr = []
        for i in range(0, len(coeficientes) - 1):
            index_pivote = self.obtener_pivote(coeficientes, Rr)
            pivote = coeficientes[index_pivote, i]
            Rr.append(pivote)
            ratios = self.calcular_ratios(coeficientes, pivote, Rr, i)
            print(coeficientes)
            print(ratios)
            for j in range(0, len(coeficientes) - len(Rr)):
                self.restar_columnas(coeficientes, index_pivote, j + i + 1, ratios[j])
        return coeficientes

    def ejecucion(self, coeficientes, resultados):
        coeficientes = np.matrix(coeficientes)
        coeficientes = self.diagonalizar_matriz(coeficientes)
        print(coeficientes)
