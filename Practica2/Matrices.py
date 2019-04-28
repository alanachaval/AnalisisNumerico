class Matrices:

    @staticmethod
    def restar_columnas(x, pivot, fila, ratio):
        x[fila] = x[fila] + x[pivot] * ratio
        return x
