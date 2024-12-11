"""
Q4: It's over Anakin, I have the high ground. I hate you!
author: Sara Gamba
"""
import cProfile
import pstats
import numpy as np
import timeit
from numba import njit
import argparse

def slow():
    """
    slow
    param:
    return: slow way of summing i**2 a large number of times
    """
    sum=0
    for i in range(1, 10000000):
        sum+=i**2
    return sum

def np_func(): 
    """
    np_func
    param:
    return: numpy way of summing i**2 a large number of times
    """
    a = np.arange(1, 10000000)
    sum = np.sum(a**2)
    return sum

@njit    
def numba_func():
    """
    numba_func
    param:
    return: numba way of summing i**2 a large number of times
    """
    sum = 0
    for i in range(1, 10000000):
        sum+=i**2
    return sum

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='It\'s over Anakin, I have the high ground. I hate you! Just run the code!')
    args = parser.parse_args()
    
    cProfile.run('slow()', 'profile_results') #understanding where I waste time

    stats = pstats.Stats('profile_results') #stat results
    stats.strip_dirs().sort_stats('time').print_stats(10)  
    #printing the time
    print("Original:{} s".format(timeit.timeit('slow()', globals=globals(), number=10))) 
    print("Numpy:{} s".format(timeit.timeit('np_func()', globals=globals(), number=10)))
    print("Numba:{} s".format(timeit.timeit('numba_func()', globals=globals(), number=10)))
