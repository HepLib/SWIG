#!/usr/bin/env python3

# python version for 0.cpp

from HepLib import *

x = Symbol("x")
y = Symbol("y")
z = Symbol("z")
n = Symbol("n")
l1 = lst([x, y, x+z])
e1 = pow(sin(x),n)
print("l1 ->", l1)
print("e1 ->", e1)
tot = l1.nops()
print("l1.nops() ->", tot)
item1 = l1.op(0)
print("1st item of l1 ->", item1)
l1.let_op(2, e1)
print("updated l1 ->", l1)
tot = e1.nops()
print("e1.nops() ->", tot)
item2 = e1.op(1)
print("2nd item of e1 ->", item2)


print()
