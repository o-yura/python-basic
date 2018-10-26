# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

# ссылка на блок-схему
# https://drive.google.com/file/d/1r1Yjl658QKjyqqjxZIETBo4Ie885wPGz/view?usp=sharing

number = int(input('Введите номер буквы в алфавите '))

symbols = 'abcdefghijklmnopqrstuvwxyz'

if number > len(symbols):
    print('Столько букв в алфавите нет')
else:
    symbol = symbols[number - 1]
    print(symbol)
