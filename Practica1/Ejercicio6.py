import math


class Ejercicio6:

    def funcion_f(self, x):
        return math.sqrt(x ** 2 + 1) - 1

    def funcion_g(self, x):
        return x ** 2 / (math.sqrt(x ** 2 + 1) + 1)

    def ejecucion(self):
        base = 8
        for x in range(1, 11):
            print("X: ", x)
            print("F: ", self.funcion_f(base ** -x))
            print("G: ", self.funcion_g(base ** -x))
        print("G es mas confiable, al evitar restar numeros similares lo cual genera un alto error relativo.")
