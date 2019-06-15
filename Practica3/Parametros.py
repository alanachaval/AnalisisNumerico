from Practica3.Eta import Eta
from Practica3.Mu import Mu
from Practica3.Nu import Nu
from Practica3.Q import Q


class Parametros:

    def __init__(self, eta_n, eta_p, lamda, q_p, r, r_, div, kappa, nu_cero, nu_inf, d_cero):
        self.eta = Eta(eta_n, eta_p)
        self.lamda = lamda
        self.q = Q(q_p)
        self.r = r
        self.r_ = r_
        self.div = div
        self.kappa = kappa
        self.nu = Nu(nu_cero, nu_inf)
        self.d_cero = d_cero
        self.mu = Mu.evaluar(self)
