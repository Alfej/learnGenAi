# Advance indexing

# fancy indexing
import numpy as np

a = np.arange(24).reshape(6,4)
print("*"*30)
print(a)

#  fancy indexing: When you want to pick some perticuler rows and columns that can't be done by the slicing we can use this
print("*"*30)
print(a[[0,2,3]])

print("*"*30)
print(a[:,[0,2,3]])

# Boolean indexing: When to extract the numbers based on the condition
b = np.random.randint(1,100,24).reshape(6,4)

print("*"*30)
print(b)
print("*"*30)


print(b[b>50])
print("*"*30)
