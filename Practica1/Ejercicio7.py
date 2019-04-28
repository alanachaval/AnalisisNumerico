class Ejercicio7:

    def ejecucion(self):
        epsilon = 1
        while 1 - epsilon != 1:
            epsilon = epsilon / 2
        print("Epsilon de maquina aproximado: ", epsilon / 2)
        return epsilon
