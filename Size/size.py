import numpy as np

a = np.array([1,2,3,4,5], dtype= 'int32')
b = np.array([[1,2,3],
              [4,5,6]])

print(a.itemsize)
print(b.itemsize)

print()
# Totla Size
print(a.nbytes)
print(b.nbytes)