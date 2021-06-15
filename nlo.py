#!/usr/bin/env python3

# python version for nlo.cpp

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
    print("Process Filter: [ ", end='')
    for amp in amps:
        print(amp.size(), end=' ')
    print("] :> [ ", end='')

    amp0 = filter(amp0);
    amp1 = filter(amp1);
    amp2 = filter(amp2);
    
    for amp in amps:
        print(amp.size(), end=' ')
    print("]")

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

m = Symbol("m")
p = Vector("p")
q1 = Vector("q1")
q2 = Vector("q2")

p1 = p
p2 = p

set_Verbose(100)
amps = Amps()

mu = Index("mu")
nu = Index("nu")
    
letSP(p,m*m)
letSP(p,nu,expr(0))
    
extps = exvec([ p ])
loops = exvec([ q1 ])
proj = SpinProj("In", 1, p1, p2, m, m, nu, -1, -3) * ColorProj(-1, -3);

amp1 = amps[1][0]
amp1 = amp1.subs(LI(-2) >> mu)
print()
print("amp @ NLO:")
print(amp1)


amp1 = MatrixContract(amp1);
print()
print("amp1 (after MatrixContract):")
print(amp1)


amp1 = amp1 * proj;
amp1 = MatrixContract(amp1);
print()
print("amp1 (MatrixContrat with Spin Projector):")
print(amp1)

set_form_using_su3(True)
amp1 = form(amp1)
amp1 = amp1.subs([NF>>3,D>>4-2*ep])
print()
print("amp1 (after FORM evaluation):")
print(amp1.factor())


amp1 = TIR(amp1, loops, extps);
amp1 = amp1.subs([ NF>>3,D>>4-2*ep])
print()
print("amp1 (after TIR):")
print(factor(amp1))


res_vec = exvec()
res_vec.push_back(amp1)
res_vec = ApartIBP(1, res_vec, loops, extps)
res = 0
for item in res_vec:
    res += item.subs([d>>4-2*ep,D>>4-2*ep])
mi = expr("F({q1^2+(-2)*p*q1},{1})")
miv = -tgamma(-1+ep)*pow(m,2*(1-ep))*I*pow(Pi,2-ep)*pow(2*Pi,2*ep-4)
res = res.subs( mi>>miv )
res = series(res,ep,0)
print()
print("amp1 (final expression):");
print(collect(factor(res),ep))





