#!/usr/bin/env python3

from HepLib import *

I = expr("I")

A = Symbol("A")
e = Symbol("e")
ebar = Symbol("ebar")
mu = Symbol("mu")
mubar = Symbol("mubar")

p = Vector("p")
P = Vector("P")
k = Vector("k")
K = Vector("K")

me = Symbol("me")
mm = Symbol("mm")

proc = Process()
proc.Model = """
    [e, ebar, -]
    [mu, mubar, -]
    [A, A, +]
    [ebar, e, A]
    [mubar, mu, A]
"""
proc.In = "e[p],ebar[P]"
proc.Out = "mubar[k],mu[K]"
proc.Options = "onshell"
proc.Loops = 0

st = {}
st["p"] = p
st["P"] = P
st["k"] = k
st["K"] = K

amps = proc.Amplitudes(st)

set_InOutTeX(-1,"$e^-(p)$")
set_InOutTeX(-3,"$e^+(P)$")
set_InOutTeX(-2,"$\\mu^+(k)$")
set_InOutTeX(-4,"$\\mu^-(K)$")

set_LineTeX(Symbol("e"),"fermion, edge label=$e$")
set_LineTeX(Symbol("ebar"),"anti fermion, edge label=$e$")
set_LineTeX(Symbol("mu"),"fermion, edge label=$\\mu$")
set_LineTeX(Symbol("mbar"),"anti fermion, edge label=$\\mu$")
set_LineTeX(Symbol("A"),"photon, edge label=$\\gamma$")

Process.DrawPDF(amps, "amps.pdf")

class ClassFR(MapFunction):
    def __init__(self):
        MapFunction.__init__(self)

    def map(self, e):
        if(isFunction(e,"OutField") or isFunction(e,"InField")):
            return expr(1)
        elif(isFunction(e, "Propagator")):
            fi1 = e.op(0).op(1)
            fi2 = e.op(1).op(1)
            mom = e.op(2)
            if(e.op(0).op(0)==A):
                return (-I) * SP(LI(fi1),LI(fi2)) / SP(mom); # Feynman Gauge
            elif(e.op(0).op(0)==ebar):
                return I * Matrix(GAS(mom)+GAS(1)*me, DI(fi1),DI(fi2)) / (SP(mom)-me*me)
            elif(e.op(0).op(0)==mubar):
                return I * Matrix(GAS(mom)+GAS(1)*mm, DI(fi1),DI(fi2)) / (SP(mom)-mm*mm)
        elif(isFunction(e, "Vertex")):
            fi1 = e.op(0).op(1)
            fi2 = e.op(1).op(1)
            fi3 = e.op(2).op(1)
            if(e.op(0).op(0)==ebar):
                return I*Symbol("e")*Matrix(GAS(LI(fi3)),DI(fi1),DI(fi2))
            elif(e.op(0).op(0)==mubar):
                return I*Symbol("e")*Matrix(GAS(LI(fi3)),DI(fi1),DI(fi2))
        else:
            return e.map(self)

print(LI(expr(1)))
amps_FR = ClassFR()(amps[0])
    
print("amps_FR: ")
print(amps_FR);
    
ampL = amps_FR
ampR = IndexL2R(conjugate(ampL));
def SS1(p,m,i):
    return Matrix(GAS(p)+m*GAS(1),DI(i),RDI(i))
def SS2(p,m,i):
    return Matrix(GAS(p)+m*GAS(1),RDI(i),DI(i))

M2 = ampL * ampR * SS1(p,me,-1) * SS2(P,-me,-3) * SS1(k,-mm,-2) * SS2(K,mm,-4);
M2 = MatrixContract(M2);
    
print("M2: ")
print(M2)
print()
    
set_form_using_dim4(True)
letSP(p,me*me)
letSP(P,me*me)
letSP(k,mm*mm)
letSP(K,mm*mm)

res = form(M2);
print("Final M2:")
print(factor(res.subs(me>>0)))
    
    


