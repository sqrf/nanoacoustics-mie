
"""
File            radialdispl.py
Author          Rafael Silva Quiroz
email           sqrf87@gmail.com

License	        educational use

Description    Calculates the radial displacement u in the interval of time given
"""


from variables import *
from muller import *


ulist = []


def getu(metal, med, vibration, radius):
    c_tp = metal.c_tp
    c_lp = metal.c_lp
    c_tm = med.c_tm
    c_lm = med.c_lm
    rho_m = med.rho_m
    rho_p = metal.rho_p
    alpha = float(c_lm) / float(c_lp)
    beta = float(c_tm) / float(c_tp)
    gama = float(c_tm) / float(c_lm)
    eta = float(rho_m) / float(rho_p)
    r_0 = radius

    def f(s):
        den = 4*(float(alpha * gama)/float(beta))**2 * (1 - eta * beta**2) + s**2*(eta + 1j * s * (float(eta)/float(alpha)))/(1+s**2/float(alpha)**2)
        ##den = 4*(float(c_tp)/float(c_lp))**2 + s**2*(eta + 1j * s * (float(eta)/float(alpha)))/(1+s**2/float(alpha)**2)
        return s / tan(s) - 1 + s**2 / den
    xinit = 2
    ztol  = 1.0e-5
    ftol  = 1.0e-5
    maxiter = 100
    wantreal = False
    nroots = 1

    raiz = zermuller(f, xinit, ztol, ftol, maxiter, wantreal, nroots)
    raiz_0 = raiz[0]

    w = (metal.c_lp / radius) * raiz_0
    for i in xrange(len(vibration.t)):
        u = -exp(-1j * w * vibration.t[i]) * (cos(raiz_0) / raiz_0 - sin(raiz_0) / raiz_0**2) * raiz_0.imag / r_0#* metal.c_lp / w
        uimag = u.imag
        ureal = u.real
        ulist.append(uimag)
    print 'w.imag = freq vib: (THz)', -w.imag/1000    #* 1e9 / 1e12
    print 'w.real = (THz)', w.real/1000
    print 'w=', w / 1000
    print '|w|=', abs(w/1000)
    print 'tD(ps)=', 1 / (-w.imag/1000)
    print 'alpha(ThZ) =', -w.imag/1000
    print 'raiz0:', raiz_0
    #print 'ulist', ulist
    return ulist




