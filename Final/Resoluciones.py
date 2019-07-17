from collections import deque


class Elemento:
    def __init__(self, valor, peso):
        self.valor = valor
        self.peso = peso

    def __repr__(self):
        return 'Elemento(%s, %s)' % (self.valor, self.peso)


class Nodo:
    def __init__(self, nivel, ganancia, peso, elemento, padre):
        # Profundidad del nodo.
        self.nivel = nivel
        # Ganancia total del sub-arbol.
        self.ganancia = ganancia
        # Peso total del sub-arbol.
        self.peso = peso
        # Elemento asociado al nodo del arbol
        self.elemento = elemento
        # Nodo padre
        self.padre = padre
        # Maxima ganancia posible utilizando este sub-arbol.
        self.limite = 0


def calcular_limite(nodo, capacidad, elementos):
    """Maxima ganancia posible utilizando este sub-arbol, se calcula con fracciones de los elementos."""
    if nodo.peso >= capacidad:
        return 0
    limite = nodo.ganancia
    peso_total = nodo.peso
    i = nodo.nivel + 1
    while i < len(elementos) and peso_total + elementos[i].peso <= capacidad:
        peso_total += elementos[i].peso
        limite += elementos[i].valor
        i += 1
    if i < len(elementos):
        limite += (capacidad - peso_total) * elementos[i].valor / elementos[i].peso
    return limite


def knapsack(capacidad, elementos):
    """Resuelve Knapsack con Branch and Bound"""
    # Se ordenan los elemntos por relacion valor-peso, para calcular los limites de los sub-arboles
    elementos = sorted(elementos, key=lambda elemento: elemento.valor / elemento.peso)
    maxima_ganancia = Nodo(-1, 0, 0, None, None)
    cola = deque([maxima_ganancia])
    while cola:
        padre = cola.popleft()
        nivel = padre.nivel + 1
        if nivel >= len(elementos):
            continue
        elemento = elementos[nivel]
        hijo = Nodo(nivel, padre.ganancia + elemento.valor, padre.peso + elemento.peso, elemento, padre)
        hijo.limite = calcular_limite(hijo, capacidad, elementos)
        if hijo.peso <= capacidad and hijo.ganancia > maxima_ganancia.ganancia:
            maxima_ganancia = hijo
        if hijo.limite > maxima_ganancia.ganancia:
            cola.append(hijo)
        hijo = Nodo(nivel, padre.ganancia, padre.peso, None, padre)
        hijo.limite = calcular_limite(hijo, capacidad, elementos)
        if hijo.limite > maxima_ganancia.ganancia:
            cola.append(hijo)
    return maxima_ganancia


def obtener_resultado(subarbol):
    resultado = []
    while subarbol is not None:
        if subarbol.elemento is not None:
            resultado.append(subarbol.elemento)
        subarbol = subarbol.padre
    return resultado


def main():
    # Instancia de http://artemisa.unicauca.edu.co/~johnyortega/instances_01_KP/
    capacidad = 1000
    elementos = [
        Elemento(100, 995),
        Elemento(94, 485),
        Elemento(506, 326),
        Elemento(416, 248),
        Elemento(992, 421),
        Elemento(649, 322),
        Elemento(237, 795),
        Elemento(457, 43),
        Elemento(815, 845),
        Elemento(446, 955),
        Elemento(422, 252),
        Elemento(791, 9),
        Elemento(359, 901),
        Elemento(667, 122),
        Elemento(598, 94),
        Elemento(7, 738),
        Elemento(544, 574),
        Elemento(334, 715),
        Elemento(766, 882),
        Elemento(994, 367),
        Elemento(893, 984),
        Elemento(633, 299),
        Elemento(131, 433),
        Elemento(428, 682),
        Elemento(700, 72),
        Elemento(617, 874),
        Elemento(874, 138),
        Elemento(720, 856),
        Elemento(419, 145),
        Elemento(794, 995),
        Elemento(196, 529),
        Elemento(997, 199),
        Elemento(116, 277),
        Elemento(908, 97),
        Elemento(539, 719),
        Elemento(707, 242),
        Elemento(569, 107),
        Elemento(537, 122),
        Elemento(931, 70),
        Elemento(726, 98),
        Elemento(487, 600),
        Elemento(772, 645),
        Elemento(513, 267),
        Elemento(81, 972),
        Elemento(943, 895),
        Elemento(58, 213),
        Elemento(303, 748),
        Elemento(764, 487),
        Elemento(536, 923),
        Elemento(724, 29),
        Elemento(789, 674),
        Elemento(479, 540),
        Elemento(142, 554),
        Elemento(339, 467),
        Elemento(641, 46),
        Elemento(196, 710),
        Elemento(494, 553),
        Elemento(66, 191),
        Elemento(824, 724),
        Elemento(208, 730),
        Elemento(711, 988),
        Elemento(800, 90),
        Elemento(314, 340),
        Elemento(289, 549),
        Elemento(401, 196),
        Elemento(466, 865),
        Elemento(689, 678),
        Elemento(833, 570),
        Elemento(225, 936),
        Elemento(244, 722),
        Elemento(849, 651),
        Elemento(113, 123),
        Elemento(379, 431),
        Elemento(361, 508),
        Elemento(65, 585),
        Elemento(486, 853),
        Elemento(686, 642),
        Elemento(286, 992),
        Elemento(889, 725),
        Elemento(24, 286),
        Elemento(491, 812),
        Elemento(891, 859),
        Elemento(90, 663),
        Elemento(181, 88),
        Elemento(214, 179),
        Elemento(17, 187),
        Elemento(472, 619),
        Elemento(418, 261),
        Elemento(419, 846),
        Elemento(356, 192),
        Elemento(682, 261),
        Elemento(306, 514),
        Elemento(201, 886),
        Elemento(385, 530),
        Elemento(952, 849),
        Elemento(500, 294),
        Elemento(194, 799),
        Elemento(737, 391),
        Elemento(324, 330),
        Elemento(992, 298),
        Elemento(224, 790)
    ]
    subarbol = knapsack(capacidad, elementos)
    resultado = obtener_resultado(subarbol)
    print('Valor total del Knapsack: ' + str(subarbol.ganancia))
    print('Elementos: ' + str(resultado))


if __name__ == "__main__":
    main()
