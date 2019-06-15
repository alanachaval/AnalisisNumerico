class Alfa:

    @staticmethod
    def evaluar(parametros):
        q = parametros.q
        eta = parametros.eta
        return q.p / (1 - eta.p) + q.n / (1 + eta.n) - 1
