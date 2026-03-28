import numpy as np

rng = np.random.default_rng()

# Random floats (0 to 1)
arr = rng.random(5)

# Random integers
ints = rng.integers(1, 10, size=5)

print(arr)
print(ints)


print("---------")
# Normal distribution (mean=0, std=1)
normal = rng.normal(loc=0, scale=1, size=1000)
print(normal)
# Uniform distribution
uniform = rng.uniform(0, 1, 1000)
print(uniform)
# Binomial distribution
binom = rng.binomial(n=10, p=0.5, size=1000)
print(binom)