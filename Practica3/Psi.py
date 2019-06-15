from Practica3.Mu import Mu


class Psi:

    def __init__(self, cero, uno, dos, tres):
        self.cero = cero
        self.uno = uno
        self.dos = dos
        self.tres = tres

    @staticmethod
    def evaluar(p, parametros):
        mu = Mu.evaluar(parametros)
        lamda = parametros.lamda
        eta = parametros.eta
        q = parametros.q

        a = p
        b = (-mu + (p + lamda) * (eta.n - eta.p) - lamda * (q.p * eta.n - q.n * eta.p))
        c = -(0.5 + mu * (eta.n - eta.p) + (p + lamda) * eta.n * eta.p)
        d = mu * eta.n * eta.p - 0.5 * (eta.n - eta.p)
        e = 0.5 * eta.n * eta.p

        def polinomio(x):
            return e * (x ** 4) + d * (x ** 3) + c * (x ** 2) + b * x + a

        solver = parametros.solver
        rtol = parametros.rtol

        ratio = 10
        i_uno = -1.0 / eta.n
        uno = solver(polinomio, i_uno, 0, rtol=rtol)
        i_cero = i_uno * ratio
        while polinomio(i_uno) * polinomio(i_cero) > 0:
            i_uno = i_cero
            i_cero = i_uno * ratio
        cero = solver(polinomio, i_cero, i_uno, rtol=rtol)
        i_dos = 1.0 / eta.p
        dos = solver(polinomio, 0, i_dos, rtol=rtol)
        i_tres = i_dos * ratio
        while polinomio(i_tres) * polinomio(i_dos) > 0:
            i_dos = i_tres
            i_tres = i_dos * ratio
        tres = solver(polinomio, i_dos, i_tres, rtol=rtol)

        return Psi(cero, uno, dos, tres)
