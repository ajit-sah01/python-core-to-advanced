import numpy as np
import time

arr = np.random.rand(10_000_000)

# Python loop (slow)
start = time.time()
sum_val = 0
for i in arr:
    sum_val += i
print("Loop Time:", time.time() - start)

# NumPy optimized (fast)
start = time.time()
sum_val = np.sum(arr)
print("NumPy Time:", time.time() - start)