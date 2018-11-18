# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный
# массив, заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

from random import random
from collections import Iterable

MAX_INT = 50


def gen_array(n):
    array = [random() * MAX_INT for _ in range(n)]
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


array = gen_array(11)
print('Исходный массив:')
print(array)
new_array = merge_sort(array)
print('Отсортированный массив:')
print(new_array)

# Результаты:
#
# Исходный массив:
# [35.87464634705782, 23.81065434224246, 29.972207785755316, 24.59432405845923, 29.576510831554042, 38.31581470711219, 39.137254456119656, 22.013156619107647, 20.098824813154398, 5.9306007499425935, 36.27858111014765]
#
# Промежуточные данные из print-а строки 59
#
# ** [[23.81065434224246, 35.87464634705782], [24.59432405845923, 29.972207785755316], [29.576510831554042, 38.31581470711219], [22.013156619107647, 39.137254456119656], [5.9306007499425935, 20.098824813154398], 36.27858111014765]
# ** [[23.81065434224246, 24.59432405845923, 29.972207785755316, 35.87464634705782], [22.013156619107647, 29.576510831554042, 38.31581470711219, 39.137254456119656], [5.9306007499425935, 20.098824813154398, 36.27858111014765]]
# ** [[22.013156619107647, 23.81065434224246, 24.59432405845923, 29.576510831554042, 29.972207785755316, 35.87464634705782, 38.31581470711219, 39.137254456119656], [5.9306007499425935, 20.098824813154398, 36.27858111014765]]
# ** [[5.9306007499425935, 20.098824813154398, 22.013156619107647, 23.81065434224246, 24.59432405845923, 29.576510831554042, 29.972207785755316, 35.87464634705782, 36.27858111014765, 38.31581470711219, 39.137254456119656]]
#
# Отсортированный массив:
# [5.9306007499425935, 20.098824813154398, 22.013156619107647, 23.81065434224246, 24.59432405845923, 29.576510831554042, 29.972207785755316, 35.87464634705782, 36.27858111014765, 38.31581470711219, 39.137254456119656]
