
"""
File            metals.py
Author          Rafael Silva Quiroz
email           sqrf87@gmail.com

License	        educational use

Description     Optical and elastic parameters of metals and media written in class objects
Return          Class Conductors, Media
Reference       Various data bases: CRC Handbook of Chemistry and Physics, 7 Edition 1990-1991, David R. Lide.
                M. A. Ordal, R. J. Bell, R. W. Alexander, Jr., L. L. Long, and M. R. Querry, Optical properties of
                fourteen metals in the infrared and far infrared: Al, Co, Cu, Au, Fe, Pb, Mo, Ni, Pd, Pt, Ag, Ti, V,
                and W, Appl. Opt. 24, 4493-4499 (1985)
"""


from variables import *



#metal(name, lmin, lmax, w_P, T, E_inf, N, number of angles, c_lp, c_tp,  rho_p, fermi_velocity,  atomic weigth):

class Conductors:
    def __init__(self):
        self.Au = Metal('Au', 400, 600, 1.39e16, 9.3e-15, 9.1, 1500,  2, 3240, 1200,  19700, 1.40e6, 196.96)
        self.Ag = Metal('Ag', 200, 600, 1.38e16, 3.1e-14, 3.7, 1500, 2, 3650, 1610,  10400, 1.396e6, 107.86)
        self.Cu = Metal('Cu', 200, 600, 1.20e16, 1.90e-14, 1, 1500,  2, 4760, 2325,  8930, 1.57e6, 63.54)
        self.Pt = Metal('Pt', 200, 600, 0.77e16, 9.51e-15, 1, 1500,  2, 3260, 1730,  21400, 1.4e6, 195.08)
        self.Al = Metal('Al', 100, 300, 2.24e16, 8.04e-15, 1, 1500,  2, 6420, 3040,  2700, 2.03e6, 26.98)
     #     self.K = Metal

# Medio(name, Emedio, c_lm, c_tm, rho_m)
class Media:
    def __init__(self):
        self.air = Medio('air', 1, 330,  0.001, 1.2) #1.2
        self.water = Medio('water', 1, 1500,  0.000001, 998) #998
        self.glass = Medio('glass', 2.5, 5640 ,3280, 3800) # 3800