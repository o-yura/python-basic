# 3. Сформировать из введенного числа обратное по порядку
# входящих в него цифр и вывести на экран. Например, если
# введено число 3486, то надо вывести число 6843.

# ссылка на блок-схему
# https://drive.google.com/file/d/1Br7etzOCWARCVSA9do66tzF_1eg_xW-B/view?usp=sharing

number = int(input('Введите натуральное число: '))
revers = 0

while number:
    dig = number % 10
    number = number // 10
    revers = revers * 10 + dig

print(revers)
