# -*- coding: utf-8 -*-
# 1. Подсчитать, сколько было выделено памяти под переменные в ранее
# разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее
# эффективным использованием памяти.
# Для анализа возьмите любые 1-3 ваших программы.
# Результаты анализа вставьте в виде комментариев к коду.
#
# P.S. Напишите в комментариях версию Python и разрядность ОС.


# Выбрано задание 5 урока 3.
#
# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.


from random import randint
from sys import getsizeof
from collections import Iterable

# импортируем функции обработки статистики из предыдущего исполнения

from lesson06_hw01 import calc_size
from lesson06_hw01 import output_info


# Вариант 1.
# Обработки массива в один проход общим методом
def max_unit(data):
    max_dig = 0
    trigger = True
    index = 0
    for k, i in enumerate(data):
        if i < 0:
            if trigger:
                max_dig = i
                index = k
                trigger = False
            if i > max_dig:
                max_dig = i
                index = k

    # Сбор информации по используемым переменным
    var_list.append(locals())

    if not trigger:
        return max_dig, index
    else:
        return False


# Вариант 2. Обработка массива встроенными функциями max, index
# и созданием промежуточного массива генератором

def max_unit2(data):
    data2 = [i for i in data if i < 0]
    max_dig = max(data2)

    # Сбор информации по используемым переменным
    var_list.append(locals())

    if max_dig < 0:
        return max_dig, data.index(max_dig)
    else:
        return False

if __name__ == '__main__':
    SIZE = 100
    data = [randint(-1000, 1000) for _ in range(SIZE)]

    ### Запускаем первый вариант
    # Временный список для сбора переменных в разных функциях
    var_list = []
    print('Решение задачи вариантом 1:')
    print('Результат:', max_unit(data))
    output_info(var_list)
    # Вычитаем размер служебного списка (var_list) для сбора информации
    print('Под переменные выделено:', calc_size(var_list) - getsizeof(var_list), 'байт памяти')
    del var_list

    ### Запускаем второй вариант
    var_list = []
    print('Решение задачи вариантом 2:')
    print('Результат:', max_unit2(data))
    output_info(var_list)
    print('Под переменные выделено:', calc_size(var_list) - getsizeof(var_list), 'байт памяти')
    del var_list

# Python 3.5.3 i686 (32 bit)
#
# Решение задачи вариантом 1:
# Результат: (-3, 63)
# Список переменных:
# 	 NN Название     Тип
# 	  1 index        <class 'int'>
# 	  2 i            <class 'int'>
# 	  3 max_dig      <class 'int'>
# 	  4 trigger      <class 'bool'>
# 	  5 data         <class 'list'>
# 	  6 k            <class 'int'>
# Под переменные выделено: 2339 байт памяти
#
# Решение задачи вариантом 2:
# Результат: (-3, 63)
# Список переменных:
# 	 NN Название     Тип
# 	  1 data2        <class 'list'>
# 	  2 max_dig      <class 'int'>
# 	  3 data         <class 'list'>
# Под переменные выделено: 3097 байт памяти
#
#
# Краткий анализ
#
# Под выполнение второго решения выделяется больше памяти,
# т.к. создается дополнительный промежуточный массив данных.
# В предыдущих занятиях эти алгоритмы тестировались на скорость
# и второй вариант был быстрее.
# Получились варианты со свободой выбора между
# утилизацией ресурсов памяти и скоростью выполнения задачи.
