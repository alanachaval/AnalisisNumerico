class Psi:

    def __init__(self, eta, mu, p, lamda, q, solver):
        a = p
        b = (-mu + (p + lamda) * (eta.n - eta.p) - lamda * (q.p * eta.n - q.n * eta.p))
        c = -(0.5 + mu * (eta.n - eta.p) + (p + lamda) * eta.n * eta.p)
        d = mu * eta.n * eta.p - 0.5 * (eta.n * eta.p)
        e = 0.5 * eta.n * eta.p

        def evaluar(x):
            return e * (x ** 4) + d * (x ** 3) + c * (x ** 2) + b * x + a

        self.cero = solver(evaluar, None, -1.0 / eta.n)
        self.uno = solver(evaluar, -1.0 / eta.n, 0)
        self.dos = solver(evaluar, 0, 1.0 / eta.p)
        self.tres = solver(evaluar, 1.0 / eta.p, None)
