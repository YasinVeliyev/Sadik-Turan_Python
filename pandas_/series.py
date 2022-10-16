import numpy as np
import pandas as pd

numbers = [10, 20, 30, 40, 50, 60]
pd_series = pd.Series(numbers)

letters = ["a", "b", "c", "h", "j", "k"]
pd_series = pd.Series(letters)

scalar = 5
pd_series = pd.Series(scalar, [0, 1, 2, 3, 4, 5])
pd_series = pd.Series(numbers, letters)

dictionary = {"a": 5, "b": 6, "c": 7}
pd_series = pd.Series(dictionary)

random_numbers = np.random.randint(10, 100, 6)
pd_series = pd.Series(random_numbers)

random_numbers = np.random.randint(10, 100, 6)
pd_series = pd.Series(random_numbers)

result = pd_series[0]
result = pd_series[::-1]

result = pd_series.ndim
result = pd_series.dtype
result = pd_series.shape

result = pd_series.sum()
result = pd_series.max()
result = pd_series.min()

result = pd_series * 2
result = np.sqrt(result)

result = pd_series > 50
result = pd_series % 2 == 0
result = pd_series[result]

opel2018 = pd.Series([20, 30, 40, 50], ["astra", "vectra", "corsa", "mokka"])
opel2019 = pd.Series([20, 30, 40, 50], ["astra", "zafira", "corsa", "mokka"])

print(opel2018 + opel2019)
print(result)
