#!/usr/bin/env python3

# python version for 7.cpp

from HepLib import *

p = Vector("p")
q1 = Vector("q1")
expr = expr(1)/SP(q1) * expr(1)/(2*SP(p,q1)-SP(q1)) * expr(1)/(2*SP(p,q1)+SP(q1))
r = Apart(expr,[q1],[p]);
r1 = ApartIR2ex(r);
r2 = ApartIR2F(r);

co << r << endl << endl
co << r1 << endl << endl
co << r2 << endl << endl
    
r3 = Apart(expr, [SP(q1),SP(p,q1)])
co << r3 << endl


