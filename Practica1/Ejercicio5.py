class Ejercicio5:

    def sumatoria_por_division(self, r):
        return r / (1 - r)

    def calcular_x_n(self, r, n):
        return r ** n

    def ejecucion(self, epsilon):
        r = 0.99
        n = 1
        suma = 0
        real = self.sumatoria_por_division(r)
        while (abs(suma - real) > epsilon and self.calcular_x_n(r, n) > epsilon and n < 100000):
            suma += self.calcular_x_n(r, n)
            n += 1
        print("Sumatoria: ", suma)
        print("Por Funcion r/(1-r): ", real)
        print("Diferencia: ", abs(real - suma))
        if (abs(suma - real) > epsilon):
            print("Diferencia > Epsilon")
        else:
            print("Diferencia < Epsilon")
        print("Epsilon: ", epsilon)
        print("Ultimo Xn: ", self.calcular_x_n(r, n))
        print("N: ", n)
        if (self.calcular_x_n(r, n) > epsilon):
            print("Xn > Epsilon")
        else:
            print("Xn < Epsilon")
        if (self.calcular_x_n(r, n) < epsilon and abs(suma - real) > epsilon):
            print("No se debe dejar de sumar cuando Xn < Epsilon.")
        else:
            print("Se debe dejar de sumar cuando Xn < Epsilon.")
