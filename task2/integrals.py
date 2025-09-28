import numpy as np
import scipy.integrate as scipy_integr

def monte_carlo_integral(lower, upper, function, points):
    x_random = np.random.uniform(lower, upper, points)
    y_random = function(x_random)
    return (upper - lower) * np.mean(y_random)

def scipyquad_integral(function, lower, upper):
    return scipy_integr.quad(function, lower, upper)


# chosen function
def f(x):
    return x**3 + 3

def f_integral(lower, upper):
    return ((upper**4)/4 + 3*upper) - ((lower**4)/4 + 3*lower)