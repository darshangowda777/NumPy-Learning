import numpy as np

#np.sort():Returns a sorted COPY of the array
a = np.array([3, 1, 5, 2])
print(np.sort(a))
print(a)   # original unchanged

#2D example (axis matters)
A = np.array([[3, 1, 2],
              [6, 5, 4]])

print(np.sort(A, axis=0))  # column-wise
print(np.sort(A, axis=1))  # row-wise

#np.argsort():sort by indices
a = np.array([40, 10, 30, 20])
idx = np.argsort(a)
print(idx)
print(a[idx])

#np.unique() — Find unique values
a = np.array([1, 2, 2, 3, 3, 3])
print(np.unique(a))

#unique+counts
values, counts = np.unique(a, return_counts=True)
print(values)
print(counts)

