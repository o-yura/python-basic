# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита
# они стоят и сколько между ними находится букв.

# ссылка на блок-схему
# https://drive.google.com/file/d/1yUF1Vn7mPdjWqvhsG0K4wm6CuXAFELnH/view?usp=sharing


symbol1 = input('Введите первый символ ')
symbol2 = input('Введите второй символ ')

symbols = 'abcdefghijklmnopqrstuvwxyz'

number1 = symbols.find(symbol1.lower()) + 1
print('Символ {} имеет номер в алфавите {}'.format(symbol1, number1))

number2 = symbols.find(symbol2.lower()) + 1
print('Символ {} имеет номер в алфавите {}'.format(symbol2, number2))

diff = abs(number2 - number1) - 1
print('Между символами имеются {} букв'.format(diff))
