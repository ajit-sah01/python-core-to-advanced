"""
fourteenonefive.py
Solving Linear Systems Ax = b using NumPy
"""

import numpy as np

def solve_system():
    A = np.array([[3, 1],
                  [1, 2]])
    
    b = np.array([9, 8])

    x = np.linalg.solve(A, b)

    print("Matrix A:\n", A)
    print("Vector b:", b)
    print("Solution x:", x)


if __name__ == "__main__":
    solve_system()