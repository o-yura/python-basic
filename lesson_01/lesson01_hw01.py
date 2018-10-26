# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# ссылка на блок-схему
# https://drive.google.com/file/d/1XW3mBU-BalUQxI6D43Aoz7lSzS4tarJ3/view?usp=sharing

number = int(input('Введите целое трехзначное число:'))

print('Обрабатываем число', number)

dig1 = number // 100
dig2 = (number - dig1 * 100) // 10
dig3 = number - (dig1 * 100) - (dig2 * 10)

print('{} - сотен, {} - десятков, {} - единиц'.format(dig1, dig2, dig3))

summ = dig1 + dig2 + dig3
print('Сумма цифр числа равна', summ)

mult = dig1 * dig2 * dig3
print('Произведение цифр числа равна', mult)
