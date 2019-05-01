import numpy as np
from numpy import matlib


class Ejercicio16:

    # A: Matriz de coeficientes
    # x: vector de variables
    # b: vector de resultados

    def optimizar(self, coeficientes, resultados):
        a = coeficientes.copy()
        b = resultados.copy()
        n = len(a)
        for i in range(n):
            d = 1 / a[i, i]
            print(d)
            print(b)
            b[i] *= d
            print(b)
            print(a)
            a[i, :] = a[i, :] * d
            print(a)
        return a, b

    # def jacobi(self, matriz, resultados, terminos):
    #     n = len(matriz)
    #     variables = np.random.uniform(-1, 1, (n, 1))
    #     temporal = variables.copy()
    #     for k in range(terminos):
    #         for i in range(n):
    #             temporal[i] = resultados[i]
    #             t = 0
    #             for j in range(n):
    #                 if j != i:
    #                     t += matriz[i, j] * variables[j]
    #             temporal[i] -= t
    #             temporal[i] /= matriz[i, i]
    #         variables = temporal.copy()
    #         print('Termino ', k + 1, '\n', variables)
    #     return variables

    def jacobi(self, matriz, resultados, terminos):
        n = len(matriz)
        variables = np.random.uniform(-1, 1, (n, 1))
        temporal = variables.copy()
        for k in range(terminos):
            for i in range(n):
                temporal[i] = resultados[i]
                t = 0
                for j in range(n):
                    if j != i:
                        t += matriz[i, j] * variables[j]
                temporal[i] -= t
            variables = temporal.copy()
            print('Termino ', k + 1, '\n', variables)
        return variables

    def ejecucion(self, coeficientes, resultados, terminos):
        a, b = self.optimizar(coeficientes, resultados)
        variables = self.jacobi(a, b, terminos)
        print('coeficientes * variables\n', coeficientes * variables)


print()
print("Ejercicio 16:")
ejercicio16 = Ejercicio16()
ejercicio16.ejecucion(np.matrix([[2., -1., 0.],
                                 [1., 6., -2.],
                                 [4., -3., 8.]]), np.matrix([[2.], [-4.], [5.]]), 25)
