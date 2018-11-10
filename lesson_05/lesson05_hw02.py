# -*- coding: utf-8 -*-
# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
#
# Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’].
# Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

LIST_HEX = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')


def hex_dec(hex_num):
    hex_list = deque(hex_num)
    hex_list.reverse()
    dec_sum = 0
    mult = 0
    for i in hex_list:
        num_index = LIST_HEX.index(i.upper())
        if mult != 0:
            dec_sum += num_index * (16 ** mult)
        else:
            dec_sum += num_index
        mult += 1
    return dec_sum


def dec_hex(dec_num):
    list_num = []

    whole = dec_num // 16
    remain = dec_num % 16

    while whole != 0 or remain != 0:
        if whole > 15:
            list_num.append(LIST_HEX[remain])
            remain = whole % 16
            whole = whole // 16
        else:
            list_num.append(LIST_HEX[remain])
            list_num.append(LIST_HEX[whole])
            whole = 0
            remain = 0

    result = deque(list_num)
    result.reverse()
    return list(result)


# Сохраняем введенные данные в списки согласно заданию
input_num1 = list(input('Введите первое шестнадцатиричное число: '))
input_num2 = list(input('Введите второе шестнадцатиричное число: '))

print('Первое число: ', input_num1)
print('Второе число: ', input_num2)

num1_dec = hex_dec(input_num1)
num2_dec = hex_dec(input_num2)

print('Сумма чисел равна: ', dec_hex(num1_dec + num2_dec))
print('Произведение чисел равно: ', dec_hex(num1_dec * num2_dec))
