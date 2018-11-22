# 1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть дана строка S длиной N. Например, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.
# Для решения задачи рекомендую воспользоваться алгоритмом sha1
# из модуля hashlib или встроенную функцию hash()

import hashlib
from random import randint


def gen_string(n):
    string = [chr(randint(97, 122)) for _ in range(n)]
    string = ''.join(string)
    return string


def hash_calc(string):
    spam_data = []
    n = len(string)
    for i in range(1, n):
        for j in range(0, n - i + 1):
            sub_string = string[j:j + i]
            h_string = hashlib.sha1(sub_string.encode()).hexdigest()
            if spam_data.count(h_string) == 0:
                spam_data.append(h_string)
    return len(spam_data)


# spam_string = 'papa'
spam_string = gen_string(100)
print('В строке: ', spam_string)
print('Количество различных подстрок: ', hash_calc(spam_string))
