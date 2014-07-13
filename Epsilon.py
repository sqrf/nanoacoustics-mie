

"""
File            Epsilon.py
Author          Rafael Silva Quiroz
email           sqrf87@gmail.com

License	        educational use

Description     Correction in dielectric function based on experimental data
Return          E_D_list with values of corrected dielectric function
Reference       Bohren & Hoffman data base
"""


from lambdalist import *
from E_gold import *

E = EgoldexperimentalData()


def epsilon(l2, metal):
    E_D_list = []
    for i in xrange(len(l2)):
        w = 2 * pi * ls / l2[i]
        gm2 = metal.gm + metal.vf / r_0
        E_D = E[i] + metal.w_p ** 2 / (w**2 + 1j * metal.gm * w) - metal.w_p ** 2 / (w**2 + 1j * gm2 * w)  # noguez
        E_D_list.append(E_D)
    return E_D_list

