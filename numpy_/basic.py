import numpy as np

py_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
np_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(type(np_array))

np_multi = np_array.reshape(3, 3)
print(np_multi)
