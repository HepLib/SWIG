#!/usr/bin/env python3

# python version for wr.cpp

from HepLib import *

xint = XIntegrand()
    
wra = WRA(Pi/5)

xint.Functions = exvec(expr("{1,-4*x(4)*x(4)-12*x(1)*x(4)+x(1)*x(2),x(1),x(2)}"))
xint.Exponents = exvec(expr("{1,1/(2)-2*ep,3*ep-5/(2),ep-3/(2)}"))
xint.Deltas = exvec(expr("{{x(1),x(2),x(4)}}"))
    
xint.Functions.subs([ x(4)>>x(4)*exp(I*wra) ]);
xint.Functions[0] = exp(I*wra);

work = SecDec()
work.epN = 1
set_Verbose(100)
    
work.Initialize(xint)
work.RemoveDeltas()
work.SDPrepares()
work.EpsEpExpands()
work.CIPrepares()

work.EpsAbs = expr("1E-5");
work.RunPTS = 1000000;
work.RunMAX = 5;

work.Integrates()

co << work.VE << endl
