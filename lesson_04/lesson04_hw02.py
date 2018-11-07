# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Первый - использовать алгоритм решето Эратосфена.
# Второй - без использования "решета".
# Проанализировать скорость и сложность алгоритмов.

def gen_sieve(n):
    sieve = [i for i in range(2, n)]
    return sieve


def add_unit(sieve):
    sieve.append(len(sieve) + 2)
    fix_digs(sieve)


def fix_digs(sieve):
    n = len(sieve)
    for i in range(2, n):
        if sieve[i] != 0:
            k = i + i
            while k < n + 2:
                print('*** k', k, '*** n', n)
                sieve[k - 2] = 0
                k += i


def get_dig(n, k=0):
    for j, i in enumerate(sieve):
        print('j', j, 'i', i)
        if i != 0:
            k += 1

            if k < n:
                add_unit(sieve)
                print(sieve)
                print('k', k, 'n', n)
                get_dig(n, k)
            else:
                return sieve[j]


sieve = gen_sieve(4)
# print(sieve)
# add_unit(sieve)
# print(sieve)
# fix_digs(sieve)
print(sieve)
print(get_dig(8))
