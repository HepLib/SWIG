#!/usr/bin/env python3

from HepLib import *

t = expr("vs")
k = Symbol("k")
p1 = Symbol("p1")
p2 = Symbol("p2")
p3 = Symbol("p3")
p4 = Symbol("p4")
p5 = Symbol("p5")
m = Symbol("m")
s = Symbol("s")

fp = FeynmanParameter()
    
fp.LoopMomenta = exvec([ k ])
fp.Propagators = exvec([ -pow(k,2),-pow(k + p1,2),-pow(k + p1 + p2,2),-pow(k + p1 + p2 + p4,2) ])
fp.Exponents = exvec(expr("{1, 1, 1, 1}"))
fp.lReplacements[p1*p1] = expr(0)
fp.lReplacements[p2*p2] = expr(0)
fp.lReplacements[p4*p4] = expr(0)
fp.lReplacements[p1*p2] = -s/2
fp.lReplacements[p2*p4] = -t/2
fp.lReplacements[p1*p4] = (s+t)/2
fp.lReplacements[s] = expr(1)
fp.Prefactor = pow(I*pow(Pi,2-ep)*exp(-ep*Euler), -1)
        
work = SecDec()
work.epN = 0
work.vsN = 0
set_Verbose(100)
        
work.Evaluate(fp);

print(work.VE)
print()
