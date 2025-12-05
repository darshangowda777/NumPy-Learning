import numpy as np

#1 Element-wise arithmetic (vectorized operations)
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print(a + b)    
print(a * b)    
print(a - b)    
print(a / b)    

#Operations return new arrays unless you assign back or use in-place ops (+=, *=).
a = np.array([1, 2, 3])
a += 5           # modifies 'a' in-place
print(a)

#2 Broadcasting
'''Broadcasting  - NumPy operate on arrays of different shapes by virtually expanding one array to match the other — without actually copying data.
Broadcasting rules:
If the two axes are equal, they are compatible.
If one of the axes is 1, that axis is compatible — the array with dimension 1 behaves as if it were repeated along that axis.
If an axis does not exist in one array (i.e., shapes have different length), treat the missing axis as if it were size 1.
If neither condition holds for any axis (sizes differ and neither is 1), broadcasting is not possible → ValueError.'''

#broadcast to scalar
x = np.array([1,2,3])  
y = 5                  
print(x + y)           

#Broadcast 1D to 2D
row = np.array([0, 1, 2])         # shape (3,)
mat = np.array([[10,10,10],[20,20,20]])  # shape (2,3)
print(mat + row)  # row is broadcast to shape (2,3)

#higher dimensions broadcasting
'''A: (4,3,2)
   B: (3,2) -> treated as (1,3,2) and broadcast to (4,3,2)
'''

#Incompatible shapes — when it fails
'''np.ones((3,2)) + np.ones((2,3))  # shapes (3,2) vs (2,3) -> ValueError
'''

#3 Universal functions (ufuncs)
'''Ufuncs are elementwise functions implemented in C — very fast and vectorized. They cover arithmetic, trig, exponentials, logs, comparisons, and more.

Common ufuncs:

Arithmetic: np.add, np.subtract, np.multiply, np.divide, np.power
Unary math: np.sqrt, np.abs, np.negative
Exponentials & logs: np.exp, np.log, np.log10
Trigonometric: np.sin, np.cos, np.tan
Comparisons: np.greater, np.less, np.equal'''

a = np.array([1.0, 4.0, 9.0])
print(np.sqrt(a))         # [1. 2. 3.]
print(np.exp(np.array([0,1])))  # [1. 2.7182818...]

# element-wise max/min
x = np.array([1, 7, 3])
y = np.array([2, 4, 5])
print(np.maximum(x, y))   # [2 7 5]


