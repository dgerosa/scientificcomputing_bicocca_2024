"""
Q2: Histograms
author: Sara Gamba
"""
import numpy as np 
import matplotlib.pyplot as plt
from urllib.request import urlopen
import argparse

def Histogramming(url_file):
    '''
    Histogramming
    parameter: url file
    return: histogram
    '''
    url = urlopen(url_file) #openurl
    data = url.read() #read data

    file = "sample.txt" #new text file name 
    file_ = open(file, 'wb') #create file
    file_.write(data) #write data on the file
    file_.close() #close file


    column_data = np.loadtxt("sample.txt", usecols=1) #use first column of the file
    bin_content, bin_edges = np.histogram(column_data) #save bins and bin contents

    center = (bin_edges[:-1] + bin_edges[1:]) / 2 #bin center 

    plt.hist(column_data, bins='auto')  
    plt.xlabel("Quantity")
    plt.ylabel("Counts")
    plt.title("Histogram")

    result = np.vstack((bin_content, center)).transpose() #nice way to show results

    print("Printing bin centers\n", result)

    plt.savefig("hist.pdf")
    print("Histogram correctly saved.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Histograms. Just run the code!')
    args = parser.parse_args()
    
    Histogramming('https://raw.githubusercontent.com/sbu-python-summer/python-tutorial/master/day-3/sample.txt')