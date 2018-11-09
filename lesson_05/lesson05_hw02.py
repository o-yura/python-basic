# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
#
# Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’].
# Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

LIST_HEX = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')


def hex_dec(hex_num):
    hex_list = deque(hex_num)
    hex_list.reverse()
    dec_sum = 0
    mult = 0
    for i in hex_list:
        num_index = LIST_HEX.index(i.lower())
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


input_1 = 'A2'
input_2 = 'C4F'

num1_dec = hex_dec(input_1)
num2_dec = hex_dec(input_2)

sum_dec = num1_dec + num2_dec
sum_hex = dec_hex(sum_dec)

mult_dec = num1_dec * num2_dec
mult_hex = dec_hex(mult_dec)

print(sum_hex)
print(mult_hex)