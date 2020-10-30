#!/usr/bin/env python3

from HepLib import *

x = Symbol("x")
y = Symbol("y")

class mapClass(MapFunction):
    def __init__(self):
        MapFunction.__init__(self)

    def map(self, e):
        if(e.match(pow(x,w(0))) and e.op(1).info("even")):
            return pow(y,e.op(1)+2)
        else:
            return e.map(self)
            
expr1 = expr("x^4+x^3+x^2+x")

print(expr1)

print(mapClass()(expr1))

    
    


