'''NumPy (Numerical Python) is the core library for numerical and scientific computing in Python.

Why NumPy is used:
                  1.Fast mathematical operations
                  2.Efficient storage of large datasets
                  3.Used by Pandas, Matplotlib, Scikit-learn, TensorFlow, PyTorch
                  4.Supports vectorization (removes Python loops → much faster)

Provides tools for:
                  1.Linear algebra
                  2.Random number generation
                  3.Statistics
                  4.Transformations & reshaping
                  5.Broadcasting computational patterns'''

#installation check
import numpy as np
print(np.__version__)

#array creation
arr1 = np.array([1,2,3,4])
print(arr1)
print(type(arr1))

#2D-array
arr2 = np.array([[1, 2, 3],[4, 5, 6]])
print(arr2)

#3D-array
arr3 = np.array([ [[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]] ])
print(arr3)

#attributes of 3D-array
print(arr3.shape)
print(arr3.ndim)
print(arr3.dtype)
