# 3. Массив размером 2m + 1, где m – натуральное число,
# заполнен случайным образом. Найти в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы,
# в другой – не больше ее.

MIN_INT = -1000
MAX_INT = 1000

from random import randint


def gen_array(n):
    array = [randint(MIN_INT, MAX_INT) for _ in range(n)]
    return array


# Находим средний элемент (медиану) отрезанием концев массива

def find_median(data):
    spam_data = data.copy()
    while len(spam_data) != 1:
        spam_max = -float('inf')
        spam_min = float('inf')
        for i in spam_data:
            if i > spam_max:
                spam_max = i
            if i < spam_min:
                spam_min = i
        spam_data.remove(spam_min)
        spam_data.remove(spam_max)

    return spam_data[0]


m = int(input('Введите переменную m: '))
array = gen_array(2 * m + 1)
print('Массив 2m + 1:')
print(array)
print('Медиана массива:', find_median(array))
