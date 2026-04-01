# numpy_broadcasting_advanced.py

import numpy as np

def basic_broadcasting():
    print("\n--- Basic Broadcasting ---")
    A = np.array([[1, 2, 3],
                  [4, 5, 6]])
    B = np.array([10, 20, 30])
    print(A + B)

def column_broadcasting():
    print("\n--- Column Broadcasting ---")
    A = np.array([[1, 2, 3],
                  [4, 5, 6]])
    B = np.array([[10],
                  [20]])
    print(A + B)

def high_dimensional():
    print("\n--- High Dimensional Broadcasting ---")
    A = np.ones((2, 3, 4))
    B = np.array([1, 2, 3, 4])
    print((A + B).shape)

def newaxis_example():
    print("\n--- np.newaxis Example ---")
    X = np.array([1, 2, 3])
    Y = np.array([10, 20])
    result = X[:, np.newaxis] + Y
    print(result)

def pairwise_operations():
    print("\n--- Pairwise Matrix (Advanced) ---")
    A = np.array([1, 2, 3])
    B = np.array([10, 20, 30])
    result = A[:, None] + B
    print(result)

def image_processing_sim():
    print("\n--- Image Processing Simulation ---")
    image = np.random.rand(4, 4, 3)
    scale = np.array([1.0, 0.5, 0.2])
    result = image * scale
    print("Scaled image shape:", result.shape)

def broadcasting_error_demo():
    print("\n--- Broadcasting Error Demo ---")
    A = np.array([1, 2, 3])
    B = np.array([1, 2])
    try:
        print(A + B)
    except ValueError as e:
        print("Error:", e)

def performance_demo():
    print("\n--- Performance Insight ---")
    A = np.random.rand(1000000)
    B = 5
    result = A + B
    print("Broadcasting done on large array")

def debug_shapes():
    print("\n--- Debug Shapes ---")
    A = np.array([[1, 2, 3]])
    B = np.array([1, 2, 3])
    print("A shape:", A.shape)
    print("B shape:", B.shape)

def main():
    basic_broadcasting()
    column_broadcasting()
    high_dimensional()
    newaxis_example()
    pairwise_operations()
    image_processing_sim()
    broadcasting_error_demo()
    performance_demo()
    debug_shapes()

if __name__ == "__main__":
    print("=== Advanced NumPy Broadcasting Demo ===")
    main()
