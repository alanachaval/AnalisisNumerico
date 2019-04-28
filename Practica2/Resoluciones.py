from Practica2.Ejercicio11 import Ejercicio11
from Practica2.Ejercicio14 import Ejercicio14
import numpy as np

print()
print("Ejercicio 11:")
ejercicio14 = Ejercicio11()
ejercicio14.ejecucion(np.matrix([[1, 0, 0],
                                 [0, 1, 0],
                                 [0, 0, 1]]), [2, 3, 4])
# [2, 3, 4]
ejercicio14.ejecucion(np.matrix([[5, 7, 3],
                                 [0, 8, 9],
                                 [0, 0, -5]]), [7, 3, 1])
# [0.68, 0.6, -0.2]
ejercicio14.ejecucion(np.matrix([[0, 8, 9],
                                 [5, 7, 3],
                                 [0, 0, -5]]), [3, 7, 1])
# [0.6, 0.68, -0.2]

print()
print("Ejercicio 14:")
ejercicio14 = Ejercicio14()
ejercicio14.ejecucion(np.matrix([[-1, 1, -4],
                                 [2, 2, 0],
                                 [3, 3, 2]]), [])
