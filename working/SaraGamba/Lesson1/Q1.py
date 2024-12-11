"""
Q1: Machine Precision
author: Sara Gamba
"""
import argparse

def MachinePrecision():
    """
    MachinePrecision:
    param: 
    return: smallest epsilon machine precision
    """
    eps=1.  
    while (1+eps)!=1:
        eps=eps/2.

    eps=eps*2

    print("The smallest epsilon is", eps)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Machine Precision. Just run the code!')
    args = parser.parse_args()
    
    MachinePrecision()

