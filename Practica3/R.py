class R:

    def __init__(self, r, t):
        self.r = r
        self.t = t

    def evaluar(self, t, s):
        return (self.t - t) * self.r
