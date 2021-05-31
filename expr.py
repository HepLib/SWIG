#!/usr/bin/env python3

from HepLib import *

# expr as key in dict
p = Vector("p")
P = Vector("P")
dict = {}
dict[p] = p
dict[2*p-p] = 1
dict[2*p-P] = P
print("expr as key in dictionary:")
for k in dict:
    print("key =", k, " & value =", dict[k])
print()

# expr from string with dict
p = Vector("p")
P = Vector("P")
st = {}
st["p"] = p
st["P"] = P
e1 = expr("p+P", st)
print("expr from string:", e1)

# expr from string as a list
xs = expr("{a,x(0),c,x(1),x(2)}")
print("list:", xs)
print("1st element:", xs.op(0))
print("1st element:", xs[0])
print()

ss = exmap()
ss[x(w())] = expr("sin(t)")+WF(w())
xs2 = subs(xs, ss)
print("new list:", xs2)

# expr with list
xs = expr([p,P,p+P])
print("expr with list:", xs)
print()

# test exvec
#----------------------
e1 = exvec()
e1.push_back(p)
e1.push_back(P)
e1.push_back(p)
e1.push_back(P)
print("exvec: ",  e1)

e1 = exvec([p, P, p+P, P, p])
print("exvec: ", e1)
e1.subs(p>>1)
print("exvec: ", e1)
ss = exmap()
ss[P] = expr("sin(t)")
e1.subs(ss)
print("exvec: ", e1)

print()
print("test iterator for exvec:")
for item in e1:
    print("exvec item:", item)

print()

# test exset
#----------------------
e2 = exset()
e2.insert(p)
e2.insert(P)
e2.insert(p)
e2.insert(P)
print("exset: ", e2)

e2 = exset([p, P, p+P, P, p])
print("exset: ", e2)

print()
print("test iterator for exset:")
for item in e2:
    print("exset item:", item)

print()

# test exmap
#----------------------
e3 = exmap()
e3[p] = p + P
e3[P] = expr(1)
e3[P] = P
print("exmap: ", e3)

print()
print("test iterator for exmap:")
for kv in e3:
    print("exmap item:", kv.first,"->",kv.second)
print()

e3 = exmap({P:P,p:p})
print("exmap: ", e3)

print()
print("test iterator for exmap:")
for kv in e3:
    print("exmap item:", kv.first,"->", kv.second)

print()


# expr with integer
#----------------------
x = Symbol("x")
print(pow(x,3))
print(3*x)
print(3+x)
print(x/3)
print(expr(3)/x)

# garRead & garWrite
#----------------------
data = {}
data["1"] = expr("a+b")
data["2"] = expr("sin(t)")
garWrite(data, "g1.gar")
garWrite("g2.gar", data)

data = garReadAll("g1.gar")
for k in data:
    print(k,":",data[k])
print(data["2"]+sin(Symbol("z")))
