# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0)
# и 2 нечетные (3 и 5).

# сылка на блок-схему
# https://drive.google.com/file/d/1Fmr2zThT7H9T3t1F-uTJ79EULK2JbuTG/view?usp=sharing

number = int(input('Введите натуральное число: '))
even = 0
odd = 0

while number:
    dig = number % 10
    number = number // 10
    if dig % 2:
        odd += 1
    else:
        even += 1

print('В числе цифры: {} - четные, {} - нечетные'.format(even, odd))
