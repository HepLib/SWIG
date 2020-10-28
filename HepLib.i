/* File: HepLib.i */
%module HepLib

%{
#define SWIG_FILE_WITH_INIT
#include "Wrap.h"
%}

//--------------------------------------------------------------------

%include std_string.i
%include exception.i

%exception {
    try {
        $action
    } catch(const std::exception& ex) {
        SWIG_exception(SWIG_RuntimeError, ex.what());
    } catch(...) {
        SWIG_exception(SWIG_RuntimeError, "HepLib unkonwn exception.");
    }
}

class expr {
public:
    expr(int i);
    expr(const std::string &s);
    
    expr operator+(const expr &e);
    expr operator-(const expr &e);
    expr operator*(const expr &e);
    expr operator/(const expr &e);
    expr operator-();
    
    expr operator+(const int i);
    expr operator-(const int i);
    expr operator*(const int i);
    expr operator/(const int i);
    
    expr expand();
    expr normal();
    expr factor();
    expr series(const expr &s, int o);
    
    std::string __str__();
    
    %pythoncode %{
    def __radd__(self, other):
        return expr(other) + self
    def __rsub__(self, other):
        return expr(other) - self
    def __rmul__(self, other):
        return expr(other) * self
    def __rdiv__(self, other):
        return expr(other) / self
    
    %}
};

extern expr expand(const expr &e);
extern expr normal(const expr &e);
extern expr factor(const expr &e);
extern expr series(const expr &e, const expr &s, int o);

extern expr pow(const expr &e1, const expr &e2);
extern expr pow(const expr &e, const int n);

extern expr Index(const std::string &s);
extern expr Vector(const std::string &s);
extern expr Symbol(const std::string &s);
extern expr SP(const expr &e1, const expr &e2);
extern expr GAS(const expr &e);
extern expr TR(const expr &e);
extern expr form(const expr &e);

extern void letSP(const expr &e1, const expr &e2, const expr &e12);
