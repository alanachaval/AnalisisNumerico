class ADefault:

    def __init__(self, eta, p, psi):
        self.tres = - (1 / p) * psi.tres * (1 + eta.n * psi.dos) / (psi.tres - psi.dos)
        self.dos = (1 / p) * psi.dos * (1 + eta.n * psi.tres) / (psi.tres - psi.dos)
