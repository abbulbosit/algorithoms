import time
from datetime import datetime
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(data)
data_1 = int(input("Enter a number: "))
print(f"{datetime.now()} sikl boshlanish vaqti")
sikl = 0
for i in data:
    time.sleep(1)
    sikl += 1
    if i == data_1:
        print(f"{i} topildi")
        print(f"{sikl} ta siklda")
        print(f"{datetime.now()}  tugash vaqi")

