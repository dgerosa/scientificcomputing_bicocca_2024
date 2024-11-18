"""
Q12: Pascal
author: Sara Gamba
"""
import argparse

def PascalFunction(n):
    """
    PascalFunction:
    param: n (rows number)
    return: triangle (a list with all rows)
    """
    triangle = []
    for i in range(n):
        row = [1]*(i+1) #It creates a new line with values equal to 1
        for j in range(1,i): 
            row[j]=triangle[i-1][j-1]+triangle[i-1][j]
        triangle.append(row)
    return triangle
        

def Format(triangle):
    """
    Format:
    param: triangle (list of Pascal triangle)
    return: triangle (list with correct alligned format)
    """
    max_len = len(" ".join(map(str, triangle[-1])))  #finds the lenght of the longest line
    for row in triangle:
        row_string = " ".join(map(str, row)) #saves the contents of a list element separated by spaces in a string
        print(row_string.center(max_len)) #print and align the strings
    return triangle

def process(n,format):
    triangle=PascalFunction(n)
    if (format=="y"):
        Format(triangle)
        return
    if (format=="n"):
        print(triangle)
        return

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Pascal program')
    parser.add_argument('--NumberofRows', type=int, help='Number of Rows to compute')
    parser.add_argument('--Format', type=str, help='Format [y/n]')

    args = parser.parse_args()

    if(args.NumberofRows is None or args.Format is None):
        print('Cannot start the program: missing the arguments!')
    else:
        process(args.NumberofRows, args.Format)
