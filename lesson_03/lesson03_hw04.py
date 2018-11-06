# 4. Определить, какое число в массиве встречается чаще всего.

data = [5, 2, 3, 5, 0, 4, 13, 34, 65, 4, 8, 45, 34, 4]
spam_data = {}
index = 0
number = 0
for i in data:
    if spam_data.get(i):
        spam_data[i] += 1
    else:
        spam_data[i] = 1

max_dig = 0
max_val = 0
for i, y in spam_data.items():
    if y > max_val:
        max_val = y
        max_dig = i

print(max_dig)
