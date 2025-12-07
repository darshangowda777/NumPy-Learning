import numpy as np

#1 indexing in 1D array
a = np.array([10, 20, 30, 40, 50])

#accessing elements
print(a[0])   # first element
print(a[2])   
print(a[-1])  #last element

#modify elements
a[1]=200
print(a)


#2 indexing in 2D array
b = np.array([[10, 20, 30],[40, 50, 60]])

print(b[0][1]) 
print(b[0,1])
print(b[0, :])   #access entire row
print(b[:,0])    #access entire column

#3 indexing in 3D array
c = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print(c[1,0,0]) #1->second block, 0->first row, 0->first column


#4 fancy-indexing
'''Fancy indexing = use lists or arrays inside indexing
helps extract complex patterns.'''

a = np.array([10,20,30,40,50])
idx = [0, 2, 4]   # positions
print(a[idx])

#Fancy indexing in 2D
b = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

#pick row 0 and 2
print(b[[0, 2]])

#Pick elements at (0,0), (1,1), (2,2)
print(b[[0,1,2], [0,1,2]])

#5 boolean indexing
arr = np.array([10, 25, 30, 5, 50])
print(arr[arr > 20])



