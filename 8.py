#!/usr/bin/env python3

# python version for 8.cpp

from HepLib import *

q1 = Symbol("q1")
p = Symbol("p")
m = Symbol("m")
    
fire = FIRE()
fire.Internal = exvec([ q1 ])
fire.External = exvec([ p ])
fire.Replacements = exvec([ p*p >> m*m ])

fire.Propagators = exvec([ q1*q1, 2*p*q1-q1*q1 ])
fire.Integrals = exvec([ expr("{2,1}") ])
fire.WorkingDir = "IBPdir";
fire.Reduce()

ho << "Reduced Rules:" << endl
ho << fire.Rules << endl << endl
ho << "Master Integrals:" << endl
ho << fire.MIntegrals << endl << endl

RunOS("rm -rf IBPdir")


