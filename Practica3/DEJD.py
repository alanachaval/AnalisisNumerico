import math
from A import A
from C import C
from Eta import Eta
from Psi import Psi
from Q import Q
from U import U
from V import V
from W import W


class DEJD:

    def __init__(self, eta_n, eta_p, mu, lamda, q_n, q_p, root_solver, d_t, r, d_, k, t, v_griega, d_cero):
        eta = Eta(eta_n, eta_p)
        q = Q(q_n, q_p)
        p = t * v_griega
        psi = Psi(eta, mu, p, lamda, q, root_solver)
        c = C(psi, eta, p)
        b_ = -math.log((d_t + k) / d_t)
        a = A(psi, eta, c, b_)
        u = U(c, a, psi)
        v = V(u)
        self.w = W(d_cero, d_t, k, t, r, v)

    def evaluar(self, t, s):
        return self.w(t, s)
