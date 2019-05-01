import numpy as np
from numpy import matlib


class Ejercicio14:

    # a: matriz de coeficientes
    # x: vector de variables
    # b: vector de resultados
    # s: vector de radios
    # l: matriz triangular inferior
    # u: matriz triangular superior
    # y: vector de variables intermedio (l * y = b)

    # Dado que
    # a * x = b
    # a = p * l * u
    # p = inv(p)
    # Entonces
    # l * u * x = p * b

    def calcular_variables_upper(self, u, y):
        n = len(u)
        x = np.matlib.zeros((n, 1))
        for i in range(n - 1, -1, -1):
            x[i] = y[i]
            for j in range(n - 1, i, - 1):
                x[i] -= u[i, j] * x[j]
            x[i] /= u[i, i]
        return x

    def calcular_variables_lower(self, l, b):
        n = len(l)
        y = np.matlib.zeros((n, 1))
        for i in range(n):
            y[i] = b[i]
            for j in range(i):
                y[i] -= l[i, j] * y[j]
            y[i] /= l[i, i]
        return y

    def permutar_matriz(self, matriz, permutaciones):
        for i, permutacion in enumerate(permutaciones):
            if i < permutacion:
                matriz[i], matriz[permutacion] = matriz[permutacion], np.copy(matriz[i])
        return matriz

    def restar_filas(self, a, pivote, fila, operacion):
        a[fila] = a[fila] - a[pivote] * operacion
        return a

    def calcular_operaciones(self, a, pivote, filas_restantes, columna):
        pivote = a[pivote, columna]
        operaciones = []
        for fila in filas_restantes:
            operaciones.append(a[fila, columna] / pivote)
        return operaciones

    def obtener_pivote(self, a, columna, s, filas_restantes):
        mayor_radio = a[filas_restantes[0], columna] / s[filas_restantes[0]]
        index = 0
        for i, fila in enumerate(filas_restantes[1:]):
            radio = a[fila, columna] / s[fila]
            if radio > mayor_radio:
                mayor_radio = radio
                index = i + 1
        return filas_restantes.pop(index)

    def calcular_radios(self, a):
        return list(max(abs(y) for y in x) for x in a.tolist())

    def descomponer_lower_upper(self, a):
        n = len(a)
        s = self.calcular_radios(a)
        pivotes = []
        permutaciones = list(np.arange(n))
        filas_restantes = list(np.arange(n))
        u = a.copy()
        l = np.matlib.zeros((n, n))
        for i in range(n):
            l[i, i] = 1
        for columna in range(n - 1):
            pivote = self.obtener_pivote(u, columna, s, filas_restantes)
            permutaciones[columna], permutaciones[permutaciones[pivote]] = \
                permutaciones[permutaciones[pivote]], permutaciones[columna]
            pivotes.append(pivote)
            operaciones = self.calcular_operaciones(u, pivote, filas_restantes, columna)
            for i, fila in enumerate(filas_restantes):
                l[n - len(filas_restantes) + i, columna] = operaciones[i]
                self.restar_filas(u, pivote, fila, operaciones[i])

        return l, u, permutaciones

    def ejecucion(self, coeficientes, resultados):
        a = np.matrix(coeficientes)
        b = np.matrix(resultados)
        l, u, permutaciones = self.descomponer_lower_upper(a)
        u = self.permutar_matriz(u, permutaciones)
        b = self.permutar_matriz(b, permutaciones)
        print('lower\n', l)
        print('upper\n', u)
        print('matriz (l * u)\n', l * u)
        print('permutaciones\n', permutaciones)
        y = self.calcular_variables_lower(l, b)
        print('y (l * y = b)\n', y)
        print('resultado parcial esperado b\n', b)
        print('resultado parcial obtenido (l * y = b)\n', l * y)
        x = self.calcular_variables_upper(u, y)
        print('variables\n', x)
        print('resultado parcial esperado y\n', y)
        print('resultado obtenido (u * x = y)\n', u * x)
        print('matriz original\n', np.matrix(coeficientes))
        m = self.permutar_matriz(l * u, permutaciones)
        print('matriz recuperada (p * l * u)\n', m)
        print('resultado esperado b\n', np.matrix(resultados))
        print('resultado obtenido (a * x)\n', m * x)
        return


# y:
# [[ 1. ]
# [ 0.5]
# [-1. ]]

print()
print("Ejercicio 14:")
ejercicio14 = Ejercicio14()
# ejercicio14.ejecucion([[-1., 1., -4.],
#                      [2., 2., 0.],
#                      [3., 3., 2.]], [[0.], [1.], [0.5]])
# [[1.25]
#  [-0.75]
#  [-0.5]]

ejercicio14.ejecucion([[1., 6., 0.],
                       [2., 1., 0.],
                       [0., 2., 1.]], [[3.], [1.], [1.]])
# [[0.27272727]
#  [0.45454545]
#  [0.09090909]]
a = np.matrix([[1., 6., 0.],
               [2., 1., 0.],
               [0., 2., 1.]])
b = np.matrix([[3.], [1.], [1.]])

x = np.linalg.solve(a, b)

print('x\n', x)

print('a*x\n', a * x)

u = np.matrix([[2., 1., 0.], [0., 2., 1.], [0., 0., -2.75]])

y = u * x

print('y\n', y)

l = np.matrix([[1., 0., 0.], [0.5, 1., 0.], [0., 2.75, 1.]])

print('l*y\n', l * y)

# [-1, 1, 0.25]
