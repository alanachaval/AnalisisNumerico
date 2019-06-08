class D:

    def __init__(self, r, b):
        self.r = r
        self.b = b

    def evaluate(self, t):
        return self.r * self.b(t)
