import numpy as np

arr = np.array([10,20,30,40])

# View (shares memory)
view_arr = arr.view()
view_arr[0] = 99
print(arr)   # original changes

# Copy (independent memory)
copy_arr = arr.copy()
copy_arr[1] = 100
print(arr)   # original does not change
