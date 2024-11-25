"""
Q3: Basins of attraction
author: Sara Gamba
"""
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

def f(x): #function
    return x**3 - 6*x**2 + 11*x - 6

def BasinsofAttraction():
    #plot function
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
    plt.show()

if __name__ == "__main__":

    BasinsofAttraction()