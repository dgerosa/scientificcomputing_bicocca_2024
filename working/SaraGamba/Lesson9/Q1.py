"""
Q1: Play with expressions
author: Sara Gamba
"""
import sympy as sym

def evaluation():
    x = sym.symbols("x")
    expr = x*sym.exp(-x) + x*(1-x)
    xval = [0.,0.1,0.2,0.4,0.8]
    for xx in xval:
        print("In x={}, the function is {}".format(xx,expr.subs(x, xx)))


if __name__ == "__main__":
    evaluation()