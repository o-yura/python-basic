# 4. Написать программу, которая генерирует в указанных пользователем границах:
#
#     случайное целое число;
#     случайное вещественное число;
#     случайный символ. Для каждого из трех случаев пользователь задает свои границы диапазона.
#   Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
#   Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

# ссылка на блок-схему
# https://drive.google.com/file/d/1Cdrwe8A49uO8izk28zSpkVrc28n1F-R9/view?usp=sharing

import random

# 1
r_int1 = int(input('Введите первое граничное целое число '))
r_int2 = int(input('Введите второе граничное целое число '))

r_res1 = random.randint(r_int1, r_int2)
print('Случайное число в диапозоне {} - {}: {}'.format(r_int1, r_int2, r_res1))

# 2
r_fl1 = float(input('Введите первое граничное вещественное число '))
r_fl2 = float(input('Введите второе граничное вещественное число '))

r_res2 = random.uniform(r_fl1, r_fl2)
print('Случайное число в диапозоне {} - {}: {}'.format(r_fl1, r_fl2, r_res2))

# 3
r_sym1 = input('Введите первый граничный символ ')
r_sym2 = input('Введите второй граничное символ ')

symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

r_s1 = symbols.find(r_sym1)
r_s2 = symbols.find(r_sym2)
r_res3 = random.randint(r_s1, r_s2)
r_res4 = symbols[r_res3]
print('Случайный символ в диапозоне {} - {}: {}'.format(r_sym1, r_sym2, r_res4))
