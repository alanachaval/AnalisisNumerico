from Practica2.Ejercicio7 import Ejercicio7
import numpy as np
from numpy import matlib


class Ejercicio17:

    def jacobi(self, coeficientes):
        n = len(coeficientes)
        q_jacobi = np.matlib.zeros((n, n))
        for i in range(n):
            q_jacobi[i, i] = 1 / coeficientes[i, i]
        return q_jacobi

    def gauss_seidel(self, coeficientes):
        n = len(coeficientes)
        q_gauss_seidel = np.matlib.zeros((n, n))
        for i in range(n):
            for j in range(0, i + 1):
                q_gauss_seidel[i, j] = coeficientes[i, j]
        q_gauss_seidel = np.linalg.inv(q_gauss_seidel)
        return q_gauss_seidel

    def calcular_espectro(self, q, coeficientes):
        n = len(coeficientes)
        identidad = np.identity(n)
        espectro = identidad - q * coeficientes
        ejercicio7 = Ejercicio7()
        return ejercicio7.formula_cerrada(espectro.tolist())

    def ejecucion(self, coeficientes):
        coeficientes = np.matrix(coeficientes)
        q_jacobi = self.jacobi(coeficientes)
        espectro_jacobi = self.calcular_espectro(q_jacobi, coeficientes)
        print('Espectro Jacobi:', espectro_jacobi, end=' => ')
        if espectro_jacobi < 1:
            print('Converge para todo X inicial')
        else:
            print('No converge para todo X inicial')
        q_gauss_seidel = self.gauss_seidel(coeficientes)
        espectro_gauss_seidel = self.calcular_espectro(q_gauss_seidel, coeficientes)
        print('Espectro Gauss-Seidel:', espectro_gauss_seidel, end=' => ')
        if espectro_gauss_seidel < 1:
            print('Converge para todo X inicial')
        else:
            print('No converge para todo X inicial')
