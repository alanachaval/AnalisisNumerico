from Practica3.W import W


class DEJD:

    @staticmethod
    def evaluar(t, s, parametros):
        return W.evaluar(t, s, parametros)

    @staticmethod
    def evaluar_default(t, s, parametros):
        return 1 - W.evaluar_default(t, s, parametros)
