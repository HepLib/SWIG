#!/usr/bin/env python3

from HepLib import *

p = Vector("p")
P = Vector("P")
st = {}
st["p"] = p
st["P"] = P
e1 = expr("p+P", st)
print(e1)
print(form(LC(e1,e1,e1,e1)))

dict = {}
dict[p] = p
dict[2*p-p] = 0

print(dict)

