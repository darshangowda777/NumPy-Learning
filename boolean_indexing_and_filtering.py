import numpy as np

#Boolean Indexing: arr[arr > value]
'''What happens internally?

arr > 10 returns a boolean mask:
[False, True, False, True, False]'''
arr = np.array([5, 15, 8, 20, 3])
print(arr[arr > 10])

#Multiple Conditions - Use operators: & (AND), | (OR), ~ (NOT)
arr = np.array([5, 15, 8, 20, 3])
print(arr[(arr > 5) & (arr < 20)])

#Filtering 2D Arrays
A = np.array([[10, 20, 30],
              [5,  15, 25]])
print(A[A > 15])

#np.where() — Conditional Selection
#syntax - np.where(condition, value_if_true, value_if_false)
arr = np.array([10, 15, 3, 25])
result = np.where(arr > 10, "High", "Low")
print(result)

#replace the values
res = np.where(arr>10, 0,arr )
print(res)

#any() and all() — Boolean Reduction
'''any() → True if at least one element is True
   all() → True if all elements are True'''

arr = np.array([True, False, True])
print(arr.any())   
print(arr.all())   

#check any value >50
arr = np.array([10, 20, 30])
print((arr > 50).any())

#check all value >5
print((arr>5).all())

#2D any() and all() with axis
A = np.array([[1, 2, 3],
              [0, 5, 6]])
#ANY along axis=0 (column-wise check)
print((A > 0).any(axis=0))

#ALL along axis=1 (row-wise check)
print((A > 0).all(axis=1))




