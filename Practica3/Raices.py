from scipy import optimize


class Raices:

    @staticmethod
    def newton_rapson(func, a, b, rtol, fprime, maxiter):
        x = (a + b) / 2
        i = 0
        x_new = 0
        while abs(func(x)) > rtol and i < maxiter:
            i += 1
            x_p = fprime(x)
            if x_p != 0:
                x_new = x - func(x) / fprime(x)
            if x_p != 0 and a < x_new < b:
                x = x_new
                if func(a) * func(x) < 0:
                    b = x
                else:
                    a = x
            else:
                x = (b + a) / 2
                if func(a) * func(x) < 0:
                    b = x
                else:
                    a = x
        return x

    @staticmethod
    def brentq(func, a, b, rtol, fprime, maxiter):
        return optimize.brentq(func, a, b, rtol=rtol, maxiter=maxiter)

    @staticmethod
    def bisect(func, a, b, rtol, fprime, maxiter):
        return optimize.bisect(func, a, b, rtol=rtol, maxiter=maxiter)
