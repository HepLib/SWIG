#!/usr/bin/env python3

# python version for 0.cpp

from HepLib import *

x = Symbol("x")
y = Symbol("y")

data = exvec()
total = 1000;
for i in range(total):
    data.push_back(sin(exp(x+y*i)))

class ParFunRun(ParFun):
    def __call__(self, idx):
        ret = data[idx]
        ret = series(ret,x,5)
        return ret
        
f = ParFunRun()
set_Verbose(100)
set_Parallel_Process(2)
ret = Parallel(total, f)
#print(ret);

print()
