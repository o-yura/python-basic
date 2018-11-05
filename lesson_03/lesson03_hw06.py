# 6. В одномерном массиве найти сумму элементов, находящихся
# между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

data = [5, 2, 3, 555, 0, -4, 13, 334, -65, -4, 8, 45, 34, 4]
max_dig = 0
min_dig = 0

for i in data:
    if i > max_dig:
        max_dig = i
    if i < min_dig:
        min_dig = i

first_index = data.index(min_dig)
second_index = data.index(max_dig)
if max_dig > min_dig:
    first_index = data.index(max_dig)
    second_index = data.index(min_dig)

result = 0

for i in range(first_index + 1, second_index):
    result += data[i]

print(result)
