# 3. В массиве случайных целых чисел поменять местами минимальный и
# максимальный элементы.

data = [5, 2, 3, 5, 0, 4, 13, 34, 65, 4, 8, 45]
min_dig = 0
max_dig = 0
for i in data:
    if i < min_dig:
        min_dig = i
    elif i > max_dig:
        max_dig = i

index_min = data.index(min_dig)
index_max = data.index(max_dig)
data[index_min] = max_dig
data[index_max] = min_dig
print(data)
