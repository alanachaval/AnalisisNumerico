from Practica3.Alfa import Alfa


class Mu:

    @staticmethod
    def evaluar(parametros):
        lamda = parametros.lamda
        alfa = Alfa.evaluar(parametros)
        return -0.5 - lamda * alfa
