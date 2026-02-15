import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])

# Split into equal parts
split_arr = np.split(arr, 4)
print(split_arr)

# Split at specific indices
split_custom = np.array_split(arr, [3,5])
print(split_custom)
