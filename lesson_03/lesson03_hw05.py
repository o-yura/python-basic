# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

data = [5, 2, 3, 5, 0, -4, 13, 334, -65, -4, 8, 45, 34, 4]

max_dig = 0
trigger = True

for i in data:
    if i < 0:
        if trigger:
            max_dig = i
            trigger = False
        if i > max_dig:
            max_dig = i

if not trigger:
    print('{} в позиции {}'.format(max_dig, data.index(max_dig)))
else:
    print('Отрицательных чисел нет')
