# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться,
# больше или меньше загаданного введенное пользователем число.
# Если за 10 попыток число не отгадано, то вывести его.

# ссылка на болк-схему
# https://drive.google.com/file/d/1v6WWf-WxUW2WVsE-Yw6jDd-dQht7o0kq/view?usp=sharing

import random

ATTEMPTS = 10
i = 0

number = random.randint(0, 100)

while True:
    remain = ATTEMPTS - i
    if remain:
        print('У вас осталось {} попыток'.format(remain))
        user_number = int(input('Введите число: '))
        if user_number == number:
            print('Вы угадали!')
            break
        elif user_number > number:
            print('Загаданное число - меньше')
        else:
            print('Загаданное число - больше')
        i += 1
    else:
        print('Вы проиграли!')
        print('Загаданное число: ', number)
        break
