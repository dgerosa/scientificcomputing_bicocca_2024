"""
Q2: Planetary positions
author: Sara Gamba
"""
import matplotlib.pyplot as plt
import numpy as np

def Planets():

    a = np.array([0.39, 0.72, 1.00, 1.52, 5.20, 9.54, 19.22, 30.06, 39.48])
    P = np.array([0.24, 0.62, 1.00, 1.88, 11.86, 29.46, 84.01, 164.8, 248.09])
    names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]

    plt.plot(a,P, marker=".",color="black", linewidth=0, markersize=12)
    plt.xlabel(r"$a$ [AU]")
    plt.ylabel(r"$P$ [year]")
    plt.yscale("log")
    plt.xscale("log")

    for txt, distance, period in zip(names,a,P):
        plt.annotate(txt,(distance,period)) 

    plt.show()


if __name__ == "__main__":
    Planets()