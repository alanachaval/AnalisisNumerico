class Raices:

    def newton_r_b(self, a, b, f, f_p, max_it, x_tol):
        x = (a + b) / 2
        i = 0
        while abs(f(x) > x_tol) and i < max_it and f_p(x) != 0:
            x_new = x - f(x) / f_p(x)
            if a < x_new < b:
                x = x_new
                if f(a) * f(x) < 0:
                    b = x
                else:
                    a = x
            elif f(x) * f(a) < 0:
                x = (x + a) / 2
                b = x

