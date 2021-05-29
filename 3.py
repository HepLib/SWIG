#!/usr/bin/env python3

# python version for 0.cpp

from HepLib import *

x = Symbol("x")
y = Symbol("y");
e0 = expr("x^4+x^3+x^2+x")
print("e0 ->", e0)
e1 = e0.subs([pow(x,w())>>pow(y,w()+2)]);
print("e1 ->",e1)

class mapClass(MapFunction):
    def map(self, e):
        if(e.match(pow(x,w())) and e.op(1).info("even")):
            return pow(y,e.op(1)+2)
        else:
            return e.map(self)

e2 = mapClass()(e0);
print("e2 ->",e2)

print()
