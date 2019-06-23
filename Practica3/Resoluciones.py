import sys
import time

import math
import matplotlib.pyplot as plot
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from numpy import linalg

from Practica3.DEJD import DEJD
from Practica3.Parametros import Parametros

# Inicio Parametros
from Practica3.Psi import Psi
from Practica3.Raices import Raices
from Practica3.Tau import Tau

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

parametros = Parametros(eta_n, eta_p, lamda, q_p, r, r_, div, kappa, nu_cero, nu_inf, d_cero)
# Fin Parametros

print()
print("Ejercicio 2:")

parametros.t_ = 30
parametros.maxiter = 400
rtols = [1.0e-3, 1.0e-6, 1.0e-9, 1.0e-12, 1.0e-15]
solvers = [Raices.newton_rapson, Raices.bisect, Raices.brentq]
solvers_names = ["newton_rapson", "bisect", "brentq"]

mejor_solver = 0
mejor_tiempo = sys.maxsize
p = 10 * math.log(2) / Tau.evaluar(0, parametros)

for i, solver in enumerate(solvers):
    parametros.solver = solver
    print("Solver:", solvers_names[i])
    inicio = time.time_ns()
    for j, rtol in enumerate(rtols):
        parametros.rtol = rtol
        for k in range(1000):
            Psi.evaluar(p, parametros)
    fin = time.time_ns()
    tiempo = fin - inicio
    print("Tiempo:", tiempo)
    if tiempo < mejor_tiempo:
        mejor_tiempo = tiempo
        mejor_solver = i

print("El solver con mejor rendimiento es:", solvers_names[mejor_solver])

if True:
    parametros.rtol = 1.0e-9
    parametros.maxiter = 400
    parametros.solver = Raices.brentq
    psi = Psi.evaluar(p, parametros)
    eta = parametros.eta
    coeficientes = np.array(
        [(1, 1, -1, -1),
         (psi.cero, psi.uno, -psi.dos, -psi.tres),
         (1.0 / (psi.cero * eta.n + 1), 1.0 / (psi.uno * eta.n + 1),
          -1.0 / (psi.dos * eta.n + 1), -1.0 / (psi.tres * eta.n + 1)),
         (1.0 / (psi.cero * eta.p - 1), 1.0 / (psi.uno * eta.p - 1),
          -1.0 / (psi.dos * eta.p - 1), -1.0 / (psi.tres * eta.p - 1))])
    n_cond = linalg.cond(coeficientes)
    print("Numero de condicion de C:", n_cond)

rtols = [1.0e-5, 1.0e-6, 1.0e-7, 1.0e-8, 1.0e-9, 1.0e-10, 1.0e-11, 1.0e-12, 1.0e-13, 1.0e-14, 1.0e-15]

for rtol_index, rtol in enumerate(rtols):
    identificador = ' Usando rtol:' + str(rtol)
    parametros.rtol = rtol
    parametros.maxiter = 400
    parametros.solver = Raices.brentq

    # Default
    parametros.k = 50
    tiempo = np.linspace(0.01, 30, 600)
    default = np.zeros((len(tiempo), 1))

    for i, t_ in enumerate(tiempo):
        parametros.t_ = t_
        default[i] = DEJD.evaluar_default(0, s_cero, parametros)

    f1 = plot.figure(rtol_index * 2 + 1)
    f1.canvas.set_window_title('Default' + identificador)
    plot.xlabel('Tiempo (en años)')
    plot.ylabel('Probabilidad de default')
    plot.plot(tiempo, default)

    # Opcion
    strike = np.linspace(0.01, 55, 60)
    madurez = np.linspace(0.01, 3, 20)
    opcion = np.zeros((len(strike), len(madurez)))

    for i, k in enumerate(strike):
        parametros.k = k
        for j, t_ in enumerate(madurez):
            parametros.t_ = t_
            opcion[i, j] = DEJD.evaluar(0, s_cero, parametros)

    f2 = plot.figure(rtol_index * 2 + 2)
    f2.canvas.set_window_title('Opción' + identificador)
    ax = f2.gca(projection='3d')
    eje_x, eje_y = np.meshgrid(madurez, strike)

    surf = ax.plot_surface(eje_x, eje_y, opcion, cmap=cm.coolwarm, linewidth=0, antialiased=False)

    ax.view_init(azim=120)
    ax.set_xlabel('Madurez (en años)')
    ax.set_ylabel('Strike (en USD)')
    ax.set_zlabel('Precio opción (en USD)')

    f2.colorbar(surf, shrink=0.5, aspect=5)

plot.show()
