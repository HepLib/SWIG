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
xs = expr("{a,b,c,x(1),y(2)}")
print("list:", xs)
print("1st element:", xs.op(0))
print("1st element:", xs[0])
print()

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

# test exmap
#----------------------
e3 = exmap()
e3[p] = p + P
e3[P] = expr(1)
e3[P] = P
print("exmap: ", e3)

e3 = exmap({P:P,p:p})
print("exmap: ", e3)

print()
