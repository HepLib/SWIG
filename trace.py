#!/usr/bin/env python3

# python version for trace.cpp

from HepLib import *

mu = Index("mu")
nu = Index("nu")
p1 = Vector("p1")
p2 = Vector("p2")
m = Symbol("m")
#note GAS(1) in gline, corresponds to the identity matrix
gline = GAS(p1)*GAS(mu)*(GAS(p2)+m*GAS(1))*GAS(mu)
trace = form(TR(gline))
co << trace << endl
