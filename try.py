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
    
class replClass(MapFunction):
    def __init__(self):
        MapFunction.__init__(self)

    def map(self, e):
        if(e.match(SP(p1,p2))):
            return b
        else:
            return e.map(self)
        
print(replClass()(SP(p1,p2)+a))

x1 = x(1);
x2 = x(2);
ep=expr("ep");

xint = Integral();
xint.Functions([x(1)+x(2)]);
xint.Exponents([-2+ep]);
xint.verb = 0;
xint.Evaluate();
print(xint)

q1 = Symbol("q1")
p1 = Symbol("p1")
p2 = Symbol("p2")

int = Integral();
int.Exponents([expr(1),expr(1),1+ep])
int.Propagators([pow(q1,2),pow(q1+p1,2),pow(q1+p1+p2,2)],[q1])
int.Replacements([pow(p1,2)==expr(1),pow(p2,2)==expr(1),p1*p2==-expr(13)])
int.verb = 100;
int.Evaluate()
print(int)



    
    


