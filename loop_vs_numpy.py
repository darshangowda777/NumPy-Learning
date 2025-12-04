#using loops
import time

N = 1000000
py_list = list(range(N))

start = time.time()
result_py = []
for x in py_list:
    result_py.append(x * x)
end = time.time()

print("Python loop time:", end - start, "seconds")


#using numpy
import numpy as np
import time

N = 1000000
np_arr = np.arange(N)

start = time.time()
result_np = np_arr * np_arr   # vectorized operation
end = time.time()

print("NumPy vectorization time:", end - start, "seconds")

