# 1. Написать программу, которая будет складывать, вычитать,
# умножать или делить два числа. Числа и знак операции вводятся
# пользователем. После выполнения вычисления программа не должна
# завершаться, а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0'
# в качестве знака операции. Если пользователь вводит неверный
# знак (не '0', '+', '-', '*', '/'), то программа должна сообщать
# ему об ошибке и снова запрашивать знак операции. Также сообщать
# пользователю о невозможности деления на ноль, если он ввел 0
# в качестве делителя.

# ссылка на блок-схему
# https://drive.google.com/file/d/1d7d-aJB1XpzeeiXnq1klXiypvc1ErAYk/view?usp=sharing

while True:
    print('Введите математическую операцию ("+", "-", "*", "/")')
    print('или 0 - для завершения программы')
    act = input('# ')

    if act == '0':
        print('Завершение программы!')
        break

    if act == '+' or act == '-' or act == '*' or act == '/':
        dig1 = float(input('Введите первое число: '))
        dig2 = float(input('Введите второе число: '))

        if act == '/' and dig2 == 0:
            print('Деление на ноль не возможно!')
        else:
            result = 0
            if act == '+':
                result = dig1 + dig2
            elif act == '-':
                result = dig1 - dig2
            elif act == '*':
                result = dig1 * dig2
            else:
                result = dig1 / dig2
            print('Результат вычисления: ', result)
    else:
        print('Введена недопустимая операция!')

    input('Нажмите Enter для продолжения')
