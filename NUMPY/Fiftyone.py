import numpy as np

# Example 1: Broadcasting 2D with 1D
A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([10, 20, 30])

result = A + B  # Broadcast B across rows
print(result)

# Example 2: Column-wise broadcasting
C = np.array([[1], [2]])
D = np.array([10, 20, 30])

result2 = C + D
print(result2)

# Example 3: Manual broadcasting using np.newaxis
x = np.array([1, 2, 3])
y = np.array([4, 5])

res = x[np.newaxis, :] + y[:, np.newaxis]
print(res)