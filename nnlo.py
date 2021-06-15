#!/usr/bin/env python3

# python version for nnlo.cpp

from HepLib import *

model = """
[ model = 'eqcd Model' ]
%------------------------------------
% Propagators
%------------------------------------
[q, qbar, -]
[Q, Qbar, -]
[gh, ghbar, -]
[g, g, +, notadpole]
[A, A, +, external]
%------------------------------------
% Vertices
%------------------------------------
[qbar, q, g; QCD='+1']
[Qbar, Q, g; QCD='+1']
[g, g, g, g; QCD='+2']
[g, g, g; QCD='+1']
[ghbar, gh, g; QCD='+1']
[qbar, q, A; QCD='+0']
[Qbar, Q, A; QCD='+0']
"""

# ----------------------

def Amps():
    
    A = Symbol("A")
    Q = Symbol("Q")
    Qbar = Symbol("Qbar")
    q = Symbol("q")
    qbar = Symbol("qbar")
    g = Symbol("g")
    gh = Symbol("gh")
    ghbar = Symbol("ghbar");
    
    proc = Process()
    proc.Model = model
    proc.In = "Q[p1],Qbar[p2]"
    proc.Out = "A[pA]"
    proc.Options = "onshell"
    proc.LoopPrefix = "q"
    
    st = { }
    st["pA"] = p1+p2
    st["p1"] = p1
    st["p2"] = p2
    st["q1"] = q1
    st["q2"] = q2
    
    proc.Loops = 0
    amp0 = proc.Amplitudes(st)
    proc.Loops = 1
    amp1 = proc.Amplitudes(st)
    proc.Loops = 2
    amp2 = proc.Amplitudes(st)
    
    chk = exvec(expr("{-1,-3,g}"))
    chk.sort()
    
    def filter(ampi):
        ret = exvec()
        for amp in ampi:
            cps = ShrinkCut(amp, exvec([g, g]), 1)
            ok = False
            for cpi in cps:
                if ok:
                    break
                for cpii0 in cpi:
                    cpii = exvec(cpii0)
                    cpii.sort()
                    if cpii==chk:
                        ok = True
                        break
            if not ok:
                ret.push_back(amp)
        return ret
        
    amps = [ amp0, amp1, amp2 ]
    ho << "Process Filter: [ "
    for amp in amps:
        ho << amp.size() << " "
    ho << "] :> [ "

    amp0 = filter(amp0);
    amp1 = filter(amp1);
    amp2 = filter(amp2);
    
    for amp in amps:
        ho << amp.size() << " "
    ho << "]" << endl

    if False:
        set_LineTeX(A, "photon")
        set_InOutTeX(-1, "$Q$")
        set_InOutTeX(-3, "$\\bar{Q}$")
        set_InOutTeX(-2, "$\\gamma^*$")
        Process.DrawPDF(amp0, "amp0.pdf")
        Process.DrawPDF(amp1, "amp1.pdf")
        Process.DrawPDF(amp2, "amp2.pdf")

    # feynman rules here
    class FeynRules(MapFunction):
    
        def map(self, e):
            if isFunction(e,"OutField") or isFunction(e,"InField"):
                return expr(1)
            elif(isFunction(e, "Propagator")):
                if e.op(0).op(0)==q:
                    return QuarkPropagator(e)
                elif(e.op(0).op(0)==Q):
                    return QuarkPropagator(e, m)
                elif(e.op(0).op(0)==g):
                    return GluonPropagator(e)
                elif(e.op(0).op(0)==gh):
                    return GhostPropagator(e)
            elif(isFunction(e, "Vertex")):
                if(e.nops()==3 and e.op(0).op(0)==ghbar and e.op(1).op(0)==gh):
                    #ghbar-gh-g
                    return gh2gVertex(e)
                elif(e.nops()==3 and e.op(0).op(0)==g and e.op(1).op(0)==g and e.op(2).op(0)==g):
                    #g^3
                    return g3Vertex(e)
                elif(e.nops()==4 and e.op(0).op(0)==g and e.op(1).op(0)==g and e.op(2).op(0)==g and e.op(3).op(0)==g):
                    #g^4
                    return g4Vertex(e)
                elif(e.nops()==3 and ((e.op(0).op(0)==qbar and e.op(1).op(0)==q) or (e.op(0).op(0)==Qbar and e.op(1).op(0)==Q)) ):
                    # qbar-q-g or Qbar-Q-g or g -> e
                    if(e.op(2).op(0)==g):
                        return q2gVertex(e);
                    else:
                        fi1 = e.op(0).op(1)
                        fi2 = e.op(1).op(1)
                        fi3 = e.op(2).op(1)
                        return Matrix(GAS(LI(fi3)),DI(fi1),DI(fi2)) * SP(TI(fi1),TI(fi2))
            return e.map(self)

    fr = FeynRules()
    
    amp0 = fr(amp0)
    amp1 = fr(amp1)
    amp2 = fr(amp2)

    return [ amp0, amp1, amp2 ]
    

# ----------------------

