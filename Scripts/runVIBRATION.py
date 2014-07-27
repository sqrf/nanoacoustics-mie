__author__ = 'sqrf'
from tsimulation import *
from metals import *
from parameters import *

##Paramteres(metal, medium, tmax, radius)

metals = Conductors()
medios = Media()
param = Parameters(metals.Pt, medios.glass, 0.01, 0.75)

tsim = Tsimulation(param)
tsim.run()
