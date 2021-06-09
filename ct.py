#!/usr/bin/env python3

# python version for ct.cpp

from HepLib import *

xint = XIntegrand()

xint.Functions = exvec([ expr(1),-4*x(4)*x(4)-12*x(1)*x(4)+x(1)*x(2),x(1),x(2) ])
xint.Exponents = exvec([ expr(1),expr(1)/expr(2)-2*ep,3*ep-expr(5)/expr(2),ep-expr(3)/expr(2) ])
xint.Deltas = exvec(expr("{{x(1),x(2),x(4)}}"))

work = SecDec()
work.epN = 1
set_Verbose(100)

work.Initialize(xint)
work.RemoveDeltas()
work.SDPrepares()
work.EpsEpExpands()
work.CIPrepares()
work.Contours()

work.EpsAbs = expr("1E-5");
work.RunPTS = 1000000;
work.RunMAX = 5;

work.Integrates()

print(work.VE)
print()
  
