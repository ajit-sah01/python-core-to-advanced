import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]], order='C')

b = np.array([[1, 2, 3],
              [4, 5, 6]], order='F')

print(a.flags)  # C-contiguous
print(b.flags)  # F-contiguous

x = np.array([1, 2, 3])
y = x.view()   # shares memory
z = x.copy()   # new memory

x[0] = 100

print(y)  # affected
print(z)  # not affected