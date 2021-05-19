#!/usr/bin/env python3

from HepLib import *

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
proc.Loops = 1

st = {}
st["p"] = Vector("p")
st["P"] = Vector("P")
st["k"] = Vector("k")
st["K"] = Vector("K")

amps = proc.Amplitudes(st)
for item in amps:
    print(item)
    print()

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


    
    


