"""
fourteenthree.py
Eigenvalues and Eigenvectors using NumPy
"""

import numpy as np

def eigen():
    A = np.array([[4, -2],
                  [1,  1]])

    eigenvalues, eigenvectors = np.linalg.eig(A)

    print("Matrix A:\n", A)
    print("Eigenvalues:\n", eigenvalues)
    print("Eigenvectors:\n", eigenvectors)


if __name__ == "__main__":
    eigen()