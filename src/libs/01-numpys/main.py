import numpy as np

## create 1D array
arr1 = np.array([1,2,3,4,5])

print(arr1)
print(arr1.shape)

print(type(arr1))

# 1D to 2D 
arr2 = np.array([1,2,3,4,5])
print(arr2.reshape(1, 5)) # 1 row, 5 columns