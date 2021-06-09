#!/usr/bin/env python3

import os
from HepLib import *

k = Symbol("k")
r = Symbol("r")
q = Symbol("q")
p1 = Symbol("p1")
p2 = Symbol("p2")
s = Symbol("s")

fp = FeynmanParameter()
fp.LoopMomenta = exvec([k,r,q]);
fp.Propagators= exvec([ -pow(k,2),-pow(k+p1+p2,2),-pow(-k+r,2),-pow(p1+r,2),-pow(k-q,2),-pow(p1+q,2) ]);
fp.Exponents = exvec(expr("{1+3*ep,1,1,1,1,1}"))
fp.lReplacements[p1*p1] = expr(0)
fp.lReplacements[p2*p2] = expr(0)
fp.lReplacements[p2*p1] = s/2
fp.lReplacements[s] = expr(-1)
fp.Prefactor = pow(I*pow(Pi,2-ep),-3) * pow(tgamma(1-ep),3)
work = SecDec()
set_Verbose(100)
work.Evaluate(fp)
print("Final Result & Error:")
print(work.VE)

