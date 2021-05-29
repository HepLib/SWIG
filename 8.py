#!/usr/bin/env python3

import os
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

print("Reduced Rules:")
print(fire.Rules)
print("Master Integrals:")
print(fire.MIntegrals)

os.system("rm -rf IBPdir")


