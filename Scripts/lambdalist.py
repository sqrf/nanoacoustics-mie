
"""
File            lambdalist.py
Author          Rafael Silva Quiroz
email           sqrf87@gmail.com

License	        educational use

Description     List of wavelengths used in Epsilon.py for calculate the corrected dielectric function
Return          Wavelengths
Reference       Bohren & Hoffman data base
"""



from variables import *
from energies import *

lambdalist = []

for i in xrange(len(energies)):
    lambdas = float(h * ls) / energies[i]
    lambdalist.append(lambdas)
l2 = lambdalist