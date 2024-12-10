"""
Q3: There and back again
author: Sara Gamba
"""

import sympy as sym
import argparse

def integration_and_derivation():
    x = sym.symbols("x")
    expr = sym.sin(x)*sym.exp(-x)
    integral = sym.integrate(expr)
    print("Integral:",integral)
    der = sym.diff(expr)
    print("Derivative:",der)
    der = sym.simplify(der)
    print("Simplified:",der)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='There and back again. Just run the code!')
    args = parser.parse_args()
    integration_and_derivation()
