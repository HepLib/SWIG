#!/usr/bin/env python3

from HepLib import *

x = Symbol("x")
y = Symbol("y")
z = Symbol("z")

a = Symbol("a")
b = Symbol("b")
c = Symbol("c")

e = x*(x+y+a)*(x+y+b)
e = expr(1)/e

res = Apart(e, [x,y,z])

print(ApartIR2ex(res))

