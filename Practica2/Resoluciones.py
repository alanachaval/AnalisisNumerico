from Ejercicio7 import Ejercicio7
from Ejercicio11 import Ejercicio11
from Ejercicio14 import Ejercicio14
from Ejercicio15 import Ejercicio15
from Ejercicio16 import Ejercicio16

print()
print("Ejercicio 7:")
ejercicio7 = Ejercicio7()
ejercicio7.ejecucion([[1., 2., 3.],
                      [4., 5., 9.],
                      [7., 8., 6.]], 10000)
# 21.0

print()
print("Ejercicio 11:")
ejercicio11 = Ejercicio11()
ejercicio11.ejecucion([[1., 0., 0.],
                       [0., 1., 0.],
                       [0., 0., 1.]], [[2.], [3.], [4.]])
# [[2.]
#  [3.]
#  [4.]]
ejercicio11.ejecucion([[5., 7., 3.],
                       [0., 8., 9.],
                       [0., 0., -5.]], [[7.], [3.], [1.]])
# [[ 0.68]
#  [ 0.6 ]
#  [-0.2 ]]
ejercicio11.ejecucion([[0., 8., 9.],
                       [5., 7., 3.],
                       [0., 0., -5.]], [[3.], [7.], [1.]])
# [[ 0.68]
#  [ 0.6 ]
#  [-0.2 ]]

print()
print("Ejercicio 14:")
ejercicio14 = Ejercicio14()
ejercicio14.ejecucion([[-1., 1., -4.],
                       [2., 2., 0.],
                       [3., 3., 2.]], [[0.], [1.], [0.5]])
# [[1.25]
#  [-0.75]
#  [-0.5]]

ejercicio14.ejecucion([[1., 6., 0.],
                       [2., 1., 0.],
                       [0., 2., 1.]], [[3.], [1.], [1.]])
# [[0.27272727]
#  [0.45454545]
#  [0.09090909]]

print()
print("Ejercicio 15:")
ejercicio15 = Ejercicio15()
ejercicio15.ejecucion([[1., .5, 1. / 3.],
                       [1. / 3., 1., .5],
                       [.5, 1. / 3., 1.]], [[11. / 8.], [11. / 8.], [11. / 8.]], 100)
# [[0.75]
#  [0.75]
#  [0.75]]

print()
print("Ejercicio 16/17:")
ejercicio16 = Ejercicio16()
ejercicio16.ejecucion([[2., -1., 0.],
                       [1., 6., -2.],
                       [4., -3., 8.]], [[2.], [-4.], [5.]], 25)
# [[ 0.62]
#  [-0.76]
#  [ 0.03]]
