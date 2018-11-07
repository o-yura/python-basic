# 1. Проанализировать скорость и сложность одного - трёх любых
# алгоритмов, разработанных в рамках домашнего задания первых трех уроков.


# Выбрано задание 5 урока 3.
#
# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random
import cProfile

# Выводим генерации массива в отдельную функцию
def gen_list(n):
    data = [random.randint(-1000, 1000) for _ in range(n)]
    return data

# Вариант 1.
# Обработки массива в один проход общим методом
def max_unit(n):
    data = gen_list(n)

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

    if not trigger:
        return max_dig, index
    else:
        return False

# Результаты timeit n=100
# max_unit(100)"
# 100 loops, best of 3: 250 usec per loop
# max_unit(1000)"
# 100 loops, best of 3: 2.49 msec per loop
# max_unit(10000)"
# 100 loops, best of 3: 24.5 msec per loop


# cProfile.run('max_unit(100000)') - 502376 function calls in 3.307 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.014    0.014    3.304    3.304 lesson04_hw01.py:17(max_unit)

# cProfile.run('max_unit(1000000)') - 5023604 function calls in 32.821 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.150    0.150   34.735   34.735 lesson04_hw01.py:17(max_unit)

# cProfile.run('max_unit(2000000)') - 10046782 function calls in 66.058 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.287    0.287   65.996   65.996 lesson04_hw01.py:17(max_unit)

# Вариант 2. Обработка массива встроенными функциями max, index
# и созданием промежуточного массива генератором

def max_unit2(n):
    data = gen_list(n)
    data2 = [i for i in data if i < 0]
    max_dig = max(data2)

    if max_dig < 0:
        return max_dig, data.index(max_dig)
    else:
        return False

# Результаты timeit n=100
# max_unit2(100)
# 100 loops, best of 3: 259 usec per loop
# max_unit2(1000)
# 100 loops, best of 3: 2.54 msec per loop
# max_unit2(10000)"
# 100 loops, best of 3: 25.2 msec per loop


# cProfile.run('max_unit2(100000)') - 502396 function calls in 3.300 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    3.298    3.298 lesson04_hw01.py:54(max_unit2)
#      1    0.002    0.002    0.002    0.002 {built-in method builtins.max}
#      1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

# cProfile.run('max_unit2(1000000)') - 5023419 function calls in 32.415 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000   36.574   36.574 lesson04_hw01.py:50(max_unit2)
#      1    0.021    0.021    0.021    0.021 {built-in method builtins.max}
#      1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

# cProfile.run('max_unit2(2000000)') - 10047028 function calls in 63.268 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000   63.198   63.198 lesson04_hw01.py:54(max_unit2)
#      1    0.037    0.037    0.037    0.037 {built-in method builtins.max}
#      1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

# Выводы:
# 1.
# Сложность обоих алгоритмов линейная.
# 2.
# Время отработки примерно одинаково, т.к. основное время
# затрачивается на генерацию массива, которая в обоих случаях одна и та же.
# 3.
# Встроенные функции max, index в сумме работают более чем в 7 раз быстрее интерпретируемой реализации.
# Встроенная функция index не "ресурсозатратна".