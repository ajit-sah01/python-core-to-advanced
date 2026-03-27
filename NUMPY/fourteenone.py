"""
fourteenone.py
Linear Algebra Basics using NumPy
"""

import numpy as np

def basics():
    # Define vectors
    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])

    # Define matrices
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    print("Vector v1:", v1)
    print("Vector v2:", v2)

    # Operations
    print("Addition:", v1 + v2)
    print("Dot Product:", np.dot(v1, v2))

    print("\nMatrix A:\n", A)
    print("Matrix B:\n", B)

    print("Matrix Addition:\n", A + B)
    print("Matrix Multiplication:\n", np.dot(A, B))


if __name__ == "__main__":
    basics()