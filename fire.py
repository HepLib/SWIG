#!/usr/bin/env python3

from HepLib import *

q1 = Symbol("q1")
p = Symbol("p")
k = Symbol("k")
m = Symbol("m")
s = Symbol("s")

fire = FIRE();
fire.Internal = exvec([q1])

fire.External = exvec([p])
fire.Replacements = exvec([ p*p >> m*m ])

fire.Propagators = exvec([q1*q1, q1*p-1])
fire.Integrals = exvec(expr("{{1,1},{2,2},{2,3}}"))
fire.WorkingDir = "IBPdir"
FIRE.Version = 6


fire.Reduce()

print("Rules:");
print(fire.Rules);
print("Master Integrals:");
print(fire.MIntegrals);

