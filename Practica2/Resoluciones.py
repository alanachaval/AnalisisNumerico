from Practica2.Ejercicio7 import Ejercicio7
from Practica2.Ejercicio11 import Ejercicio11
from Practica2.Ejercicio14 import Ejercicio14
from Practica2.Ejercicio16 import Ejercicio16
from Practica2.Ejercicio17 import Ejercicio17
import numpy as np

print()
print("Ejercicio 7:")
ejercicio7 = Ejercicio7()
ejercicio7.ejecucion([[1., 2., 3.],
                      [4., 5., 9.],
                      [7., 8., 6.]], 10000)

print()
print("Ejercicio 11:")
ejercicio11 = Ejercicio11()
ejercicio11.ejecucion(np.matrix([[1., 0., 0.],
                                 [0., 1., 0.],
                                 [0., 0., 1.]]), [2., 3., 4.])
# [2, 3, 4]
ejercicio11.ejecucion(np.matrix([[5., 7., 3.],
                                 [0., 8., 9.],
                                 [0., 0., -5.]]), [7., 3., 1.])
# [0.68, 0.6, -0.2]
ejercicio11.ejecucion(np.matrix([[0., 8., 9.],
                                 [5., 7., 3.],
                                 [0., 0., -5.]]), [3., 7., 1.])
# [0.6, 0.68, -0.2]

print()
print("Ejercicio 14:")
ejercicio14 = Ejercicio14()
ejercicio14.ejecucion(np.matrix([[-1., 1., -4.],
                                 [2., 2., 0.],
                                 [3., 3., 2.]]), [0., 1., 0.5])
# [1.25, 0.5, -1]

ejercicio14.ejecucion(np.matrix([[1., 6., 0.],
                                 [2., 1., 0.],
                                 [0., 2., 1.]]), [3., 1., 1.])
# [-1, 1, 0.25]

print()
print("Ejercicio 16:")
ejercicio16 = Ejercicio16()
ejercicio16.ejecucion(np.matrix([[2., -1., 0.],
                                 [1., 6., -2.],
                                 [4., -3., 8.]]), np.matrix([[2.], [-4.], [5.]]), 25)

print()
print("Ejercicio 17:")
ejercicio17 = Ejercicio17()
ejercicio17.ejecucion(np.matrix([[2., -1., 0.],
                                 [1., 6., -2.],
                                 [4., -3., 8.]]))
