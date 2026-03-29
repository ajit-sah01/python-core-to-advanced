import numpy as np

# Without vectorization (slow)
arr = np.arange(1, 1000000)

def slow_square(x):
    result = []
    for i in x:
        result.append(i * i)
    return result

# With vectorization (fast)
fast_result = arr ** 2

print(fast_result[:10])