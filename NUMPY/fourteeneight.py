import numpy as np
rng = np.random.default_rng()

arr = np.array([1, 2, 3, 4, 5])

# In-place shuffle
rng.shuffle(arr)
print(arr)

# Permutation (returns new array)
perm = rng.permutation(arr)
print(perm)