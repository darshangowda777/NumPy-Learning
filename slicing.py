import numpy as np

# general format of slicing -> [start : stop : step]

#slicing in 1D array
a = np.array([10, 20, 30, 40, 50, 60])

print(a[1:4])   #[20 30 40]
print(a[0:6:2])  #slicing with step
print(a[:3])     #slicing from start
print(a[2:])     #slicing till end

#slicing in 2D array
b = np.array([[10,20,30],
              [40,50,60],
              [70,80,90]])

print(b[0:2, 1:3])
print(b[:, 0])  # first column
print(b[1, 0:2])  # row 1, col 0–1 
print(b[:, 0])  # Take full rows, specific column
print(b[1, 0:2])  # Take specific row, range of columns

#slicing in 3D array
a = np.array([
    [[1, 2], [3, 4]],       
    [[5, 6], [7, 8]]       
])

#slice all blocks and columns in row1
print(a[:, 1, :])

#Slice only block 0, all rows, column 0
print(a[0,:,0])














