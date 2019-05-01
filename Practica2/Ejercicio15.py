import numpy as np


class Ejercicio15:

    # a: matriz de coeficientes
    # x: vector de variables
    # b: vector de resultados

    def optimizar(self, a, b):
        a = a.copy()
        b = b.copy()
        n = len(a)
        for i in range(n):
            a[i, i] = 0  # para permitir operar con multiplicaciones matriciales
        return a, b

    def richardson(self, a, b, terminos):
        n = len(a)
        x = np.random.uniform(-1, 1, (n, 1))
        for k in range(terminos):
            x = b - a * x
            print('Termino ', k + 1, '\n', x)
        return x

    def ejecucion(self, coeficientes, resultados, terminos):
        coeficientes = np.matrix(coeficientes)
        resultados = np.matrix(resultados)
        a, b = self.optimizar(coeficientes, resultados)
        variables = self.richardson(a, b, terminos)
        print('resultado esperado\n', resultados)
        print('resultado obtenido (coeficientes * variables)\n', coeficientes * variables)
