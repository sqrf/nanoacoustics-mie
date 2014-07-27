
"""
File            mie2.py
Author          Rafael Silva Quiroz
email           sqrf87@gmail.com

License	        educational use

Description     Generates the values oF wavelength dependent optical transmission with the correction of dielectric function


"""

from bhmie import bhmie
from Epsilon import *
from metals import *
from lambdalist import l2
from drude import *


metales = Conductors()
medios = Media()
metal = metales.Au
med = medios.glass



Q_scalist_sim = []
xlist = []
Q_sca_d_list = []
Q_sca_q_list = []
################
E_list = [] ####prov
E_list_correction = []
E_drude = getDrude(l2, metal, r_0)
E_simulation_DL = epsilon(l2, metal)


for i in xrange(len(l2)):
    x = 2 * pi * r_0 * sqrt(med.Emedio)/l2[i]     # Size parameter
    ################
    # Mie theory. Here the bhmie function is used
    s1, s2, qext, qsca, qback, gsca = bhmie(x, sqrt(E_simulation_DL[i]), metal.nang)
    Qsca = qsca
    Q_scalist_sim.append(Qsca)

    xlist.append(x)
    Er = E_drude[i].real
    Er_correction = E_simulation_DL[i].real
    E_list.append(Er)
    E_list_correction.append(Er_correction)
gm_correction = metal.gm + metal.vf / r_0
######
max_T = max(Q_scalist_sim[10:220])  # Find the maximum y value
max_lambda = l2[Q_scalist_sim.index(max_T)]
max_E = E_simulation_DL[Q_scalist_sim.index(max_T)]
energyoflambda = float(h * ls / max_lambda)

print 'maxT= ', max_T
print 'Max_lambda =', max_lambda, metal.gm, gm_correction #   #
print 'Energy =', energyoflambda
print 'epsilon(maxQ) =', max_E
print l2

#######################################

f = open("list_l2", "w")
     #ylist = (Qlist - max_T)/max_T
f.write("\n".join(map(lambda x: str(x), l2)))
f.close()
        ##
f = open("list_T_correcion", "w")
        #ylist = (Qlist - mdq.max_T)/mdq.max_T
f.write("\n".join(map(lambda x: str(x), Q_scalist_sim)))
f.close()

plot(l2, Q_scalist_sim, 'g-', label='mie')
title('Simulation of T for a  nanoparticle   ')
xlabel('$\lambda$')
ylabel('T')
xlim(450, 600)#(max_lambda-150, max_lambda+150)
ylim(0, 2 * max_T)
grid()
legend()
show()
##############################################
plot(l2, E_list, label='drude')
plot(l2, E_list_correction, label='correction')
title('Dielectric function')
grid()
legend()
show()
