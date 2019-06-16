class Psi:

    def __init__(self, cero, uno, dos, tres):
        self.cero = cero
        self.uno = uno
        self.dos = dos
        self.tres = tres

    @staticmethod
    def evaluar(p, parametros):
        mu = parametros.mu
        lamda = parametros.lamda
        eta = parametros.eta
        q = parametros.q

        a = p
        b = (-mu + (p + lamda) * (eta.n - eta.p) - lamda * (q.p * eta.n - q.n * eta.p))
        c = -(0.5 + mu * (eta.n - eta.p) + (p + lamda) * eta.n * eta.p)
        d = mu * eta.n * eta.p - 0.5 * (eta.n - eta.p)
        e = 0.5 * eta.n * eta.p

        def func(x):
            return e * (x ** 4) + d * (x ** 3) + c * (x ** 2) + b * x + a

        def fprime(x):
            return 4 * e * (x ** 3) + 3 * d * (x ** 2) + 2 * c * x + b

        solver = parametros.solver
        rtol = parametros.rtol
        maxiter = parametros.maxiter

        ratio = 10
        i_uno = -1.0 / eta.n
        dos = solver(func, i_uno, 0, rtol, fprime, maxiter)
        i_cero = i_uno * ratio
        while func(i_uno) * func(i_cero) > 0:
            i_uno = i_cero
            i_cero = i_uno * ratio
        tres = solver(func, i_cero, i_uno, rtol, fprime, maxiter)
        i_dos = 1.0 / eta.p
        uno = solver(func, 0, i_dos, rtol, fprime, maxiter)
        i_tres = i_dos * ratio
        while func(i_tres) * func(i_dos) > 0:
            i_dos = i_tres
            i_tres = i_dos * ratio
        cero = solver(func, i_dos, i_tres, rtol, fprime, maxiter)

        return Psi(cero, uno, dos, tres)
