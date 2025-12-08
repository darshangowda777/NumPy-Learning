import numpy as np

#reshape() —
''' Change array shape without changing data
reshape() usually returns a view, not a copy (faster)'''
a = np.array([1,2,3,4,5,6])
b = a.reshape(2,3)
print(b)

#You can use -1 to auto-compute dimension
c = a.reshape(3, -1)   # NumPy automatically finds correct dimension
print(c)

# flatten() — Always returns a COPY (1D array)
arr = np.array([[1,2,3],[4,5,6]])
print(arr.flatten())

#ravel() — Returns a VIEW when possible (preferred)
arr = np.array([[1,2,3],[4,5,6]])
print(arr.ravel())

#hstack() — Horizontal stacking (column-wise join)
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.hstack((a,b)))

#for 2D
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print(np.hstack((A,B)))

#vstack() — Vertical stacking (row-wise join)
print(np.vstack((a,b)))
#for 2D
print(np.vstack((A,B)))

#concatenate() — General stacking, most powerful
'''syntax : np.concatenate((arr1, arr2, ...), axis=0)
'''
#Example 1 — axis=0 (vertical)
np.concatenate((A, B), axis=0)

#Example 2 — axis=1 (horizontal)
np.concatenate((A, B), axis=1)

#Example 3 — 3D arrays
X1 = np.array([
    [[1, 2],
     [3, 4]],

    [[5, 6],
     [7, 8]]
])

X2 = np.array([
    [[10, 20],
     [30, 40]],

    [[50, 60],
     [70, 80]]
])
np.concatenate((X1, X2), axis=2)
