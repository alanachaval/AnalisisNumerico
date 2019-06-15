from Practica3.A import A
from Practica3.Alfa import Alfa
from Practica3.B import B
from Practica3.C import C
from Practica3.D import D
from Practica3.Eta import Eta
from Practica3.Mu import Mu
from Practica3.Psi import Psi
from Practica3.Q import Q
from Practica3.U import U
from Practica3.V import V
from Practica3.W import W


class DEJD:

    def __init__(self, eta_n, eta_p, lamda, q_p, root_solver, r, div, kappa, t, v_griega, d_cero):
        eta = Eta(eta_n, eta_p)
        q = Q(q_p)
        p = t * v_griega
        alfa = Alfa.evaluar(q, eta)
        mu = Mu.evaluar(lamda, alfa)
        psi = Psi(eta, mu, p, lamda, q, root_solver)
        c = C(psi, eta, p)
        d = D.evaluar(d_cero, r, div, t)
        b = B.evaluar(d, kappa)

        # b_ = -math.log((d_t + k) / d_t)
        a = A(psi, eta, c, b)
        u = U(c, a, psi)
        v = V(u)
        self.w = W(d_cero, d, kappa, t, r, v)

    def evaluar(self, t, s):
        return self.w.evaluar(t, s)
