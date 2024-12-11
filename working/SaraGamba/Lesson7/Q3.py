"""
Q3: Scaling
author: Sara Gamba
"""
import numpy as np
np.__config__.show()
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['MKL_NUM_THREADS'] = '1'

import multiprocessing
import time
import os
import json
import matplotlib.pyplot as plt
import argparse


def sum_sub_array(start, end, a1, a2):
    """
    sum_sub_array
    param: start of the sub array, end of the sub array, array 1 and array 2
    return: sum of two sub arrays
    """
    return np.sum(a1[start:end] + a2[start:end])


def parallel_sum(a1, a2, num_cores):
    """
    parallel_sum
    param: array 1 , array 2 and number of cores
    return: sum of two arrays, parallel
    """
    size = len(a1)
    chunk_size = size // num_cores #nearest integer
    pool = multiprocessing.Pool(num_cores) #creation of simultaneous processes
    results = []
    
    # array splitted into chunks and sum_sub_array function 
    for i in range(num_cores): #iteration for each core
        start = i * chunk_size #start of the chunck
        if (i < num_cores - 1): #if it is not the last core
            end = (i + 1) * chunk_size
        else: #if it is the last core
            end = size #last array index
        results.append(pool.apply_async(sum_sub_array, (start, end, a1, a2))) # runs in one process
    
    pool.close() #close the process object
    pool.join() #waiting for all processes
    
    # sum all results from cores
    tot = sum(result.get() for result in results)
    return tot


def test_scaling():
    """
    test_scaling
    param:
    return: plot of the scaling test performed
    """
    size = int(1e7)
    a1 = np.random.rand(size)
    a2 = np.random.rand(size)
    
    # varying the numbers of cores
    num_cores_tot = [1, 2, 4, 8, 16, 32]
    times = []
    
    for num_cores in num_cores_tot:
        start_time = time.time()
        parallel_sum(a1, a2, num_cores)
        end_time = time.time()
        times.append(end_time - start_time)
    
    # results plot
    plt.figure()
    plt.plot(num_cores_tot, times, marker='o')
    plt.xlabel('Cores')
    plt.ylabel('Time (s)')
    plt.title('Scaling')
    plt.savefig("test_scaling.pdf")
    print("test_scaling.pdf correctly saved.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Scaling. Just run the code!')
    args = parser.parse_args()
    
    num_cores = os.cpu_count()
    print(f"Number of cores in the CPU: {num_cores}")
    
    test_scaling()
