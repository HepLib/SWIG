#!/usr/bin/env python3

# python version for 3.cpp

from HepLib import *

x = Symbol("x")
y = Symbol("y");
e0 = expr("x^4+x^3+x^2+x")
co << "e0 -> " << e0 << endl
e1 = e0.subs([pow(x,w)>>pow(y,w+2)]);
co << "e1 -> " << e1 << endl

class mapClass(MapFunction):
    def map(self, e):
        if(e.match(pow(x,w)) and e.op(1).info("even")):
            return pow(y,e.op(1)+2)
        else:
            return e.map(self)

e2 = mapClass()(e0);
co << "e2 -> " << e2 << endl
