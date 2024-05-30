
import time
from datetime import datetime

data = list(set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))


data_l = len(data) - 1
data.sort()
print(data)

target = int(input("Target: "))
low = 0
count = 0
print(datetime.now())
while True:
    time.sleep(1)
    count += 1
    middle = (data_l + low) // 2
    if data[middle] < target:  # false
        low = middle + 1
    elif data[middle] == target:
        print(target)
        print(f"Count {count}")
        break

    else:
        data_l = middle

print(datetime.now())




