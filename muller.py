"""
File            zermuller.py
Author          Ernesto P. Adorio,Ph.D.
email           ernesto.adorio@gmail.com
                UPDEPP at Clark Field
                Pampanga, the Philippines
license	        educational use

Description     Zero finding using muller's method.
Return          array of roots found
Reference       Conte and DeBoor, pp.120-122.
Revisions       04.03.2009 first Python release based on old 1998 C++ code by
the translator
"""

from cmath import *



def zermuller(f, xinit, ztol=1.0e-5, ftol=1.0e-5, maxiter=1000, wantreal=False, nroots=1):
    nmaxiter = 0
    retflag = 0
    roots = []
    for j in range(nroots):
        #print "j=",  j
        x1 = xinit
        x0 = x1 - 1.0
        x2 = x1 + 1.0

        f0, undeflate = deflate(f, x0, j, roots)
        f1, undeflate = deflate(f, x1, j, roots)
        f2, undeflate = deflate(f, x2, j, roots)

        h21 = x2 - x1
        h10 = x1 - x0
        f21 = (f2 - f1) / h21
        f10 = (f1 - f0) / h10

        for i in range(maxiter):
            #print "iter", i
            f210 = (f21 - f10) / (h21 + h10)
            b = f21 + h21 * f210
            t = b * b - 4.0 * f2 * f210

            if (wantreal):        # force real roots ? #
                if (real(t) < 0.0):
                    t = 0.0
                else:
                    t = real(t)

            Q = sqrt(t)
            D = b + Q
            E = b - Q

            if (abs(D) < abs(E)):
                D = E

            if (abs(D) <= ztol):      # D is nearly zero ? #
                xm = 2 * x2 - x1
                hm = xm - x2
            else:
                hm = -2.0 * f2 / D
                xm = x2 + hm


            # compute deflated value of function at xm.  #
            fm, undeflate = deflate(f, xm, j, roots)


            # Divergence control #
            absfm = abs(fm)
            absf2 = 100. * abs(f2)
            # Note: Originally this was a while() block but it
            #	   causes eternal cycling for some polynomials.
            #	   Hence, adjustment is only done once in our version.
            if (absf2 > ztol and absfm >= absf2):
                hm = hm * 0.5
                xm = x2 + hm
                fm = f(xm)
                absfm = abs(fm)


            # function or root tolerance using original function
            if (abs(undeflate) <= ftol or abs(hm) <= ztol):
                if (i > nmaxiter):
                    nmaxiter = i
                    retflag = 0
                    break

            # Update the variables #
            x0 = x1
            x1 = x2
            x2 = xm

            f0 = f1
            f1 = f2
            f2 = fm

            h10 = h21
            h21 = hm
            f10 = f21
            f21 = (f2 - f1) / h21

        if (i > maxiter):
            nmaxiter = i
            retflag = 2
            break

        xinit = xm
        #print "a root is ", xinit
        roots.append(xinit)

        # initial estimate should be far enough from latest root.
        xinit = xinit + 0.85

    maxiter = nmaxiter
    return roots


def deflate(f, z, kroots, roots):
    """
    Arguments
      f				Input: complex<double> function whose root is desired
      z				Input: test root
      kroots		Input: number of roots found so far
      roots			Input/Output: saved array of roots

    Return value
      Deflated value of f at z.

    Description
      This routine is local to zermuller.
      Basically, it divides the complex<double> function f by the product
                (z - root[0]) ... (z - root[kroots - 1]).
      where root[0] is the first root, root[1] is the second root, ... etc.
    """
    undeflate = t = f(z)
    nroots = len(roots)
    for i in range(nroots):
        denom = z - roots[i]
        while (abs(denom) < 1e-8):# avoid division by a small number #
            denom += 1.0e-8
        t = t / denom
    return t, undeflate