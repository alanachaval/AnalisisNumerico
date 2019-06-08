import math
from A import A
from B import B
from C import C
from D import D
from Eta import Eta
from Psi import Psi
from Q import Q
from U import U
from V import V
from W import W


class DEJD:

    def __init__(self, eta_n, eta_p, mu, lamda, q_n, q_p, root_solver, b_cero, r, d_, k, t, v_griega):
        eta = Eta(eta_n, eta_p)
        q = Q(q_n, q_p)
        p = t * v_griega
        psi = Psi(eta, mu, p, lamda, q, root_solver)
        c = C(psi, eta, p)
        b = B(b_cero, r, d_)
        d = D(r, b)
        b_ = -math.log((d(t) + k) / d(t))
        a = A(psi, eta, c, b_)
        u = U(c, a, psi)
        v = V(u)
        self.w = W(d, k, t, r, v)

    def evaluar(self, t, s):
        return self.w(t, s)
