#!/usr/bin/env python3

# python version for 0.cpp

from HepLib import *

me = Symbol("me")
mm = Symbol("mm")
e = Symbol("e")
mu = Index("mu")
nu = Index("nu");
p = Vector("p")
P = Vector("P")
k = Vector("k")
K = Vector("K")
q = Vector("q")

letSP(p,me*me)
letSP(P,me*me)
letSP(k,mm*mm)
letSP(K,mm*mm)

def gpm(p, m):
    return GAS(p)+m*GAS(1)

tr1 = TR( gpm(P,-me)*GAS(mu)*gpm(p,me)*GAS(nu) );
tr2 = TR( gpm(k,mm)*GAS(mu)*gpm(K,-mm)*GAS(nu) );
res =  pow(e,4) / (4*pow(SP(q),2)) * tr1 * tr2;
set_form_using_dim4(True)
res = form(res)
res = factor(res);
print(res.subs(me>>0));
print()

set_form_using_su3(True)
a = IndexCA("a")
i = IndexCF("i")
j = IndexCF("j");
tr = TTR([a,a]);
print("tr1 =", form(tr))
tr = SUNT(a,i,j) * SUNT(a,j,i);
print("tr2 =", form(tr))
tr = SUNT([a,a],i,i)
print("tr3 =", form(tr))

print()