nL = Symbol("nL")
nH = Symbol("nH")
m = Symbol("m")
p = Vector("p")
q1 = Vector("q1")
q2 = Vector("q2")

As = Symbol("as")
Z2 = Symbol("Z2")
Zas = Symbol("Zas")
zm = Symbol("zm")
mm = Symbol("mm")
smu = Symbol("mu") # m/mu

p1 = p
p2 = p

set_Verbose(100)
amps = Amps()

mu = Index("mu")
nu = Index("nu")
    
letSP(p,m*m)
letSP(p,nu,expr(0))
    
extps = exvec([ p ])
loops = exvec()
proj = SpinProj("In", 1, p1, p2, m, m, nu, -1, -3) * ColorProj(-1, -3);

class nLnH(MapFunction):
    def map(self, e):
        w0 = w(0)
        if(not e.has(TR(w0))):
            return e
        elif(e.match(TR(w0))):
            if e.has(m):
                return nH * e
            else:
                return nL * e
        else:
            return e.map(self)

ampN = expr(0)
class DoFA(ParFun):
    def __call__(self, idx):
        amp = ampN[idx]
        amp = MatrixContract(amp)
        amp = nLnH()(amp)
        amp = amp.subs(gs>>sqrt(4*Pi*As*Zas))
        
        if(loops.size()!=2):
            amp = Z2*amp.subs([ m>>m*(1+zm) ])
        amp = amp.subs(LI(-2)>>mu)
        amp = amp * proj
        amp = MatrixContract(amp)
        set_form_using_su3(True)
        amp = form(amp)
        amp = amp.subs([ NF>>3, D>>4-2*ep ])
        if (loops.size()<1):
            return amp
        amp = TIR(amp, loops, extps)
        amp = factor(amp)
        if(loops.size()!=2):
            amp = series(amp,zm,2-loops.size())
        return amp

    
# -- LO --
ampN = amps[0]
res_vec = Parallel(ampN.size(), DoFA(), "LO")
Res0 = expr(0)
for item in res_vec:
    Res0 += item.subs([ d>>4-2*ep, D>>4-2*ep ])
tree = Res0.subs([ zm>>0, Z2>>1, Zas>>1 ])
Res0 = Res0/tree
Res0 = Res0.subs([ Z2>>RC.Z2("Q",m,2), zm>>RC.Zm(m,2)-1, Zas>>RC.Zas(2) ])
Res0 = Res0.subs([ NF>>3, NA>>8, nH>>1, nL>>3 ])
Res0 = series(series(Res0,ep,0),As,2)
Res0 = Res0.subs([ log(m)>>log(mm)+log(smu), log(m/smu)>>log(mm), log(smu/m)>>-log(mm) ])
ho << "Result @LO:" << endl
ho << Res0 << endl << endl

# -- MI --
mistxt = file2expr("mis.txt")
mi2ex = exmap()
for item in mistxt:
    mi2ex[item.op(0)] = item.op(1)

## -- NLO --
ampN = amps[1]
loops = exvec([ q1 ])
res_vec = Parallel(ampN.size(), DoFA(), "NLO")
res_vec = ApartIBP(1, res_vec, loops, extps)
Res1 = 0
for item in res_vec:
    Res1 += item.subs([ d>>4-2*ep, D>>4-2*ep ])
Res1 = Res1/tree
Res1 = Res1.subs(mi2ex)
Res1 = Res1.subs([ Z2>>RC.Z2("Q",m,1), zm>>RC.Zm(m,1)-1, Zas>>RC.Zas(1) ])
Res1 = Res1.subs([ NF>>3, NA>>8, nH>>1, nL>>3 ])
Res1 = series(series(Res1,ep,0),As,2)
Res1 = Res1.subs([ log(m)>>log(mm)+log(smu), log(m/smu)>>log(mm),log(smu/m)>>-log(mm) ])
Res1 = normal(Res1)
ho << "Result @NLO:" << endl
ho << Res1 << endl << endl

## -- NNLO --
ampN = amps[2]
loops = exvec([ q1, q2 ])
res_vec = Parallel(ampN.size(), DoFA(), "NNLO")
res_vec = ApartIBP(1, res_vec, loops, extps);
Res2 = expr(0)
for item in res_vec:
    Res2 += item.subs([ d>>4-2*ep, D>>4-2*ep ])
Res2 = Res2/tree
Res2 = Res2.subs(mi2ex)
Res2 = Res2.subs([ Zas>>RC.Zas(0) ])
Res2 = Res2.subs([ NF>>3, NA>>8, nH>>1, nL>>3 ])
Res2 = series(series(Res2,ep,0),As,2)
Res2 = Res2.subs([ log(m)>>log(mm)+log(smu), log(m/smu)>>log(mm), log(smu/m)>>-log(mm) ])
Res2 = normal(Res2)
ho << "Result @NNLO:" << endl
ho << Res2 << endl << endl

ho << "Final Result:"
Res = Res0 + Res1 + Res2
Res = normal(Res)
ho << Res << endl << endl
