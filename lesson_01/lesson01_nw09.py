# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

# ссылка на блок-схему
# https://drive.google.com/file/d/1Bzxiy5bJdbszrM1-X49fdtPEkWuNm68p/view?usp=sharing

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = float(input('Введите третье число: '))

if b < a < c:
    print('Среднее число: ', a)
elif a < b < c:
    print('Среднее число: ', b)
else:
    print('Среднее число: ', c)
