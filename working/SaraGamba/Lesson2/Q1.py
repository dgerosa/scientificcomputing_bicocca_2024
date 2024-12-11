"""
Q1: Fun with arrays
author: Sara Gamba
"""
import numpy as np
import argparse

def ArrayFunction_1(rows,columns):
    """
    ArrayFunction_1
    param: rows and columns
    return: array with given number of rows and columns and selection of second and fourth array
    """
    first_array = np.arange(rows*columns).reshape(columns,rows)
    first_array = (first_array+1).transpose()
    print("First array:")
    print(first_array)
    selected_rows = first_array[[1, 3]]
    print("\nSecond and fourth rows:")
    print(selected_rows)


def ArrayFunction_2(rows,columns):
    """
    ArrayFunction_2
    param: rows and columns
    return: array with given number of rows and columns (0 in the center and ones on the outer part)
    """
    second_array = np.ones((columns,rows),dtype=int)
    second_array[1:-1,1:-1]=0
    print("Second array:")
    print(second_array)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Fun with arrays')
    parser.add_argument('--NumberofRows', type=int, help='Number of Rows to compute (greater than four)')
    parser.add_argument('--NumberofColumns', type=int, help='Number of Columns to compute')

    args = parser.parse_args()

    if(args.NumberofRows is None or args.NumberofColumns is None):
        print('Cannot start the program: missing the arguments!')
    else:
        ArrayFunction_1(args.NumberofRows,args.NumberofColumns)
        ArrayFunction_2(args.NumberofRows,args.NumberofColumns)