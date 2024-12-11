"""
Q2: My own test
author: Sara Gamba
"""
import numpy as np
np.__config__.show()
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['MKL_NUM_THREADS'] = '1'
import argparse
import multiprocessing
import time
import os
import json
import matplotlib.pyplot as plt
import unittest



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
    plt.savefig("./working/SaraGamba/Lesson8/test_scaling.pdf")
    print("./working/SaraGamba/Lesson8/test_scaling.pdf correctly saved.")


def create_benchmark(file_name="./working/SaraGamba/Lesson8/benchmark.json"):
    """
    create_benchmark
    param: file name
    return: it creates a benchmark and saves results
    """
    size = 1000000
    a1 = np.random.rand(size)
    a2 = np.random.rand(size)
    np.savez("./working/SaraGamba/Lesson8/test_benchmark.npz", a1=a1, a2=a2)
    
    ex_sum = parallel_sum(a1, a2, num_cores=4)
    benchmark = {"ex_sum": ex_sum}
    with open(file_name, "w") as file:
        json.dump(benchmark, file)
    print(f"Benchmark correctly saved in {file_name}")

class RegressionTest(unittest.TestCase):
    
    def test_regression(self):
        """
        test_regression
        param:
        return: regression test with the saved benchmark
        """
        with open("./working/SaraGamba/Lesson8/benchmark.json", "r") as file:
            benchmark = json.load(file)
        data = np.load("./working/SaraGamba/Lesson8/test_benchmark.npz")
        a1 = data["a1"]
        a2 = data["a2"]
        new = parallel_sum(a1, a2, num_cores=4)
        self.assertAlmostEqual(
            new, benchmark["ex_sum"], delta=1e-6,
            msg="Regression test failed"
        )


class TestLesson7Q3(unittest.TestCase):

    def test_sum_sub_array(self):
        """
        test_sum_sub_array
        param:
        return: test the sum of sub arrays
        """
        a1 = np.array([1, 2, 3, 4, 5])
        a2 = np.array([5, 4, 3, 2, 1])
        res = sum_sub_array(1, 4, a1, a2)
        self.assertEqual(res, 18) 

    def test_parallel_sum(self):
        """
        test_parallel_sum
        param:
        return: test the parallel sum
        """
        a1 = np.array([1, 2, 3, 4, 5])
        a2 = np.array([5, 4, 3, 2, 1])
        res = parallel_sum(a1, a2, num_cores=2)
        self.assertEqual(res, 30)  

    def test_parallel_sum_large_array(self):
        """
        test_parallel_sum_large_array
        param:
        return: test the parallel sum of large and random arrays
        """
        size = 1000000
        a1 = np.random.rand(size)
        a2 = np.random.rand(size)
        expected = np.sum(a1 + a2)
        res = parallel_sum(a1, a2, num_cores=4)
        self.assertAlmostEqual(res, expected, delta=1e-6)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lesson7Q3.py code and test")
    parser.add_argument("--scaling", action="store_true", help="Scaling test.")
    parser.add_argument("--create-benchmark", action="store_true", help="Benchmark creation.")
    parser.add_argument("--run-regression-test", action="store_true", help="Regression test only.")
    parser.add_argument("--run-tests", action="store_true", help="All unit tests.")

    args = parser.parse_args()

    if args.scaling:
        print("Executing scaling test...")
        num_cores = os.cpu_count()
        print(f"Number of cores in the CPU: {num_cores}")
        test_scaling()

    elif args.create_benchmark:
        print("Creating benchmark...")
        num_cores = os.cpu_count()
        create_benchmark()
    elif args.run_tests:
        print("Executing unit tests...")
        unittest.main(argv=[''], exit=False)
    elif args.run_regression_test:
        print("Executing regression test...")
        unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(RegressionTest))
    else:
        parser.print_help()
