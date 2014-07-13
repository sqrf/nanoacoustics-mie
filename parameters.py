
"""
File            parameters.py
Author          Rafael Silva Quiroz
email           sqrf87@gmail.com

License	        educational use

Description     Define the class Parametes as a function of kind of metal, kind of media, maximum time  and radius of nanoparticle
"""



class Parameters:
    def __init__(self, metal, medio, tmax, radius):
        self.metal = metal
        self.medio = medio
        self.tmax = tmax
        self.radius = radius