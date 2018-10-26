# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.

# год, номер которого кратен 400, — високосный;
# остальные годы, номер которых кратен 100, — невисокосные;
# остальные годы, номер которых кратен 4, — високосные.

# ссылка на блок-схему
# https://drive.google.com/file/d/1DY74iiopPwu8tAeOFsLAhXsokS2gMx61/view?usp=sharing

year = int(input('Введите год: '))

if year % 400:
    if year % 100:
        if year % 4:
            print('Год невисокосный')
        else:
            print('Год високосный')
    else:
        print('Год високосный')
else:
    print('Год високосный')
