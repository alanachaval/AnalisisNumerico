import numpy as np


class Ejercicio16:

    # a: Matriz de coeficientes
    # x: vector de variables
    # b: vector de resultados

    def optimizar(self, a, b):
        a = a.copy()
        b = b.copy()
        n = len(a)
        for i in range(n):
            d = 1 / a[i, i]
            b[i] *= d
            a[i, :] *= d
            a[i, i] = 0  # para permitir operar con multiplicaciones matriciales
        return a, b

    def jacobi(self, a, b, terminos):
        n = len(a)
        x = np.random.uniform(-1, 1, (n, 1))
        for k in range(terminos):
            x = b - a * x
            print('Termino ', k + 1, '\n', x)
        return x

    def gauss_seidel(self, a, b, terminos):
        n = len(a)
        x = np.random.uniform(-1, 1, (n, 1))
        for k in range(terminos):
            for i in range(n):
                x[i] = b[i] - a[i] * x
            print('Termino ', k + 1, '\n', x)
        return x

    def ejecucion(self, coeficientes, resultados, terminos):
        coeficientes = np.matrix(coeficientes)
        resultados = np.matrix(resultados)
        a, b = self.optimizar(coeficientes, resultados)
        print('Inicio Jacobi')
        variables = self.jacobi(a, b, terminos)
        print('coeficientes * variables\n', coeficientes * variables)
        print('Inicio Gauss-Seidel')
        variables = self.gauss_seidel(a, b, terminos)
        print('coeficientes * variables\n', coeficientes * variables)
