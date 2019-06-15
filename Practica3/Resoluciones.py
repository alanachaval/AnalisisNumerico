from scipy import optimize

from Practica3.DEJD import DEJD

t_ = 10  # valor parametros

# Inicio Parametros
eta_n = 0.1181
eta_p = 0.0443
lamda = 162.5382
q_p = 0.4894
r = 0.03
r_ = 0.5
div = 0.078
kappa = 1.2433
nu_inf = 0.0151
d_cero = 32.5
nu_cero = 0.0260
s_cero = 25.86
# Fin Parametros

solver = optimize.brentq

dejd = DEJD(eta_n, eta_p, lamda, q_p, r, r_, div, kappa, nu_cero, d_cero, t_, solver)

print(dejd.evaluar(t_, s_cero))
