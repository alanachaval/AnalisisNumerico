class Ejercicio9:

    def formula_recusiva(self, n):
        x_sub_n_menos_2 = 1
        x_sub_n_menos_1 = 1 / 3
        x_sub_n = x_sub_n_menos_2
        if n == 1:
            x_sub_n = x_sub_n_menos_1
        for i in range(2, n + 1):
            x_sub_n = (13 / 3) * x_sub_n_menos_1 - (4 / 3) * x_sub_n_menos_2
            x_sub_n_menos_2 = x_sub_n_menos_1
            x_sub_n_menos_1 = x_sub_n
        return x_sub_n

    def formula_cerrada(self, n):
        return (1 / 3) ** n

    def ejecucion(self, valores):
        for n in valores:
            print("N: ", n)
            print("Formula Recusiva: ", self.formula_recusiva(n))
            print("Formula Cerrada: ", self.formula_cerrada(n))
        print("La Formula Cerrada es mas confiable al evitar la resta entre numeros similares"
              " y no acumular errores de las operaciones anteriores.")
