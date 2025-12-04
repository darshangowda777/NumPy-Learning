import numpy as np

#1 np.array() — This converts Python lists, tuples, or nested lists into NumPy arrays.
a = np.array([1, 2, 3, 4])
print(a)
c = np.array([[[1,2], [3,4]],[[5,6], [7,8]]])
print(c)

#2 np.arange() — Similar to Python’s range() but returns arrays, not lists.
#syntax - np.arange(start, stop, step)
print(np.arange(0, 10))         # 0 to 9
print(np.arange(1, 10, 2))      # odd numbers
print(np.arange(10, 1, -2))     # reverse direction

