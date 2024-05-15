import numpy as np
from base import util
from scipy.integrate import odeint

class Dstate:
    def __init__(self, C1, C2, C3, R12, R23, R31):
        self.C1 = C1
        self.C2 = C2
        self.C3 = C3
        self.R12 = R12
        self.R23 = R23
        self.R31 = R31

    def __call__(self, X, t):
        # "spacchetto" lo stato
        P1, P2, P3 = X
        # Calcolo i flussi
        q12 = 1/self.R12 * (P1 - P2)
        q23 = 1/self.R23 * (P2 - P3)
        q31 = 1/self.R31 * (P3 - P1)
        # Calcolo le derivate
        dP1 = 1/self.C1 * (q31 - q12)
        dP2 = 1/self.C2 * (q12 - q23)
        dP3 = 1/self.C3 * (q23 - q31)
        # Restituisco il risultato
        return np.array([dP1, dP2, dP3])

    
def simulate(f, X0, t):
    X = odeint(f, X0, t)
    util.plot_state_evolution(X, t, ylabels=['P1', 'P2', 'P3'], xlabel='t', figsize=(20, 5), same_scale=True)
    return X, t


def final_P1(X, t):
    return X[-1, 0]


def times_P2_eq_P3(X, t):
    mask_same = np.abs(X[:, 1] - X[:, 2]) < 1e-2
    return t[mask_same]
