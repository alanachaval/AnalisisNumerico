from A import A
from C import C
from D import D
from Eta import Eta
from Psi import Psi
from Q import Q
from U import U
from V import V
from W import W


class DEJD:

    def __init__(self, eta_n, eta_p, mu, lamda, q_n, q_p, root_solver, r, k, t):
        eta = Eta(eta_n, eta_p)
        q = Q(q_n, q_p)
        p = 0  # tau, calcular
        psi = Psi(eta, mu, p, lamda, q, root_solver)
        c = C(psi, eta, p)
        b = 0  # -a, calcular
        a = A(psi, eta, c, b)
        u = U(c, a, psi)
        v = V(u)
        # b = B(), implementar
        d = D(r, b)
        self.w = W(d, k, t, r, v)

    def evaluar(self, t, s):
        return self.w(t, s)
