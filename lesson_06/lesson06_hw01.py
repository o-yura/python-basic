# -*- coding: utf-8 -*-
# 1. Подсчитать, сколько было выделено памяти под переменные в ранее
# разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее
# эффективным использованием памяти.
# Для анализа возьмите любые 1-3 ваших программы.
# Результаты анализа вставьте в виде комментариев к коду.
#
# P.S. Напишите в комментариях версию Python и разрядность ОС.

from random import randint
from sys import getsizeof
from collections import Iterable
from collections import Counter


# Универсальная функция подсчета использования памяти списка переменных
def calc_size(var_list):
    def _get_no_iter(unit):
        unit_type = type(unit)
        unit_size = getsizeof(unit)

        spam_sizes.append(unit_size)

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


# Вывод статистической информации по переменным
def output_info(data):
    print('Список переменных:')
    print('\t{0:>3} {1:<12} {2:<10}'.format('NN', 'Название', 'Тип'))
    for i in data:
        j = 0
        for key, value in i.items():
            j += 1
            print('\t{0:>3} {1:<12} {2:<10}'.format(j, key, str(type(value))))


# Выбрано задание 4 урока 3.
# Определить, какое число в массиве встречается чаще всего.

# Вариант 1. Перебором, общим методом.

def get_max_1(n):
    data = [randint(0, 10) for _ in range(n)]
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
    data = [randint(0, 10) for _ in range(n)]
    spam_data = Counter(data)

    # Сбор информации по используемым переменным
    var_list.append(locals())

    return spam_data.most_common(1)[0][0]


### Запускаем первый вариант
# Временный список для сбора переменных в разных функциях
var_list = []
print('Решение задачи вариантом 1:')
print('Результат:', get_max_1(10))
output_info(var_list)
# Вычитаем размер служебного списка (var_list) для сбора информации
print('Под переменные выделено:', calc_size(var_list) - getsizeof(var_list), 'байт памяти')
del var_list

print()

### Запускаем второй вариант
var_list = []
print('Решение задачи вариантом 2:')
print('Результат:', get_max_2(10))
output_info(var_list)
print('Под переменные выделено:', calc_size(var_list) - getsizeof(var_list), 'байт памяти')
del var_list

### Python 3.6.6 x86_64
#
# Результат выполнения программ:
#
# Решение задачи вариантом 1:
# Результат: 1
# Список переменных:
# 	 NN Название     Тип
# 	  1 y            <class 'int'>
# 	  2 max_val      <class 'int'>
# 	  3 max_dig      <class 'int'>
# 	  4 i            <class 'int'>
# 	  5 spam_data    <class 'dict'>
# 	  6 data         <class 'list'>
# 	  7 n            <class 'int'>
# Под переменные выделено: 2113 байт памяти
#
# Решение задачи вариантом 2:
# Результат: 2
# Список переменных:
# 	 NN Название     Тип
# 	  1 spam_data    <class 'collections.Counter'>
# 	  2 data         <class 'list'>
# 	  3 n            <class 'int'>
# Под переменные выделено: 1509 байт памяти

#
# Краткий анализ
#
# Во втором варианте решения под переменные выделяется значительно меньше памяти,
# в связи с их меньшим количеством.
# В первом варианте используются промежуточные переменные для перебора данных,
# подсчета и поиска наибольшего значения.
# Во втором варианте эти задачи решаются возможностями встроенных функций collections.
