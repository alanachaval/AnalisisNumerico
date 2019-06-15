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

parametros = Parametros(eta_n, eta_p, lamda, q_p, r, r_, div, kappa, nu_cero, nu_inf, d_cero)

parametros.rtol = 1.0e-15
parametros.solver = optimize.brentq

# Default
parametros.k = 50
tiempo = np.linspace(0.01, 30, 600)
default = np.zeros((len(tiempo), 1))

for i, t_ in enumerate(tiempo):
    parametros.t_ = t_
    default[i] = DEJD.evaluar_default(0, s_cero, parametros)

f1 = plot.figure(2)
f1.canvas.set_window_title('Default')
plot.plot(tiempo, default)

# Opcion
parametros.t_ = 1/12
strike = np.linspace(8, 55, 600)
opcion = np.zeros((len(strike), 1))

for i, k in enumerate(strike):
    parametros.k = k
    opcion[i] = DEJD.evaluar(0, s_cero, parametros)

f2 = plot.figure(1)
f2.canvas.set_window_title('Opcion')
plot.plot(strike, opcion)

plot.show()
