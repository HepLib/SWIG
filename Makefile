all: _HepLib.so

flatns=""
uname := $(shell uname -s)
ifeq ($(uname),Darwin)
  flatns = "-flat_namespace"
endif

HepLib.cpp: HepLib.i
	swig -python -c++ -o HepLib.cpp HepLib.i

HepLib.o : HepLib.cpp
	heplib++ -fPIC -c HepLib.cpp $$(python3-config --cflags)

_HepLib.so : HepLib.o
	heplib++ -shared $(flatns) HepLib.o -o _HepLib.so $$(python3-config --ldflags --embed)

clean:
	rm -f HepLib.cpp HepLib.o _HepLib.so HepLib.py
