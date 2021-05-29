#!/usr/bin/env python3

# python version for 0.cpp

from HepLib import *

expr_str = "WF(1)+x(1)^2+sin(5)+power(a,n)"
e1 = expr(expr_str);
print(e1);
a = Symbol("a")
n = Symbol("n");
e2 = WF(expr(1))+pow(x(1),2)+sin(expr(5))+pow(a,n)
print(e1-e2)

print()
