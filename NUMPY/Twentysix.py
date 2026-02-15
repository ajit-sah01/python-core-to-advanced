import numpy as np

arr = np.array([10,20,30,40])

print(arr > 20)
print(arr == 30)

# Filter using condition
filtered = arr[arr > 20]
print(filtered)
