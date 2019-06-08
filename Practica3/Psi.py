class Psi:

    def __init__(self, eta, mu, p, lamda, q, solver):
        a = p
        b = (-mu + (p + lamda) * (eta.n - eta.p) - lamda * (q.p * eta.n - q.n * eta.p))
        c = -(0.5 + mu * (eta.n - eta.p) + (p + lamda) * eta.n * eta.p)
        d = mu * eta.n * eta.p - 0.5 * (eta.n * eta.p)
        e = 0.5 * eta.n * eta.p

        def evaluar(x):
            return e * (x ** 4) + d * (x ** 3) + c * (x ** 2) + b * x + a

        ratio = 10
        i_uno = -1.0 / eta.n
        self.uno = solver(evaluar, i_uno, 0)
        i_cero = i_uno * ratio
        while evaluar(i_uno) * evaluar(i_cero) > 0:
            i_uno = i_cero
            i_cero = i_uno * ratio
        self.cero = solver(evaluar, i_cero, i_uno)
        i_dos = 1.0 / eta.p
        self.dos = solver(evaluar, 0, i_dos)
        i_tres = i_dos * ratio
        while evaluar(i_tres) * evaluar(i_dos) > 0:
            i_dos = i_tres
            i_tres = i_dos * ratio
        self.tres = solver(evaluar, i_dos, i_tres)
