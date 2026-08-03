#  Brodcasting: It is a powerful mechanism that allows numpy to work with arrays of different shapes when performing arithmetic operations. 
#  THE SMALLER ARRAY IS "BROADCAST" ACROSS THE LARGER ARRAY SO THAT THEY HAVE COMPATIBLE SHAPES.

#  rules of broadcasting:
#  1. Make the 2 arrays have the same number of dimension:
    #  - If the arrays do not have the same number of dimensions, prepend the shape of the smaller array with ones until both shapes have the same length.
# 2. Make each dimension of the arrays same size:
    #  - If the shape of the two arrays does not match in a dimension, the array with shape equal to 1 in that dimension is stretched to match the other shape.
    #  If the size in any dimension is different and neither is equal to 1, an error is raised.

# example 1
import numpy as np

a = np.arange(12).reshape(4,3)
b = np.arange(3)

print("*"*30)
print(a)
print("*"*30)
print(b)
print("*"*30)
print(a+b)
print("*"*30)

#  this will not work because the shape of a is (3,4) and the shape of b is (3,) so after streching the shape of b will become (1,3)->(3,3) and the shape of a is (3,4) so they are not compatible and it will give an error.
a = np.arange(12).reshape(3,4) 
b = np.arange(3)

try:
    print("*"*30)
    print(a)
    print("*"*30)
    print(b)
    print("*"*30)
    print(a+b)
    print("*"*30)
except Exception as e:
    print("Error:", e)
