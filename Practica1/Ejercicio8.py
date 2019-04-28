class Ejercicio8:

    def multiplicar_listas(self, x, y):
        return list(item_x * item_y for item_x, item_y in zip(x, y))

    def ejecucion(self, x, y):
        elementos_multiplicados = self.multiplicar_listas(x, y)
        hacia_adelante = sum(elementos_multiplicados)
        print("Hacia adelante: ", hacia_adelante)
        hacia_atras = sum(reversed(elementos_multiplicados))
        print("Hacia atras: ", hacia_atras)

        positivos = list(valor for valor in elementos_multiplicados if valor > 0)
        negativos = list(valor for valor in elementos_multiplicados if valor < 0)

        positivos_mayor_menor_negativos_menor_mayor = sum(sorted(positivos, reverse=True)) + sum(sorted(negativos))
        print("Positivos de mayor a menor + negativos de menor a mayor: ", positivos_mayor_menor_negativos_menor_mayor)

        positivos_menor_mayor_negativos_mayor_menor = sum(sorted(positivos)) + sum(sorted(negativos, reverse=True))
        print("Positivos de menor a mayor + negativos de mayor a menor: ", positivos_menor_mayor_negativos_mayor_menor)

        print("Al sumar los valores positivos de menor a mayor y los negativos de mayor a menor "
              "se reduce el error al evitar que se desprecie el valor de los numeros de menor magnitud.")
