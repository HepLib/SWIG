#!/usr/bin/env python3

from HepLib import *

p1 = Vector("p1")
p2 = Vector("p2")
p3 = Vector("p3")

q1 = Vector("q1")
q2 = Vector("q2")
q3 = Vector("q3")

i1 = Index("i1")
i2 = Index("i2")
i3 = Index("i3")

ei = SP(q1,i1) * SP(q2,i2)
res = TIR(ei, [q1,q2], [p1,p2])
print(res)

c1 = (ei- res) * SP(p1,i1) * SP(p1,i2)
print(form(c1).normal())
c2 = (ei- res) * SP(p2,i1) * SP(p2,i2)
print(form(c2).normal())

