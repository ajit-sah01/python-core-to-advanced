import numpy as np

rng = np.random.default_rng()

# Random floats (0 to 1)
arr = rng.random(5)

# Random integers
ints = rng.integers(1, 10, size=5)

print(arr)
print(ints)