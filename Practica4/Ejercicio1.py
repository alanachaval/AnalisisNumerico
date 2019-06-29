from math import cos
from math import sin
import matplotlib.pyplot as plt

n = 200
h = 0.01
t = -1
x = 3
T = [t]
X = [x]

for i in range(n):
    x_1 = cos(t) - sin(x) + t ** 2
    x_2 = -sin(t) - x_1 * cos(x) + 2 * t
    x_3 = -cos(t) - x_2 * cos(x) - (x_1 ** 2) * sin(x) + 2
    x_4 = sin(t) + ((x_1 ** 3) - x_3) * cos(x) + 3 * x_1 * x_2 * sin(x)

    x = x + x_1 * h + x_2 * (h ** 2) / 2 + x_3 * (h ** 3) / 6 + x_4 * (h ** 4) / 24
    t = t + h
    X.append(x)
    T.append(t)

plt.plot(T, X)
plt.xlabel('t')
plt.ylabel('x')
plt.show()
