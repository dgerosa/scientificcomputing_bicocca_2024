"""
Q1: Play with expressions
author: Sara Gamba
"""
import sympy as sym
import argparse

def evaluation():
    """
    evaluation
    param:
    return: evaluates the function in 5 different points
    """
    x = sym.symbols("x")
    expr = x*sym.exp(-x) + x*(1-x)
    xval = [0.,0.1,0.2,0.4,0.8]
    for xx in xval:
        print("In x={}, the function is {}".format(xx,expr.subs(x, xx)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Play with expressions. Just run the code!')
    args = parser.parse_args()
    
    evaluation()