#!/usr/bin/env python3

from HepLib import *

# cout & hout

cc = BOLDYELLOW

e0 = expr("pow(x+y,3)")
ho << cc << "ho e0: " << RESET << e0 << endl
ho << cc << "ho expanded: " << RESET << e0.expand() << endl << endl
co << cc << "co e0: " << RESET << e0 << endl
co << cc << "co expanded: " << RESET << e0.expand() << endl << endl

# expr as key in dict
p = Vector("p")
P = Vector("P")
dict = {}
dict[p] = p
dict[2*p-p] = 1
dict[2*p-P] = P
ho << cc << ("expr as key in dictionary:") << RESET << endl
for k in dict:
    ho << cc << "key = " << RESET << k
    ho << cc << " & value = " << RESET << dict[k] << endl
ho << endl

# expr from string with dict
p = Vector("p")
P = Vector("P")
st = {}
st["p"] = p
st["P"] = P
e1 = expr("p+P", st)
ho << cc << "expr from string: " << RESET << e1 << endl

# expr from string as a list
xs = expr("{a,x(0),c,x(1),x(2)}")
ho << cc << "list: " << RESET << xs << endl
ho << cc << "1st element: " << RESET << xs.op(0) << endl
ho << cc << "1st element: " << RESET << xs[0] << endl << endl

for item in xs:
    ho << cc << "item in expr: " << RESET << item << endl
ho << endl

ss = exmap()
ss[x(w)] = expr("sin(t)")+WF(w)
xs2 = subs(xs, ss)
ho << cc << "new list: " << RESET << xs2 << endl

# expr with list
xs = expr([p,P,p+P])
ho << cc << "expr with list:" << RESET << xs << endl
ho << endl

# test exvec
#----------------------
e1 = exvec()
e1.push_back(p)
e1.push_back(P)
e1.push_back(p)
e1.push_back(P)
ho << cc << "exvec: " << RESET << e1 << endl
ho << cc << "from hout: " << RESET << e1 << endl

e1 = exvec([p, P, p+P, P, p])
ho << cc << "exvec: " << RESET << e1 << endl
e1.subs(p>>1)
ho << cc << "exvec: " << RESET << e1 << endl
ss = exmap()
ss[P] = expr("sin(t)")
e1.subs(ss)
ho << cc << "exvec: " << RESET << e1 << endl
ho << endl

ho << cc << "test iterator for exvec:" << RESET << endl
for item in e1:
    ho << cc << "exvec item:" << RESET << item << endl
ho << endl

# test exset
#----------------------
e2 = exset()
e2.insert(p)
e2.insert(P)
e2.insert(p)
e2.insert(P)
ho << cc << "exset: " << RESET << e2 << endl

e2 = exset([p, P, p+P, P, p])
ho << cc << "exset: " << RESET << e2 << endl
ho << cc << "from hout: " << e2 << RESET << endl
ho << endl

ho << cc << "test iterator for exset:" << endl
for item in e2:
    ho << cc << "exset item:" << RESET << item << endl
ho << endl

# test exmap
#----------------------
e3 = exmap()
e3[p] = p + P
e3[P] = expr(1)
e3[P] = P
ho << cc << "exmap: " << RESET << e3 << endl
co << cc << "from cout: " << RESET << e3 << endl
ho << endl

ho << cc << "test iterator for exmap:" << endl
for kv in e3:
    ho << cc << "exmap item: " << RESET << kv.first << " -> " << kv.second << endl
ho << endl

e3 = exmap({P:P,p:p})
ho << cc << "exmap: " << RESET << e3 << endl
ho << endl

ho << cc << "test iterator for exmap:" << endl
for kv in e3:
    ho << cc << "exmap item: " << RESET << kv.first << " -> " << kv.second << endl
ho << endl


# garRead & garWrite
#----------------------
ho << cc << "test garWrite & garRead:" << RESET << endl
data = {}
data["1"] = expr("a+b")
data["2"] = expr("sin(t)")
garWrite(data, "g1.gar")
garWrite("g2.gar", data)

data = garReadAll("g1.gar")
for k in data:
    ho << k << " -> " << data[k] << endl
ho << data["2"]+sin(Symbol("z")) << endl
ho << RunOS("rm g1.gar g2.gar") << endl

