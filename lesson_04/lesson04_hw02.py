# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Первый - использовать алгоритм решето Эратосфена.
# Второй - без использования "решета".
# Проанализировать скорость и сложность алгоритмов.

import cProfile


# Вариант 1

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


# print(get_dig(68))


# Вариант 2

def get_dig2(n):
    lim_nums = 0x7fffffff
    list = []
    result = 0
    for i in range(2, lim_nums):
        for j in list:
            if i % j == 0:
                break
        else:
            if n > 0:
                list.append(i)
                n -= 1
            else:
                result = j
                break
    return result


# print(get_dig2(68))

# cProfile.run('get_dig(1500)')
# cProfile.run('get_dig2(1500)')
