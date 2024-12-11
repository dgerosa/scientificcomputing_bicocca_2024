"""
Q1: Simple numerical integral
author: Sara Gamba
"""
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import argparse


def power_law_log(x, a, b): 
    """
    power_law_log
    param: a (exp), b constant
    return: fit function
    """
    return  np.log(x) * a + b 


def NumericalIntegrals():
    """
    NumericalIntegrals
    param:
    return: different type of integrals and fit of integrate.simps varying the number of sample points
    """
    xmin=-5.
    xmax=5.
    function = lambda x: np.exp(-x*x) #function to integrate
    integral_q , err = integrate.quad(function,xmin,xmax) #quad integral
    print("quad integral: {} \n".format(integral_q))
    N=64
    dim=4
    errors = np.array([])
    it = np.array([])
    for i in range(dim):#simps integral
        x = np.linspace(-5, 5, N)
        f = np.exp(-x**2)
        integral_s = integrate.simps(f, x) 
        print("simps integral with {} points: {} \n".format(N,integral_s))
        errors = np.append(errors, abs(integral_s-integral_q))
        it = np.append(it, N)
        N = N*2

    plt.loglog(it,errors, marker=".",color="black", linewidth=0, markersize=12)
    plt.xlabel(r"$N$")
    plt.ylabel(r"$errore$")

    #fit to check power low
    popt, pcov = curve_fit(power_law_log, it, np.log(errors))

    #curve fit generation
    N_fit = np.linspace(min(it), max(it), 100)
    y_fit = np.exp(power_law_log(N_fit, *popt))

    plt.plot(N_fit, y_fit, "-",color="Orange")

    #Fit results
    print(f"Fit of exp(N,a)*c \n  a = {popt[0]:.2f} \n b = {popt[1]:.2f}") #print results

    plt.savefig("fit.pdf")
    print("fit.pdf correctly saved.")




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simple numerical integral. Just run the code!')
    args = parser.parse_args()
    NumericalIntegrals()