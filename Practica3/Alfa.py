class Alfa:

    @staticmethod
    def evaluar(q, eta):
        return q.p / (1 - eta.p) + q.n / (1 + eta.n) - 1
