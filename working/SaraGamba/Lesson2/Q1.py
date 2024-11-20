import numpy as np

first_array = np.arange(15).reshape(3,5)
first_array = (first_array+1).transpose()
print(first_array)

rows=8
columns=10
second_array = np.ones((columns,rows),dtype=int)
second_array[1:-1,1:-1]=0
print(second_array)

