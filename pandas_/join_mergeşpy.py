import pandas as pd

customers = {
    'CustomerId': [1, 2, 3, 4],
    'FirstName': ["Ahmet", "Ali", "Hasan", "Canan"],
    'LastName': ["Yılmaz", "Korkmaz", "Çelik", "Toprak"]
}

orders = {
    'OrderId': [10, 11, 12, 13],
    'CustomerId': [1, 2, 5, 7],
    'OrderDate': ['2010-07-04', '2010-08-04', '2010-07-07', '2012-07-04']
}

customers = pd.DataFrame(customers, columns=["CustomerId", "FirstName", "LastName"])
orders = pd.DataFrame(orders, columns=["OrderId", "CustomerId", "OrderDate"])

# print(customers)
# print(orders)

result = pd.merge(customers, orders, how="inner")
result = pd.merge(customers, orders, how="left")
result = pd.merge(customers, orders, how="right")
result = pd.merge(customers, orders, how="outer")
# print(result)
customersA = {
    'CustomerId': [1, 2, 3, 4],
    'FirstName': ["Ahmet", "Ali", "Hasan", "Canan"],
    'LastName': ["Yılmaz", "Korkmaz", "Çelik", "Toprak"]
}
#
customersB = {
    'CustomerId': [4, 5, 6, 7],
    'FirstName': ["Yağmur", "Çınar", "Cengiz", "Can"],
    'LastName': ["Bilge", "Turan", "Yılmaz", "Turan"]
}
#
customersA = pd.DataFrame(customersA, columns=["CustomerId", "FirstName", "LastName"])
customersB = pd.DataFrame(customersB, columns=["CustomerId", "FirstName", "LastName"])
#
result = pd.concat([customersA, customersB])
result = pd.concat([customersA, customersB], axis=1)

print(result)
