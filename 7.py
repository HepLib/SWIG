#!/usr/bin/env python3

from HepLib import *

p = Vector("p")
q1 = Vector("q1")
expr = expr(1)/SP(q1) * expr(1)/(2*SP(p,q1)-SP(q1)) * expr(1)/(2*SP(p,q1)+SP(q1))
r = Apart(expr,[q1],[p]);
r1 = ApartIR2ex(r);
r2 = ApartIR2F(r);

print(r)
print()
print(r1)
print()
print(r2)
print()
    
r3 = Apart(expr, [SP(q1),SP(p,q1)])
print(r3)
print()


