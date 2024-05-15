import numpy as np
from base import util
from scipy.integrate import odeint

class BMWDstate:
    def __init__(self, rho, A, Cd, m, F):
        self.rho = rho
        self.A = A
        self.Cd = Cd
        self.m = m
        self.F = F

    def __call__(self, X, t):
        # "spacchetto" lo stato
        x, v = X
        # Calcolo la forza di trascinamento
        Ft = -0.5 * self.rho * self.Cd * self.A * v * abs(v)
        # Calcolo le derivate
        dx = v
        dv = 1/self.m * (self.F + Ft)
        # Restituisco il risultato
        return np.array([dx, dv])

    
def simulate(f, X0, t):
    X = odeint(f, X0, t)
    util.plot_state_evolution(X, t, ylabels=['x', 'v'], xlabel='tempo', figsize=(20, 5))
    return X, t


def x_in_3s(X, t):
    return np.interp(3, t, X[:, 1])


def time_to_100kph(X, t):
    return np.interp(27.8, X[:, 1], t)


def max_speed(X, t):
    return np.max(X[:, 1])
    

