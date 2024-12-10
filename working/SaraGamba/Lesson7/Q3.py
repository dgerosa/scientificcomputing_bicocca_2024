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

# sum of two sub arrays
def sum_sub_array(start, end, array1, array2):
    return np.sum(array1[start:end] + array2[start:end])

# sum of two arrays, parallel
def parallel_sum(array1, array2, num_cores):
    size = len(array1)
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
        results.append(pool.apply_async(sum_sub_array, (start, end, array1, array2))) # runs in one process
    
    pool.close() #close the process object
    pool.join() #waiting for all processes
    
    # sum all results from cores
    tot = sum(result.get() for result in results)
    return tot

# test scaling
def test_scaling():
    size = int(1e7)
    array1 = np.random.rand(size)
    array2 = np.random.rand(size)
    
    # varying the numbers of cores
    num_cores_tot = [1, 2, 4, 8, 16, 32]
    times = []
    
    for num_cores in num_cores_tot:
        start_time = time.time()
        parallel_sum(array1, array2, num_cores)
        end_time = time.time()
        times.append(end_time - start_time)
    
    # results plot
    plt.figure()
    plt.plot(num_cores_tot, times, marker='o')
    plt.xlabel('Cores')
    plt.ylabel('Time (s)')
    plt.title('Scaling')
    plt.savefig("test_scaling.pdf")


def create_benchmark(file_name="benchmark.json"):
    """Crea un benchmark salvando i dati e i risultati attesi."""
    size = 1000000
    array1 = np.random.rand(size)
    array2 = np.random.rand(size)
    np.savez("test_data.npz", array1=array1, array2=array2)
    
    expected_sum = parallel_sum(array1, array2, num_cores=4)
    benchmark = {"expected_sum": expected_sum}
    with open(file_name, "w") as f:
        json.dump(benchmark, f)
    print(f"Benchmark salvato in {file_name}")


if __name__ == "__main__":
    
    num_cores = os.cpu_count()
    print(f"Number of cores in the CPU: {num_cores}")
    
    test_scaling()
    create_benchmark()