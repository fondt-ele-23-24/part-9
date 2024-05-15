import numpy as np
from base import util
from scipy.integrate import odeint

class PX8Dstate:
    def __init__(self, m, g, rho, V, A, Cd, Tp, Lp):
        self.m = m
        self.g = g
        self.rho = rho
        self.V = V
        self.A = A
        self.Cd = Cd
        self.Tp = Tp
        self.Lp = Lp

    def __call__(self, X, t):
        # "spacchetto" lo stato
        x, v = X
        # recupero il valore di L
        L = np.interp(t, self.Tp, self.Lp)
        # calcolo le forze
        Fg = -self.g * (self.m + self.rho * L)
        Fb = self.g * self.rho * self.V
        Ft = -0.5*self.rho * self.A * self.Cd * v * abs(v)
        # calcolo le derivate
        dx = v
        dv = 1/(self.m + self.rho * L) * (Fg + Fb + Ft)
        return np.array([dx, dv])

    
def simulate(f, X0, t):
    X = odeint(f, X0, t)
    util.plot_state_evolution(X, t, ylabels=['x', 'v'], xlabel='tempo', figsize=(20, 5))
    return X, t

def get_depth(X, t):
    q10 = np.interp(10, t, X[:, 0])
    q20 = np.interp(20, t, X[:, 0])
    q30 = np.interp(20, t, X[:, 0])
    return q10, q20, q30
