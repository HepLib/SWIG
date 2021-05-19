#!/usr/bin/env python3

from HepLib import *

me = Symbol("me")
mm = Symbol("mm")
e = Symbol("e")

mu = Index("mu")
nu = Index("nu")
r1 = Index("r1")
r2 = Index("r2")

p = Vector("p")
P = Vector("P")
k = Vector("k")
K = Vector("K")
q = Vector("q")

a = IndexCA("a")
b = IndexCA("b")
c = IndexCA("c")
d = IndexCA("d")
i = IndexCF("i")
j = IndexCF("j")
k = IndexCF("k")

#set_form_using_su3(False)
res = form(SUNT(lst([a,b,a,b]),i,i))
print(res.factor())

