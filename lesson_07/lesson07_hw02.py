# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный
# массив, заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

from random import randint
from collections import Iterable

MIN_INT = 0
MAX_INT = 49


def gen_array(n):
    array = [randint(MIN_INT, MAX_INT) for _ in range(n)]
    return array


def merge_sort(data):
    def _merge_pair(first, second):
        result = []
        if isinstance(first, Iterable):
            if not isinstance(second, Iterable):
                second = [second]
            for i in second:
                index_first = 0
                for j in first:
                    if i < j:
                        first.insert(index_first, i)
                        break
                    elif index_first == len(first) - 1:
                        first.append(i)
                        break
                    index_first += 1
            result = first
        else:
            if first < second:
                result = [first, second]
            else:
                result = [second, first]
        return result

    def _mix_engine(data):
        spam_size = len(data)
        while spam_size != 1:
            spam_data = []
            j = 0
            trigger = True
            for i in range(spam_size):
                if j % 2 != 0:
                    unit2 = data[i]
                    unit = _merge_pair(unit1, unit2)
                    trigger = False
                    spam_data.append(unit)
                else:
                    unit1 = data[i]
                    trigger = True
                j += 1
            if trigger:
                spam_data.append(unit1)
            spam_size = len(spam_data)
            # print('**', spam_data)
            return _mix_engine(spam_data)
        return data[0]

    return _mix_engine(data)


array = gen_array(21)
print('Исходный массив:')
print(array)
new_array = merge_sort(array)
print('Отсортированный массив:')
print(new_array)


# Результат:
# Исходный массив:
# [46, 49, 10, 39, 29, 8, 10, 41, 47, 2, 15, 38, 8, 35, 3, 21, 43, 12, 36, 37, 11]
# Отсортированный массив:
# [2, 3, 8, 8, 10, 10, 11, 12, 15, 21, 29, 35, 36, 37, 38, 39, 41, 43, 46, 47, 49]
#
#  Промежуточные значения через print в строке 60
# [46, 49, 10, 39, 29, 8, 10, 41, 47, 2, 15, 38, 8, 35, 3, 21, 43, 12, 36, 37, 11]
# ** [[46, 49], [10, 39], [8, 29], [10, 41], [2, 47], [15, 38], [8, 35], [3, 21], [12, 43], [36, 37], 11]
# ** [[10, 39, 46, 49], [8, 10, 29, 41], [2, 15, 38, 47], [3, 8, 21, 35], [12, 36, 37, 43], 11]
# ** [[8, 10, 10, 29, 39, 41, 46, 49], [2, 3, 8, 15, 21, 35, 38, 47], [11, 12, 36, 37, 43]]
# ** [[2, 3, 8, 8, 10, 10, 15, 21, 29, 35, 38, 39, 41, 46, 47, 49], [11, 12, 36, 37, 43]]
# ** [[2, 3, 8, 8, 10, 10, 11, 12, 15, 21, 29, 35, 36, 37, 38, 39, 41, 43, 46, 47, 49]]
# [2, 3, 8, 8, 10, 10, 11, 12, 15, 21, 29, 35, 36, 37, 38, 39, 41, 43, 46, 47, 49]
