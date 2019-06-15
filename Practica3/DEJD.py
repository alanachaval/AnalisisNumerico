from Practica3.Alfa import Alfa
from Practica3.B import B
from Practica3.D import D
from Practica3.Eta import Eta
from Practica3.Mu import Mu
from Practica3.Q import Q
from Practica3.W import W


class DEJD:

    def __init__(self, eta_n, eta_p, lamda, q_p, r, r_, div, kappa, nu_cero, d_cero, t_, solver):
        eta = Eta(eta_n, eta_p)
        q = Q(q_p)
        alfa = Alfa.evaluar(q, eta)
        mu = Mu.evaluar(lamda, alfa)
        d_t = D.evaluar(d_cero, r_, div, t_)
        b = B.evaluar(d_t, kappa)
        self.w = W(eta, mu, lamda, q, b, d_cero, d_t, kappa, r, nu_cero, solver)

    def evaluar(self, t, s):
        return self.w.evaluar(t, s)
