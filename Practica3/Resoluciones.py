import math
from scipy import optimize

from Practica3.DEJD import DEJD

t = 10  # valor parametros

# Inicio Parametros
nu_0 = 0.0260
nu_inf = 0.0151
kappa = 1.2433
lamda = 162.5382
eta_p = 0.0443
eta_n = 0.1181
q_p = 0.4894
# Fin Parametros

root_solver = optimize.brentq
div = 0.078
r = 0.03
d_cero = 32.5
s_cero = 25.86

v_griega = nu_inf * t - (nu_0 - nu_inf) / kappa * (math.e ** (-0 * t) - 1)

# self.s_0 = 25.86
# self.d_0 = 32.5
# self.r = 0.03
# self.d = 0.078
# self.R = 0.5


dejd = DEJD(eta_n, eta_p, lamda, q_p, root_solver, r, div, kappa, t, v_griega, d_cero)

print(dejd.evaluar(0, s_cero))
