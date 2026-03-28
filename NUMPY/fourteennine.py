import numpy as np

rng = np.random.default_rng()

data = np.array([10, 20, 30, 40, 50])

# Random sample with replacement
sample1 = rng.choice(data, size=3, replace=True)

# Without replacement
sample2 = rng.choice(data, size=3, replace=False)

# Weighted sampling
weights = [0.1, 0.2, 0.3, 0.2, 0.2]
sample3 = rng.choice(data, size=3, p=weights)

print(sample1, sample2, sample3)