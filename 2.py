#!/usr/bin/env python3

# python version for 2.cpp

from HepLib import *

x = Symbol("x")
y = Symbol("y")
z = Symbol("z")
n = Symbol("n")
l1 = lst([x, y, x+z])
e1 = pow(sin(x),n)
co << "l1 -> " << l1 << endl
co << "e1 -> " << e1 << endl
tot = l1.nops()
co << "l1.nops() -> " << tot << endl
item1 = l1.op(0)
co << "1st item of l1 -> " << item1 << endl
l1.let_op(2, e1)
co << "updated l1 -> " << l1 << endl
tot = e1.nops()
co << "e1.nops() -> " << tot << endl
item2 = e1.op(1)
co << "2nd item of e1 -> " << item2 << endl

