# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

# ссылка на блок-схему
# https://drive.google.com/file/d/1EsMEZXP1s4y6Y0cy3OmPlp1CtW_m-jJg/view?usp=sharing

n = int(input('Введите количество элементов ряда: '))
summ = 0
unit = 1
i = 0
while i < n:
    summ = summ + unit
    unit = unit * -0.5
    i += 1

print(summ)
