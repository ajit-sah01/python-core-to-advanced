import numpy as np

arr = np.array([[1,2],[3,4]])

# Simple iteration
for x in arr:
    print(x)

# Element-wise iteration
for x in np.nditer(arr):
    print(x)
