from Practica3.V import V


class DEJD:

    @staticmethod
    def evaluar(self, t, s, parametros):
        return self.w.evaluar(t, s, parametros)

    @staticmethod
    def evaluar_default(t, s, parametros):
        return V.evaluar_default(t, s, parametros)
