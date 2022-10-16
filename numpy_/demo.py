import numpy as np

result = np.array([10, 15, 30, 45, .60])

result = np.arange(5, 15)

result = np.arange(5, 100, 5)
result = np.zeros(10)
result = np.ones(10)
result = np.linspace(0, 100, 5)

result = np.random.randint(10, 30, 5)
result = np.random.randn(10)

result = np.random.randint(10, 50, 15).reshape(3, 5)
matris = np.random.randint(-50, 50, 15).reshape(3, 5)

rowTotal = matris.sum(axis=1)
colTotal = matris.sum(axis=0)
print(matris)
# print(rowTotal, colTotal)

result = matris.max()
result = matris.min()
result = matris.mean()

result = matris.argmax()
result = matris.argmin()
result = np.arange(10, 20)

result = result[::-1]
result = matris[0]

result = matris[1, 2]
result = matris[:, 0]
result = matris ** 2

cutler = matris[matris % 2 == 0]
print(cutler)
result = cutler[cutler > 2]
print(result)
