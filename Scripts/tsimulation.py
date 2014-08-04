

"""
File            tsimulation.py
Author          Rafael Silva Quiroz
email           sqrf87@gmail.com

License	        educational use

Description     Using the maximum value of optical trasmission T generates the time dependent optical trasmission plot.
                This plot is associated with the vibration of the nanoparticle. In this plot one can estimate the eigenfrequency.
"""


from radialdispl import getu
from simulation_mie import *


class Tsimulation:
    def __init__(self, parameters):
        self.param = parameters

    def run(self):

        metal = self.param.metal
        medio = self.param.medio
        r_0 = self.param.radius

        mdq = Mdq(self.param)
        mdq.runmdq()
        mdq.plot()

        Q_scalist = []
        Q_extlist = []


        vibration = Vibration(self.param.tmax)
        radius = getu(metal, medio, vibration, r_0)

        radlist = []
        volist = []
        densitylist = []
        monitor_radvib = []

        E_simulation_DL = mdq.max_E   #getDrude(l1, metal)


        for i in xrange(len(radius)):
            radvib = r_0 + radius[i]
            x = 2 * pi * radvib * sqrt(medio.Emedio)/mdq.max_lambda    ##   # Size parameter
            ################
            # Mie theory. Here the bhmie function is used
            s1, s2, qext, qsca, qback, gsca = bhmie(x, sqrt(E_simulation_DL), metal.nang)
            Qsca = qsca
            Qext= qext
            Q_scalist.append(Qsca)
            Q_extlist.append(Qext)
            #####provisional
            vol = 1.33 * pi * radvib**3
            radlist.append(radvib)
            volist.append(vol)
            ## temporal
            m0 = metal.rho_p * volist[0]
            densidad = m0 / vol
            densitylist.append(densidad)
            monitor_radvib.append(radvib)


            ####################
           ###############maybe not needed
        A = pi * r_0 ** 2
        k_thermal = 70e-9  # W/nm*K
        C_abs = (Q_extlist[0] - Q_scalist[0]) * A
        I = 1.8e-9  # W/nm^2
        #Q_H = (C_abs * I) / (4 * pi )
        DT = (C_abs * I) / (4 * pi * k_thermal * r_0)
        alpha_V = 27e-6 # 1/K
        R = r_0 * (1 + alpha_V * DT)**(1/3)
        B = R - r_0
        #######################


        print '*************************'
        print 'u(t) =', radius[0], ' nm ----- radial displacement in t=0 '
        print 'R + u(t) =', monitor_radvib[0], ' nm ----- Time-dependent radius in t=0'


        Qlist = Q_scalist
        tlist = vibration.t

        ############################saving list

        filename = 'time'
        path_to_file = pjoin("./output/", filename)
        f = open(path_to_file, "w")
        f.write("\n".join(map(lambda x: str(x), tlist)))
        f.close()
        ##
        filename = 'T(time)'
        path_to_file = pjoin("./output/", filename)
        f = open(path_to_file, "w")
        ylist = (Qlist - mdq.max_T)/mdq.max_T
        f.write("\n".join(map(lambda x: str(x), ylist)))
        f.close()



        #######################################
        plot(1000*tlist, (Qlist - mdq.max_T )/mdq.max_T, 'r-', label='mie')
        title('Simulation of time dependent $\Delta T/T$ ' + ' for a ' + str(r_0) + ' nm ' + self.param.metal.name + ' nanoparticle on ' + self.param.medio.name)
        xlabel('t(ps)')
        ylabel('$\Delta T/T$')
        grid()
        filename = "T(time) 'plot' "
        path_to_file = pjoin("./output/", filename)
        savefig(path_to_file, format="png")
        show()
        ######

       # plot(1e3 * vibration.t, radlist)
        #title('Vibration of radius')
        #xlabel('t')
        #ylabel('R(t)')
        #show()

        ##############################################
        #plot(1e3*vibration.t, densitylist)
        #title('Density')
        #xlabel('t')
        #ylabel('rho(t')
        #show()



