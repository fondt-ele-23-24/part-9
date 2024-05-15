import numpy as np
from base import util
from scipy.integrate import odeint

class Dstate:
    def __init__(self, G, ME, MM, MS, D):
        self.G = G
        self.ME = ME
        self.MM = MM
        self.MS = MS
        self.D = D

    def __call__(self, X, t):
        # "spacchetto" lo stato
        x, v = X
        # Calcolo le forze
        rse = x
        Fse = -self.G * self.MS * self.ME / (rse * abs(rse))
        rsm = x - self.D
        Fsm = -self.G * self.MS * self.MM / (rsm * abs(rsm))
        # Calcolo le derivate
        dx = v
        dv = 1/self.MS * (Fse + Fsm)
        # Restituisco il risultato
        return np.array([dx, dv])

    
def simulate(f, X0, t):
    X = odeint(f, X0, t)
    util.plot_state_evolution(X, t, ylabels=['x', 'v'], xlabel='t', figsize=(20, 5))
    return X, t


def goal_reached(X, D, rM):
    return np.max(X[:, 0]) >= D - rM 
