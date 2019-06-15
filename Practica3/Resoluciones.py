import matplotlib.pyplot as plot
import numpy as np
from scipy import optimize

from Practica3.DEJD import DEJD
from Practica3.Parametros import Parametros

# Inicio Parametros
eta_n = 0.1181
eta_p = 0.0443
lamda = 162.5382
q_p = 0.4894
r = 0.03
r_ = 0.5
div = 0.078
kappa = 1.2433
nu_cero = 0.0260
nu_inf = 0.0151
d_cero = 32.5
s_cero = 25.86
# Fin Parametros

parametros = Parametros(eta_n, eta_p, lamda, q_p, r, r_, div, kappa, nu_cero, nu_inf, d_cero, s_cero)

parametros.rtol = 1.0e-15
parametros.solver = optimize.brentq
parametros.k = 50

tiempo = np.linspace(3, 40, 600)
opcion = np.zeros((len(tiempo), 1))
default = np.zeros((len(tiempo), 1))

for i, t_ in enumerate(tiempo):
    parametros.t_ = t_
    opcion[i] = DEJD.evaluar(0, 30, parametros)
    default[i] = DEJD.evaluar_default(0, 30, parametros)

plot.plot(tiempo, opcion)
plot.plot(tiempo, default)
plot.show()
