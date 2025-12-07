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

#3 np.linspace() — Generate exact number of values 
print(np.linspace(0,1,5)) #generates 5 numbers between 0 and 1 with even spacing between numbers
print(np.linspace(10,98,10))#generates 10 numbers between 10 and 98 with even spacing between numbers

#4 np.zeros() — Create array filled with 0s (Useful for initialization)
print(np.zeros(3))

#multidimensional 
print(np.zeros((4,7), ))
print(np.zeros((3,5,8),dtype=int))

#5 np.ones() — Create array filled with 1s (Useful for initialization)
print(np.ones(3))
print(np.ones((2,3), ))

#6 Random Arrays — Important for ML & testing (NumPy random module helps generate arrays with random values)

#Random float numbers between 0 and 1
r1 = np.random.rand(3)
print(r1)

#Random numbers from normal distribution(mean=0 and SD=1)
r2 = np.random.randn(5)
print(r2)

#Random integers
#syntax:np.random.randint(low, high=None, size=None, dtype=int)
r3 = np.random.randint(1,10,size=(5,5))
print(r3)

#Set random seed (important for reproducibility)
'''Controls the randomness in NumPy
Without a seed → every run gives different random numbers.
With a seed → same random numbers every time'''

np.random.seed(42)
print(np.random.rand(3))


