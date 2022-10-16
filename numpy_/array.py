import numpy as np

result = np.array([1, 3, 5, 7, 9])

result = np.arange(1, 10)
result = np.arange(10, 100)
result = np.zeros(10)
result = np.ones(10)
result = np.linspace(0, 100, 5)
result = np.linspace(0, 5, 5)
result = np.random.randint(0, 10)
result = np.random.randint(20)
result = np.random.randint(1, 10, 3)
result = np.random.rand(5)
result = np.arange(50)
result = result.reshape(5, 10)
result = np.random.randint(10, 100, 10)

print(result)
print(result.max())
print(result.mean())
print(result.argmax())
print(result.argmin())

# print(result.sum(axis=1))
# print(result.sum(axis=0))
