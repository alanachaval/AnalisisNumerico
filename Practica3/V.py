import math

from Practica3.U import U


class V:
    lamda = [0.00277778, -6.40277778, 924.05000000, -34597.92777778, 540321.11111111, -4398346.36666666,
             21087591.77777770, -63944913.04444440, 127597579.55000000, -170137188.08333300,
             150327467.03333300, -84592161.50000000, 27478884.76666660, -3925554.96666666]

    @staticmethod
    def evaluar(tau, y, parametros):
        return (
                math.log(2) / tau *
                sum(
                    V.lamda[j - 1] * U.evaluar(j * math.log(2) / tau, y, parametros)
                    for j in range(1, len(V.lamda) + 1)
                )
        )

    @staticmethod
    def evaluar_default(tau, y, parametros):
        return (
                math.log(2) / tau *
                sum(
                    V.lamda[j - 1] * U.evaluar_default(j * math.log(2) / tau, y, parametros)
                    for j in range(1, len(V.lamda) + 1)
                )
        )
