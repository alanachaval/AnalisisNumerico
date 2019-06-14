import math
from scipy import optimize

from Practica3.DEJD import DEJD

t = 500  # valor parametros

# Inicio Parametros
nu_0 = 0.0260
nu_inf = 0.0151
kappa = 1.2433
lamda = 162.5382
eta_p = 0.0443
eta_n = 0.1181
q_p = 0.4894
# Fin Parametros

q_n = 1 - q_p
root_solver = optimize.brentq
d_ = 0.078
r = 0.03
d_cero = 32.5
s_cero = 25.86
d_t = d_cero * (math.e ** ((t - 0) * (r - d_)))

alfa = q_p / (1 - eta_p) + q_n / (1 - eta_n) - 1
mu = -0.5 - lamda * alfa
v_griega = nu_inf * t - (nu_0 - nu_inf) / kappa * (math.e ** (-0 * t) - 1)


dejd = DEJD(eta_n, eta_p, mu, lamda, q_n, q_p, root_solver, d_t, r, d_, k, t, v_griega, d_cero)

print(dejd.evaluar(0, s_cero))
