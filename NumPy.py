
#1. Create a null vector of size 10 but the fifth value which is 1.

import numpy as np

null_v = np.zeros(10)
null_v[4] = 1

print(null_v)




#2. Create a vector with values ranging from 10 to 49.

import numpy as np

vector = np.arange(10, 50)

print(vector)




#3. Create a 3x3 matrix with values ranging from 0 to 8

import numpy as np

matrix = np.arange(9).reshape(3, 3)

print(matrix)




#4. Find indices of non-zero elements from [1,2,0,0,4,0]

import numpy as np

indices = np.array([1, 2, 0, 0, 4, 0])

nonzero_indices = np.nonzero(indices)

print(nonzero_indices)





#5. Create a 10x10 array with random values and find the minimum and maximum values.

import numpy as np

array = np.random.rand(10, 10)

minimum_value = np.min(array)
maximum_value = np.max(array)

print("Array:")
print(array)
print("Minimum value:", minimum_value)
print("Maximum value:", maximum_value)




#6. Create a random vector of size 30 and find the mean value.


import numpy as np

vector = np.random.rand(30)

mean_value = np.mean(vector)

print("Vector:")
print(vector)
print("Mean value:", mean_value)



