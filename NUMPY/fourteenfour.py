"""
fourteenfour.py
Matrix Inverse using NumPy
"""

import numpy as np

def inverse():
    A = np.array([[1, 2],
                  [3, 4]])

    inv_A = np.linalg.inv(A)

    print("Matrix A:\n", A)
    print("Inverse of A:\n", inv_A)


if __name__ == "__main__":
    inverse()