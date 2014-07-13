
"""
File            simulation_mie.py
Author          Rafael Silva Quiroz
email           sqrf87@gmail.com

License	        educational use

Description     Using the modules bhmie, drude and metals this  module  generates with Mie theory the wavelength dependet
                optical trasmission T showing the maximum value in the wavelength of resonance.
"""

from bhmie import bhmie
from drude import *
from metals import *




class Mdq:
    def __init__(self, parameters):
        self.parameteres = parameters
        self.metal = parameters.metal
        self.medio = parameters.medio
        self.r_0 = parameters.radius
        self.max_lambda = 0.0
        self.energyoflambda = 0.0
        self.max_E = 0.0
        self.max_T = 0.0
        self.l = []
        self.Q_scalist_sim = []
        

    def runmdq(self):
    
        resolution = float(self.metal.lmax)/self.metal.N          # Gives the number of points to plot
        self.l = arange(self.metal.lmin, self.metal.lmax, resolution)  # Generate an array of numbers between lmin and lmax with resolution
                                                        # increasing
        l1 = list(self.l)                                    # Converts the l-array into a list
    
        Q_scalist_sim = []
        xlist = []
    
    
        E_simulation_DL = getDrude(l1, self.metal, self.r_0)
        #E_simulation_DL = getDrudeLorentz(l1, self.metal, self.metalLorenz)
    
        for i in xrange(len(l1)):
            x = 2 * pi * self.r_0 * sqrt(self.medio.Emedio)/l1[i]     # Size parameter
            ################
            # Mie theory. Here the bhmie function is used
            s1, s2, qext, qsca, qback, gsca = bhmie(x, sqrt(E_simulation_DL[i]), self.metal.nang)
            Qsca = qsca
            self.Q_scalist_sim.append(Qsca)
    
            ####################
            #########
            xlist.append(x)
        gm_correction = self.metal.gm + self.metal.vf / self.r_0
        ######
        self.max_T = max(self.Q_scalist_sim)  # Find the maximum y value
        self.max_lambda = self.l[self.Q_scalist_sim.index(self.max_T)]
        self.max_E = E_simulation_DL[self.Q_scalist_sim.index(self.max_T)]
        self.energyoflambda = float(h * ls / self.max_lambda)

        f = open("list_lambdas_mdq", "w")
        #ylist = (Qlist - max_T)/max_T
        f.write("\n".join(map(lambda x: str(x), self.l)))
        f.close()
        ##
        f = open("list_T_mdq", "w")
        #ylist = (Qlist - mdq.max_T)/mdq.max_T
        f.write("\n".join(map(lambda x: str(x), self.Q_scalist_sim)))
        f.close()
        #return 200
    
    def plot(self):
        print 'Max_lambda =', self.max_lambda       #metal.gm, gm_correction, #   #
        print 'Energy =', self.energyoflambda
        print 'epsilon(maxQ) =', self.max_E
        print 'Tmax=', self.max_T
        #######################################
        plot(self.l, self.Q_scalist_sim, 'g-', label='mie')
        title('Simulation of light transmission $ T \ $' + 'for a ' + str(self.r_0) + ' nm ' + self.metal.name  + ' Nanoparticle on ' + self.medio.name)
        xlabel('$\lambda$ (nm)')
        ylabel('T')
        xlim(self.max_lambda-100, self.max_lambda+100)
        grid()
        #legend()
        #savefig('Al-T-14nm.png')
        show()
        #return 300
        ##############################################
