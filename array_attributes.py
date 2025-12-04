import numpy as np

#1 shape – tells structure of array that defines number of rows and columns
a = np.array([1, 2, 3, 4])
print(a.shape)

b = np.array([[1, 2, 3],[4, 5, 6]])
print(b.shape)

c = np.array([[[1,2], [3,4]],[[5,6], [7,8]]])
print(c.shape)

#2 ndim – Number of Dimensions (tells how many axes the array has)
print(a.ndim)  # 1D
print(b.ndim)  # 2D
print(c.ndim)  # 3D

#3 dtype – dtype shows what type of data that array stores
x = np.array([1, 2, 3])
print(x.dtype)

y = np.array([1, 2, 3.5])
print(y.dtype)

#4 size – Total Number of Elements in the Array
b = np.array([[1,2,3],[4,5,6]])
print(b.size)

#5 astype() - Type conversion

#int -> float
a = np.array([1, 2, 3])
b = a.astype(float)
print(b.dtype)

#float -> int
c = np.array([1.5, 2.8, 9.2])
d = c.astype(int)
print(d.dtype)

#str -> int
s = np.array(["1", "2", "3"])
r = s.astype(int)
print(r.dtype)