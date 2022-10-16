import pandas as pd

s1 = pd.Series([3, 2, 0, 1])
s2 = pd.Series([0, 3, 7, 2])

data = dict(apples=s1, oranges=s2)
df = pd.DataFrame(data)

df = pd.DataFrame()

df = pd.DataFrame([1, 2, 3, 4, 5])
df = pd.DataFrame()

data = [["Ahmet", 50], ["Ali", 60], ["Yağmur", 70], ["Çınar", 80]]
df = pd.DataFrame(data, columns=["Isim", "Puan"], index=[1, 2, 3, 4], dtype=float)

dictionary = {"Isim": ["Ahmet", "Ali", "Yagmur", "Cinar"], "Puan": [50, 60, 70, 80]}
df = pd.DataFrame(dictionary)

df = pd.DataFrame(dictionary, index=[1, 2, 3, 4])

dict_list = [{"Name": "Ahmet", "Grade": 50}, {"Name": "Yagmur", "Grade": 70}, {"Name": "Ali", "Grade": 60},
             {"Name": "Cinar", "Grade": 80}]
df = pd.DataFrame(dict_list)
print(df)
