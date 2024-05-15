import numpy as np
from base import util
from scipy.integrate import odeint

class Dstate:
    def __init__(self, Ca, Cw, Rca, Raw, Rwo, Tc, To):
        self.Ca = Ca
        self.Cw = Cw
        self.Rca = Rca
        self.Raw = Raw
        self.Rwo = Rwo
        self.Tc = Tc
        self.To = To

    def __call__(self, X, t):
        # "spacchetto" lo stato
        Ta, Tw = X
        # Calcolo le correnti
        wca = 1/self.Rca * (self.Tc - Ta)
        waw = 1/self.Raw * (Ta - Tw)
        wwo = 1/self.Rwo * (Tw - self.To)
        # Calcolo le derivate
        dTa = 1/self.Ca * (wca - waw)
        dTw = 1/self.Cw * (waw - wwo)
        # Restituisco il risultato
        return np.array([dTa, dTw])

    
def simulate(f, X0, t):
    X = odeint(f, X0, t)
    util.plot_state_evolution(X, t, ylabels=['Ta', 'Tw'], xlabel='t', figsize=(20, 5))
    return X, t


def final_temp(X, t):
    Taf, Taw = X[-1, 0], X[-1, 1]
    return Taf, Taw


def temp_in_1h(X, t):
    Ta1h = np.interp(3600, t, X[:, 0])
    Tw1h = np.interp(3600, t, X[:, 1])
    return Ta1h, Tw1h


def time_to_20C(X, t):
    return np.interp(20, X[:, 0], t)

