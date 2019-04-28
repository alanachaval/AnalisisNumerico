import math


class Ejercicio11:

    # S (x ^ n) * (e ^ x) dx = (x ^ n) * (e ^ x) - n * S (x ^ (n - 1)) * (e ^ x) dx
    # Si el intervalo es 0-1 =>
    # Para n > 0
    # S (x ^ n) * (e ^ x) dx = e - n * S (x ^ (n - 1)) * (e ^ x) dx
    # Para n = 0
    # S (e ^ x) dx = e - 1
    #
    # Pendiente demostrar que si lim n -> inf => y(n) -> 0
    def integral(self, n):
        if n == 0:
            return math.e - 1
        return math.e - (n * self.integral(n - 1))

    def ejecucion(self, max_n):
        for n in range(0, max_n + 1):
            print("N: ", n, ". Resultado: ", self.integral(n))
