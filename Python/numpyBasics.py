# Numpy:
# Numpy is a powerful library for numerical computing in Python. It provides support for large multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently.

# Numpy array vs Python list
# Numpy array have a fixed size at creation, unlike python list. Changing the size of ndarray it will delete and create the new one
# Datatype of elements in the ndarray should be same

import numpy as np

print("*"*25)
a = np.array([1,2,3])
print(a)

print("*"*25)
a = np.array([1,2,3], dtype= float)
print(a)

print("*"*25)
a = np.arange(1,10) # works like range of python
print(a)

print("*"*25)

a = np.arange(1,11).reshape(2,5) # multiplication of reshape should be equal to number of element
print(a)

print("*"*25)
a = np.ones((3,4)) #created 3*4 matrix with ones
print(a)

print("*"*25)
a = np.zeros((3,4)) #created 3*4 matrix with zeros 
print(a)

print("*"*25)
a = np.random.random((3,4)) #created 3*4 matrix with random number 
print(a)

print("*"*25)
a = np.linspace(-10,10,4) # Provide 4 points in the range from equal distance
print(a)

print("*"*25)
a = np.identity(4) # Provide identity matrix of n*n
print(a)

print("*"*25)
a1 = np.arange(10)
a2 = np.arange(12, dtype = float).reshape(3,4)
a3 = np.arange(8, dtype = int).reshape(2,2,2)

print(a1)
print(a2)
print(a3)

# ndim provides the number of direction
print("*"*25)
print(a3.ndim)

# shape provides shape of a matrix
print("*"*25)
print(a3.shape)

# Size provides total element of a matrix
print("*"*25)
print(a3.size)

# itemsize provides the element size in the array
print("*"*25)
print(a3.itemsize)

# dtype provides the data type of the array
print("*"*25)
print(a3.dtype)


#  Changing datatype
a3 = a3.astype(float)
print("*"*25)
print(a3.dtype)

# Scaler Operations
a2 = a2*2
print("*"*25)
print(a2)

# Relational Operations
print("*"*25)
print(a2>5)

# Vector operations
a4 = np.arange(12,24, dtype = float).reshape(3,4)
print("*"*25)
print(a2+a4)

# Functions

# min, max, sum, prod
print("*"*25)
print(np.max(a1))

print("*"*25)
print(np.max(a2,axis=1)) #0-> col 1-> row

# mean/ median/ std/ var
print("*"*25)
print(np.mean(a1))

print("*"*25)
print(np.std(a2,axis=1)) #0-> col 1-> row

# Dot Product
print("*"*25)
a5 = np.arange(12,24, dtype = float).reshape(4,3)
print(np.dot(a2,a5))

# Stacking
print("*"*25)
print(np.hstack((a4,a2)))

# Stacking
print("*"*25)
print(np.vstack((a4,a2)))

# split
print("*"*25)
print(np.hsplit(a4,2))  #( array, equal part)

# split
print("*"*25)
print(np.vsplit(a4,3))