"""
Q1: Machine Precision
author: Sara Gamba
"""
def MachinePrecision():
    eps=1.  
    while (1+eps)!=1:
        eps=eps/2.

    eps=eps*2

    print("The smallest epsilon is", eps)


if __name__ == "__main__":
    MachinePrecision()

