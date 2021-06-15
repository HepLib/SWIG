#!/usr/bin/env python3

# python version for 0.cpp

from HepLib import *

x = symbol("x")
y = symbol("y")
z = symbol("z")
r = expr("2/3")
co << "x -> " <<  x << ", r -> " << r << endl

e1 = r*x+2*y+pow(y,10)
co << "e1 -> " << e1 << endl
e2 = (x+1)/(x-1)
co << "e2 -> " << e2 << endl
e3 = sin(x+2*y)+3*z+41
co << "e3 -> " << e3 << endl
e4 = e3+e2/exp(e1)
co << "e4 -> " << e4 << endl

print()

x = symbol("x")
y = Symbol("y")
co << "x -> " << x << ", y-> " << y << endl
e1 = conjugate(x);
co << "conjugate(x) -> " << e1 << endl
e2 = conjugate(y)
co << "conjugate(y) -> " << e2 << endl

