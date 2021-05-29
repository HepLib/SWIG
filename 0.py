#!/usr/bin/env python3

# python version for 0.cpp

from HepLib import *

x = symbol("x")
y = symbol("y")
z = symbol("z")
r = expr("2/3")
print("x ->", x, ", r ->", r)

e1 = r*x+2*y+pow(y,10)
print("e1 ->", e1)
e2 = (x+1)/(x-1)
print("e2 ->", e2)
e3 = sin(x+2*y)+3*z+41
print("e3 ->", e3)
e4 = e3+e2/exp(e1)
print("e4 ->", e4)

print()

x = symbol("x")
y = Symbol("y")
print("x ->", x, ", y->", y)
e1 = conjugate(x);
print("conjugate(x) ->", e1)
e2 = conjugate(y)
print("conjugate(y) ->", e2)

print()
