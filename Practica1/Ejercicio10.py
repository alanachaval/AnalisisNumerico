import math


class Ejercicio10:

    def formula_recusiva(self, n):
        x_sub_n_menos_2 = 1
        x_sub_n_menos_1 = (1 - math.sqrt(5)) / 2
        x_sub_n = x_sub_n_menos_2
        if n == 1:
            x_sub_n = x_sub_n_menos_1
        for i in range(2, n + 1):
            x_sub_n = x_sub_n_menos_1 + x_sub_n_menos_2
            x_sub_n_menos_2 = x_sub_n_menos_1
            x_sub_n_menos_1 = x_sub_n
        return x_sub_n

    def formula_cerrada(self, n):
        return math.pow((1.0 - math.sqrt(5)) / 2, n)

    def ejecucion(self, valores):
        for n in valores:
            print("N: ", n)
            print("Formula Recusiva: ", self.formula_recusiva(n))
            print("Formula Cerrada: ", self.formula_cerrada(n))
        print("El valor teorico correcto es ((1 - sqrt(5)) / 2) ** n.")
        print("Formula Recusiva no es una forma estable de calcular rn.")
