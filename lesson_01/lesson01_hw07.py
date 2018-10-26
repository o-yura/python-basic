# 7. По длинам трех отрезков, введенных пользователем, определить возможность
# существования треугольника, составленного из этих отрезков.
# Если такой треугольник существует, то определить,
# является ли он разносторонним, равнобедренным или равносторонним.

# ссылка на блок-схему
# https://drive.google.com/file/d/1Bs7BJSiIz2tTfT3ECyHIgGCVbHyzggto/view?usp=sharing

side1 = float(input('Введите длину первой стороны: '))
side2 = float(input('Введите длину второй стороны: '))
side3 = float(input('Введите длину третьей стороны: '))

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    if side1 == side2 == side3:
        print('Треугольник равносторонний')
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')
else:
    print('Треугольник построить не возможно')