"""
Q1: Fun with arrays
author: Sara Gamba
"""
import numpy as np
import argparse

def ArrayFunction_1(rows,columns):
    first_array = np.arange(rows*columns).reshape(columns,rows)
    first_array = (first_array+1).transpose()
    print(first_array)


def ArrayFunction_2(rows,columns):
    second_array = np.ones((columns,rows),dtype=int)
    second_array[1:-1,1:-1]=0
    print(second_array)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Fun with arrays')
    parser.add_argument('--NumberofRows', type=int, help='Number of Rows to compute')
    parser.add_argument('--NumberofColumns', type=int, help='Number of Columns to compute')

    args = parser.parse_args()

    if(args.NumberofRows is None or args.NumberofColumns is None):
        print('Cannot start the program: missing the arguments!')
    else:
        ArrayFunction_1(args.NumberofRows,args.NumberofColumns)
        ArrayFunction_2(args.NumberofRows,args.NumberofColumns)