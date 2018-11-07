# -*- coding: utf-8 -*-
# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Первый - использовать алгоритм решето Эратосфена.
# Второй - без использования "решета".
# Проанализировать скорость и сложность алгоритмов.

import cProfile


# Вариант 1 - Решето

def gen_sieve(n):
    sieve = [i for i in range(n + 1)]
    sieve[0], sieve[1] = 0, 0
    return sieve


def fix_digs(sieve):
    n = len(sieve)
    for i in range(2, n):
        if sieve[i] != 0:
            k = i + i
            while k < n:
                sieve[k] = 0
                k += i


def add_digs(sieve, numbers):
    sieve.append(numbers)
    fix_digs(sieve)


def get_dig(n):
    sieve = gen_sieve(n)
    fix_digs(sieve)
    first_index = 2
    k = 0
    numbers = len(sieve)

    while k != n:
        for i in range(first_index, numbers):
            if sieve[i] != 0:
                k += 1
        add_digs(sieve, numbers)
        first_index = numbers
        numbers += 1

    return sieve[first_index - 1]


# print(get_dig(15))

# Результаты timeit n=100
#
# get_dig(10)
# 100 loops, best of 3: 108 usec per loop
# get_dig(100)
# 100 loops, best of 3: 21.1 msec per loop
# get_dig(200)
# 100 loops, best of 3: 119 msec per loop

# Результаты cProfile
#
# cProfile.run('get_dig(100)') - 1777 function calls in 0.029 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#    443    0.028    0.000    0.028    0.000 lesson04_hw02.py:18(fix_digs)
#    442    0.000    0.000    0.029    0.000 lesson04_hw02.py:28(add_digs)
#    444    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#    442    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# cProfile.run('get_dig(1000)') - 27689 function calls in 7.157 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#  6921    7.137    0.001    7.138    0.001 lesson04_hw02.py:18(fix_digs)
#  6920    0.006    0.000    7.146    0.001 lesson04_hw02.py:28(add_digs)
#  6922    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#  6920    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}

# cProfile.run('get_dig(2000)') - 61569 function calls in 35.066 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#  15391   35.014    0.002   35.017    0.002 lesson04_hw02.py:18(fix_digs)
#  15390    0.017    0.000   35.036    0.002 lesson04_hw02.py:28(add_digs)
#  15392    0.003    0.000    0.003    0.000 {built-in method builtins.len}
#  15390    0.003    0.000    0.003    0.000 {method 'append' of 'list' objects}


# Вариант 2 - без решета

def get_dig2(n):
    lim_nums = 0x7fffffff
    list_digs = []
    result_num = 0
    for i in range(2, lim_nums):
        for k in list_digs:
            if i % k == 0:
                break
        else:
            if n > 0:
                list_digs.append(i)
                n -= 1
            else:
                result_num = k
                break
    return result_num


# print(get_dig2(15))

# Результаты timeit n=100
#
# dig2(10)
# 100 loops, best of 3: 6.46 usec per loop
# get_dig2(100)"
# 100 loops, best of 3: 284 usec per loop
# get_dig2(200)
# 100 loops, best of 3: 1.05 msec per loop
# dig2(1000)
# 100 loops, best of 3: 27.4 msec per loop

# Результаты cProfile
#
# cProfile.run('get_dig2(100)') - 104 function calls in 0.000 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 lesson04_hw02.py:67(get_dig2)
#    100    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# cProfile.run('get_dig2(1000)') - 1004 function calls in 0.029 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.029    0.029    0.029    0.029 lesson04_hw02.py:75(get_dig2)
#   1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# cProfile.run('get_dig2(2000)') - 2004 function calls in 0.111 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.111    0.111    0.111    0.111 lesson04_hw02.py:80(get_dig2)
#   2000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}


# cProfile.run('get_dig(2000)')
# cProfile.run('get_dig2(2000)')


# Вывод
# 1. Алгоритм работы с решетом сложен и работает медленно с большими числами
# в связи с тем, что чем больше число в поиске, тем глубже
# нужно растягивать решето и его обрабатывать.
# На каждый шаг перебора числа приходится по 4 вызова обработки работы с решетом.
# Основные затраты времени расходуются на зачеркивание составных чисел.

#
# 2. Без решета, удалось собрать алгоритм с обработкой в один проход и количество
# вызовов равно порядковому номеру числа в ряде.
