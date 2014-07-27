
"""
File            variables.py
Author          Rafael Silva Quiroz
email           sqrf87@gmail.com

License	        educational use

Description     This module defines some physical constants used, and defines the Class Metal and Medio, where all the optical and elastic
                information is contained
"""

from pylab import *
#from Parameters import *

# Physical Constants
r_0 = 10
ls = 3e17       # Light Speed (nm/s)
h = 4.13e-15    # Planck Constant eV*S
A = 6.023e23

# Normalization Constants
T_0 = 1e-12


## Bulk constants and variables

class Metal:
    def __init__(self, name, lmin, lmax, w_P, T, E_inf, N, nang, c_lp, c_tp, rho_p, vf, aweigth):
        self.name = name
        self.lmin = lmin
        self.lmax = lmax
        self.w_p = w_P
        self.T = T
        self.E_inf = E_inf
        self.gm = 1 / self.T
        self.N = N
        self.nang = nang
        self.c_lp = c_lp
        self.c_tp = c_tp
        self.rho_p = rho_p
        self.vf = vf
        self.aweigth = aweigth
"""

class MetalLorenz:
    def __init__(self, omega_L, gamma_L, deltaE):
        self.omega_L = omega_L
        self.gamma_L = gamma_L
        self.deltaE = deltaE
"""
class Medio:
    def __init__(self, name, Emedio, c_lm, c_tm,  rho_m):
        self.name = name
        self.Emedio = Emedio
        self.c_lm = c_lm
        self.c_tm = c_tm
        self.rho_m = rho_m




## Variables for the vibration
class Vibration:
    def __init__(self, trange):
        #osc: 0.78e12
        #relax: 7.7e-12
        #trange: 30e-12
        #self.w1 = osc * T_0     # hz
        #self.tau = trelax / T_0    # seconds
        #self.a1 = 1 / self.tau
        self.tmax = trange   # / T_0
        self.resolution_vibration = float(self.tmax) / 200
        self.t = arange(0, self.tmax, self.resolution_vibration)
        #self.t = linspace(0, self.tmax, 500)

"""
    def get_u(self):
        d_1 = float(r_0) / 10
        d = r_0 + d_1 * exp(-self.a1 * self.t) * sin(self.w1 * self.t)
        return d
        """