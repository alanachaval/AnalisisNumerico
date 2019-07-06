import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import gridspec
from mpl_toolkits.mplot3d import Axes3D


def heat_function(g, h, k, t_max, nombre, fig_id):
    x = np.linspace(0, 1, int(1 / h), endpoint=True)
    s = k / h ** 2
    a = np.zeros((len(x), len(x)))
    for i in range(len(x) - 1):
        a[i, i] = 1 + 2 * s
        a[i + 1, i] = -s
        a[i, i + 1] = -s
    a[-1, -1] = 1 + 2 * s
    print(a)
    u = []
    u_j = np.zeros(len(x))
    for index, x_i in enumerate(x):
        u_j[index] = g(x_i)
    u.append(u_j)
    t = np.linspace(0, t_max, int(t_max / k), endpoint=True)
    for t_j in range(len(t) - 1):
        u_j = np.linalg.solve(a, u_j)
        u.append(u_j)
    print(u)

    f2 = plt.figure(fig_id)
    f2.canvas.set_window_title('Transmision de Calor ' + nombre)
    ax = f2.gca(projection='3d')
    eje_x, eje_y = np.meshgrid(x, t)

    surf = ax.plot_surface(eje_x, eje_y, np.array(u), cmap=cm.coolwarm, linewidth=0, antialiased=False)

    ax.view_init(azim=120)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Temp')

    f2.colorbar(surf, shrink=0.5, aspect=5)


def g_1(x):
    return math.sin(x * np.pi)


def g_2(x):
    return math.e ** (x * math.sin(x * np.pi))


def g_3(x):
    return 400 * math.e ** (x * math.sin(np.pi / 4 + x * (np.pi / 2)))


def g_4(x):
    return 400 * np.pi / 4 + x * (np.pi / 2)


def g_5(x):
    return math.sin(x * np.pi * 4) ** 2


heat_function(g_1, 0.01, 0.01, 0.5, 'math.sin(x * np.pi)', 1)
heat_function(g_2, 0.01, 0.01, 0.5, 'math.e ** (x * math.sin(x * np.pi))', 2)
heat_function(g_3, 0.01, 0.01, 0.5, '400 * math.e ** (x * math.sin(np.pi / 4 + x * (np.pi / 2)))', 3)
heat_function(g_4, 0.01, 0.01, 0.5, '400 * np.pi / 4 + x * (np.pi / 2)', 4)
heat_function(g_5, 0.01, 0.01, 0.5, 'math.sin(x * np.pi * 4) ** 2', 5)

plt.show()
