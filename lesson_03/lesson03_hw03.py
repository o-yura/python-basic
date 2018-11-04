# 3. В массиве случайных целых чисел поменять местами минимальный и
# максимальный элементы.

data = [5, 2, 3, 5, 0, 4, 13, 34, 65, 4, 8, 45]
min = 0
max = 0
for i in data:
    if i < min:
        min = i
    elif i > max:
        max = i

index_min = data.index(min)
index_max = data.index(max)
data[index_min] = max
data[index_max] = min
print(data)
