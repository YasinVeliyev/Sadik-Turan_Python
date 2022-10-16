import numpy as np

numbers = np.array([0, 5, 10, 15, 20, 25, 50, 75, 85])

result = numbers[5]
result = numbers[-1]
result = numbers[0:3]
result = numbers[:3]
result = numbers[3:]
result = numbers[3:-1]
result = numbers[::]
result = numbers[::-2]

numbers = numbers.reshape(3, 3)
result = numbers[0][1]
result = numbers[1]
print(type(result) == type(numbers))
result = numbers[:, 1:2]
result = numbers[:, -1]

arr1 = np.arange(0, 10)
arr2 = arr1

print(numbers)
print(result)
