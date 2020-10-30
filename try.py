#!/usr/bin/env python3

from HepLib import *


ia = Index("ia");
ib = Index("ib");

p1 = Vector("p1");
p2 = Vector("p2");

a = Symbol("a");
b = Symbol("b");
c = Symbol("c");

res = TR(GAS(ia)*GAS(ib)*GAS(a*p1+b*p2)*GAS(ia)*GAS(ib)*GAS(p1));

res = form(res);
print(res);

print(res.factor())

print(res.subs(pow(w(1),2)==expr(13)))

print(subs(res,pow(w(1),2)==expr(13)))

print(call("sin",a))

try:
    print(series(res,a+b,0))
except:
    print("Expected Error.");
    
series(res,a+b,0)

class replClass(MapFunction):
    def __init__(self):
        MapFunction.__init__(self)

    def map(self, e):
        if(e.match(SP(p1,p2))):
            return b
        else:
            return e.map(self)
        
print(replClass()(SP(p1,p2)+a))

    
    


