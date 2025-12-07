import numpy as np

#compute mean
a = np.array([[1, 2, 3],
              [4, 5, 6]])
print(a.mean())
print(a.mean(axis=0))  # column-wise mean
print(a.mean(axis=1))  # row-wise mean

# compute sum
print(a.sum())
print(a.sum(axis=0))  # column sums
print(a.sum(axis=1))  # row sums


