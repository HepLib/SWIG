all: _HepLib.so

HLS=HepLib_SWIG

flatns=""
uname := $(shell uname -s)
ifeq ($(uname),Darwin)
  flatns = "-flat_namespace"
endif

$(HLS).cpp:
	swig -python -c++ -o $(HLS).cpp $$(heplib-config --prefix)/include/HepLib.i

$(HLS).o : $(HLS).cpp
	heplib++ -fPIC -c $(HLS).cpp $$(python3-config --cflags)

_HepLib.so : $(HLS).o
	heplib++ -shared $(flatns) $(HLS).o -o _HepLib.so $$(python3-config --ldflags --embed)

clean:
	rm -rf $(HLS)* _HepLib.so HepLib.py __pycache__ xform* *.gar
