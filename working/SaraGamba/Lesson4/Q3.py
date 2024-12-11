"""
Q3: Basins of attraction
author: Sara Gamba
"""
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
import argparse

def f(x): 
    """
    f
    param: x
    return: function
    """
    return x**3 - 6*x**2 + 11*x - 6

def BasinsofAttraction():
    """
    BasinsofAttraction
    param: 
    return: Roots of the function and plot
    """
    x = np.linspace(0, 4, 500)
    y = f(x)
    plt.plot(x, y, color='black')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    
    #finding roots
    roots = []
    rs = []
    intervals = [(0.8, 1.3), (1.8, 2.3), (2.8, 3.3)]  

    for minimum, maximum in intervals:
        root, r = optimize.brentq(f, minimum, maximum, full_output=True)
        roots.append(root)
        plt.plot(np.array([root]), np.array([f(root)]), color="Red", marker="o")
        rs.append(r.converged)

    print("Roots of the function x**3 - 6*x**2 + 11*x - 6:", roots)
    print("Converged?:",rs)
    plt.grid()
    plt.savefig("bas.pdf")
    print("bas.pdf correctly saved.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Basins of attraction. Just run the code!')
    args = parser.parse_args()
    BasinsofAttraction()