import numpy as np
from base import util
from scipy.integrate import odeint

class Dstate:
    def __init__(self, g, rho, A, Cd, M):
        self.g = g
        self.rho = rho
        self.A = A
        self.Cd = Cd
        self.M = M

    def __call__(self, X, t):
        # "spacchetto" lo stato
        y, v = X
        # Calcolo le forze
        Fg = -self.g * self.M
        Ft = -0.5 * self.rho * self.A * self.Cd * v * abs(v)
        # Calcolo le derivate
        dx = v
        dv = 1/self.M * (Fg + Ft)
        # Restituisco il risultato
        return np.array([dx, dv])

    
def simulate(f, X0, t):
    X = odeint(f, X0, t)
    util.plot_state_evolution(X, t, ylabels=['y', 'v'], xlabel='t', figsize=(20, 5), same_scale=False)
    return X, t


def y_at_1sec(X, t):
    return np.interp(1, t, X[:, 0])
