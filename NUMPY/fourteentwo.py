"""
fourteentwo.py
Determinant Calculation using NumPy
"""

import numpy as np

def determinant():
    A = np.array([[1, 2], [3, 4]])

    det = np.linalg.det(A)

    print("Matrix A:\n", A)
    print("Determinant of A:", det)


if __name__ == "__main__":
    determinant()