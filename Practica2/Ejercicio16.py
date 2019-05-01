import numpy as np
from numpy import matlib


class Ejercicio16:

    # a: Matriz de coeficientes
    # x: vector de variables
    # b: vector de resultados

    def optimizar(self, coeficientes, resultados):
        a = coeficientes.copy()
        b = resultados.copy()
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

    def ejecucion(self, coeficientes, resultados, terminos):
        a, b = self.optimizar(coeficientes, resultados)
        print('Inicio Jacobi')
        variables = self.jacobi(a, b, terminos)
        print('coeficientes * variables\n', coeficientes * variables)


print()
print("Ejercicio 16:")
ejercicio16 = Ejercicio16()
ejercicio16.ejecucion(np.matrix([[2., -1., 0.],
                                 [1., 6., -2.],
                                 [4., -3., 8.]]), np.matrix([[2.], [-4.], [5.]]), 25)
