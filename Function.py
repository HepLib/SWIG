#!/usr/bin/env python3

from HepLib import *

class F1(Function):
    def __call__(self, e):
        print("F1 call: ")
        return "123+11";
    
f1 = F1()
print(f1())

