
"""
File            n-atomos.py
Author          Rafael Silva Quiroz
email           sqrf87@gmail.com

License	        educational use

Description     Calculates the number of atoms for nanoparticles in several radii
"""


from metals import*

metales = Conductors()
metal_Pt = metales.Pt
metal_Au = metales.Au
metal_Al = metales.Al
metal_Ag = metales.Ag
metal_Cu = metales.Cu

#metal(lmin, lmax, w_P, T, E_inf, N, nang, c_lp, c_tp,  rho_p, vf,  aweigth):
atomslist_Pt = []
atomslist_Au = []
atomslist_Al = []
atomslist_Ag = []
atomslist_Cu = []


radii = [0, 0.5, 1, 1.5, 2, 2.5, 3]  #nm

for i in range(len(radii)):
    V = 4/3 * pi * (radii[i] * 1e-7)**3
    rho = metal_Pt.rho_p / 1e3
    m = V * rho
    numberofmoles_Pt = m / metal_Pt.aweigth
    numberatoms_Pt = numberofmoles_Pt * A
    atomslist_Pt.append(numberatoms_Pt)
    ##
    numberofmoles_Au = m / metal_Au.aweigth
    numberatoms_Au = numberofmoles_Au * A
    atomslist_Au.append(numberatoms_Au)
    ##
    numberofmoles_Al = m / metal_Al.aweigth
    numberatoms_Al = numberofmoles_Al * A
    atomslist_Al.append(numberatoms_Al)
    ##
    numberofmoles_Ag = m / metal_Ag.aweigth
    numberatoms_Ag = numberofmoles_Ag * A
    atomslist_Ag.append(numberatoms_Ag)
    ##
    numberofmoles_Cu = m / metal_Cu.aweigth
    numberatoms_Cu = numberofmoles_Cu * A
    atomslist_Cu.append(numberatoms_Cu)
    """
    f = open("radii", "w")
        #ylist = (Qlist - max_T)/max_T
    f.write("\n".join(map(lambda x: str(x), radii)))
    f.close()
        ##
    f = open("atomlist_Pt", "w")
    #ylist = (Qlist - mdq.max_T)/mdq.max_T
    f.write("\n".join(map(lambda x: str(x), atomslist_Pt)))
    f.close()

    f = open("atomlist_Au", "w")
    #ylist = (Qlist - mdq.max_T)/mdq.max_T
    f.write("\n".join(map(lambda x: str(x), atomslist_Au)))
    f.close()

    f = open("atomlist_Ag", "w")
    #ylist = (Qlist - mdq.max_T)/mdq.max_T
    f.write("\n".join(map(lambda x: str(x), atomslist_Ag)))
    f.close()

    f = open("atomlist_Cu", "w")
    #ylist = (Qlist - mdq.max_T)/mdq.max_T
    f.write("\n".join(map(lambda x: str(x), atomslist_Cu)))
    f.close()

    f = open("atomlist_Al", "w")
    #ylist = (Qlist - mdq.max_T)/mdq.max_T
    f.write("\n".join(map(lambda x: str(x), atomslist_Al)))
    f.close()"""




plot(radii, atomslist_Pt, 'bs--', label='Pt')
plot(radii, atomslist_Au, 'gs--', label='Au')
plot(radii, atomslist_Al, 'rs--', label='Al')
plot(radii, atomslist_Ag, 'ys--', label='Ag')
plot(radii, atomslist_Cu, 'cs--', label='Cu')
title('Number of atoms N as function of radius ')
xlabel('Radius')
ylabel('N(r)')
#ylim([0, 2500])
grid()
legend(loc=2)
show()