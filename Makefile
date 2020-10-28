all: _HepLib.so

HepLib.cpp: HepLib.i
	swig -python -c++ -o HepLib.cpp HepLib.i

HepLib.o : HepLib.cpp
	heplib++ -fPIC -c HepLib.cpp $$(python3-config --cflags)

_HepLib.so : HepLib.o
	heplib++ -shared -flat_namespace HepLib.o -o _HepLib.so $$(python3-config --ldflags) -lpython3.9

clean:
	rm -f HepLib.cpp HepLib.o _HepLib.so HepLib.py
