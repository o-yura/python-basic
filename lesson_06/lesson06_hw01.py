# 1. Подсчитать, сколько было выделено памяти под переменные в ранее
# разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее
# эффективным использованием памяти.
# Для анализа возьмите любые 1-3 ваших программы.
# Результаты анализа вставьте в виде комментариев к коду.
#
# P.S. Напишите в комментариях версию Python и разрядность ОС.

import random
import sys
from collections import Iterable
from collections import Counter


# Универсальная функция подсчета использования памяти списка переменных
def calc_size(var_list):
    def _get_no_iter(unit):
        unit_type = type(unit)
        unit_size = sys.getsizeof(unit)

        spam_sizes.append(unit_size)

        # print(unit, unit_type, unit_size)

        if isinstance(unit, Iterable):
            if unit_type is dict:
                for i, j in unit.items():
                    _get_no_iter(i)
                    _get_no_iter(j)
            elif unit_type is not str:
                for i in unit:
                    _get_no_iter(i)

    spam_sizes = []
    _get_no_iter(var_list)
    return sum(spam_sizes)


# Выбрано задание 4 урока 3.
# Определить, какое число в массиве встречается чаще всего.

# Вариант 1. Перебором, общим методом.

def get_max_1(n):
    data = [random.randint(0, 10) for _ in range(n)]
    spam_data = {}
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

    # Сбор информации по используемым переменным
    var_list.append(locals())

    return max_dig


# Вариант 2. Используем collections.

def get_max_2(n):
    data = [random.randint(0, 10) for _ in range(n)]
    spam_data = Counter(data)

    # Сбор информации по используемым переменным
    var_list.append(locals())

    return spam_data.most_common(1)[0][0]


var_list = []
print('Решение задачи вариантом 1:')
print('Результат:', get_max_1(10))
print(var_list)
print('Под переменные выделено:', calc_size(var_list), 'байт памяти')
del var_list

var_list = []
print('Решение задачи вариантом 2:')
print('Результат:', get_max_2(10))
print(var_list)
print('Под переменные выделено:', calc_size(var_list), 'байт памяти')
del var_list

### Python 3.6.6 x86_64
#
# Результат выполнения программ:
#
# Решение задачи вариантом 1:
# Результат: 3
# [{'y': 1, 'max_val': 2, 'max_dig': 3, 'i': 0, 'spam_data': {4: 1, 3: 2, 9: 2, 10: 2, 7: 1, 1: 1, 0: 1}, 'data': [4, 3, 3, 9, 10, 10, 7, 9, 1, 0], 'n': 10}]
# Под переменные выделено: 2197 байт памяти
#
# Решение задачи вариантом 2:
# Результат: 10
# [{'spam_data': Counter({10: 3, 8: 2, 5: 2, 6: 1, 4: 1, 3: 1}), 'data': [8, 8, 10, 10, 5, 10, 6, 5, 4, 3], 'n': 10}]
# Под переменные выделено: 1549 байт памяти

# Краткий анализ
#
# Во втором варианте решения под переменные выделяется меньше памяти,
# в связи с их меньшим количеством.
# В первом варианте используются промежуточные переменные для перебора данных,
# подсчета и поиска наибольшего значения.
# Во втором варианте эти задачи решаются возможностями встроенных функций collections.