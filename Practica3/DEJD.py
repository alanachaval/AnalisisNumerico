from Practica3.Alfa import Alfa
from Practica3.B import B
from Practica3.D import D
from Practica3.Eta import Eta
from Practica3.Mu import Mu
from Practica3.Q import Q
from Practica3.VDefault import VDefault
from Practica3.W import W


class DEJD:

    def __init__(self, eta_n, eta_p, lamda, q_p, r, r_, div, kappa, nu_cero, nu_inf, d_cero, t_, t, solver, rtol):
        eta = Eta(eta_n, eta_p)
        q = Q(q_p)
        alfa = Alfa.evaluar(q, eta)
        mu = Mu.evaluar(lamda, alfa)
        d_t = D.evaluar(d_cero, r_, div, t_, t)
        b = B.evaluar(d_t, kappa)
        self.w = W(eta, mu, lamda, q, b, d_cero, d_t, kappa, r, nu_cero, nu_inf, t_, solver, rtol)
        self.vDefault = VDefault(eta, mu, lamda, q, nu_cero, nu_inf, t_, kappa, d_t, solver, rtol)

    def evaluar(self, t, s):
        return self.w.evaluar(t, s)

    def evaluarDefault(self, t, s):
        return self.vDefault.evaluar(t, s)
