import matplotlib.pyplot as plt


def ringe_kuta(f, x, t, h, n):
    T = [t]
    X = [x]
    for k in range(n):
        f_1 = h * f(t, x)
        f_2 = h * f(t + h / 2, x + f_1 / 2)
        f_3 = h * f(t + h / 2, x + f_2 / 2)
        f_4 = h * f(t + h, x + f_3)

        x = x + (f_1 + 2 * f_2 + 2 * f_3 + f_4) / 6
        t = t + h
        X.append(x)
        T.append(t)
    return T, X


# Ejercicio3

f = lambda t, x: (t ** -2) * (t * x - (x ** 2))
x = 2
t = 1
h = 0.005
n = int(3 / h)
T, X = ringe_kuta(f, x, t, h, n)

plt.plot(T, X)
plt.show()
