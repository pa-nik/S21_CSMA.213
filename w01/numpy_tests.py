# some examples of using numpy arrays
import numpy as np

print('convert python list to numpy array:')
a = np.array([1, 4, 2, 5, 3])
print(a)

print('numpy array filled with 10 zeroes of type integer:')
a = np.zeros(10, dtype=int)
print(a)

print('3x5 array filled with ones of type float:')
a = np.ones((3, 5), dtype=float)
print(a)

print('array of 5 values linearly spaced between 0 and 1:')
a = np.linspace(0, 1, 5)
print(a)

# create 2 numpy arrays from python lists
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print('2 numpy arrays:')
print(x)
print(y)

print('add 2 arrays:')
print(x+y)
print(np.add(x,y))  # same result as above

print('multiply an array by 2:')
print(x*2)
print(np.multiply(x,2))  # same result as above