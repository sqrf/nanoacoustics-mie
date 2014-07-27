
"""
File            drude.py
Author          Rafael Silva Quiroz
email           sqrf87@gmail.com

License	        educational use

Description     Calculates the dielectric function for metals based on Drude's model
Return          Dielectric function
Reference       Bohren & Hoffman data base
"""


from variables import *



def getDrude(l1, metal, radius):
    E_D_list = []
    for i in xrange(len(l1)):
        w = 2 * pi * ls / l1[i]
        gm2 = metal.gm + metal.vf / (2 * radius)
        E_D = metal.E_inf - metal.w_p ** 2 / (w * (w + gm2 * 1j))  # noguez
        E_D_list.append(E_D)
    return E_D_list

"""
def getDrudeLorentz(l1, metal, metalLorenz):
    E_DL_list = []
    #gm = 1 / metal.T
    for i in xrange(len(l1)):
        w = 2 * pi * ls / l1[i]
        E_DL = metal.E_inf - metal.w_p ** 2 / (w * (w + gm2 * 1j)) - (
            metalLorenz.deltaE * metalLorenz.omega_L ** 2) / (
                   (w ** 2 - metalLorenz.omega_L ** 2) + metalLorenz.gamma_L * w * 1j)
        E_DL_list.append(E_DL)
    return E_DL_list
    """