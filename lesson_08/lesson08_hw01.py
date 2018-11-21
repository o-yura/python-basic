# 1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть дана строка S длиной N. Например, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.
# Для решения задачи рекомендую воспользоваться алгоритмом sha1
# из модуля hashlib или встроенную функцию hash()

import hashlib
from random import randint

N = 100

def gen_string(n):
    string = [chr(randint(97, 122)) for _ in range(n)]
    string = ''.join(string)
    return string

for i in range(N - 1):
    for j in range(N - )


print(gen_string(N))
