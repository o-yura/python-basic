# 1. Отсортировать по убыванию методом «пузырька» одномерный
# целочисленный массив, заданный случайными числами на промежутке [-100; 100).
# Вывести на экран исходный и отсортированный массивы.

from random import randint

MIN_INT = -100
MAX_INT = 99


def gen_array(n):
    array = [randint(MIN_INT, MAX_INT) for i in range(n)]
    return array


def bubble_sort(n):
    array = gen_array(n)
    first_unit = 0
    last_unit = len(array) - 1
    while first_unit < last_unit:
        max_unit = 0
        max_index = 0
        for i in range(first_unit, last_unit):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
            if array[i] > max_unit:
                max_unit = array[i]
                max_index = i
        array[first_unit], array[max_index] = array[max_index], array[first_unit]
        last_unit -= 1
        first_unit += 1
        # print(array)


bubble_sort(10)
