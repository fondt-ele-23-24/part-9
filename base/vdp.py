import numpy as np

def vdp_dstate(state, t):
    mu = 1
    x, y = state # "spacchetto" lo stato
    dx = y
    dy = mu * (1 - x**2) * y - x
    return np.array([dx, dy])


class VdpDstate:
    def __init__(self, mu):
        self.mu = mu
    
    def __call__(self, state, t):
        mu = self.mu # recupero mu dall'istanza corrente
        x, y = state
        dx = y
        dy = mu * (1 - x**2) * y - x
        return np.array([dx, dy])
