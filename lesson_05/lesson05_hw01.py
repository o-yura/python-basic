# -*- coding: utf-8 -*-
# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего
# и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
#
# Примечание: 4 квартала - это 4 разных прибыли ;-)

from collections import namedtuple


# Функция ввода данных
def input_data(size):
    for _ in range(size):
        name = input('Введите название предприятия: ')
        print('Ввод данных по предприятию', name)
        profit_1 = float(input('Введите прибыль за первый квартал: '))
        profit_2 = float(input('Введите прибыль за второй квартал: '))
        profit_3 = float(input('Введите прибыль за третий квартал: '))
        profit_4 = float(input('Введите прибыль за четвертый квартал: '))

        units.append(Company(name, profit_1, profit_2, profit_3, profit_4))


# Функция вычисления средней квартальной прибыли предприятия за год
def calc_midle(unit):
    size_1 = unit.profit_1
    size_2 = unit.profit_2
    size_3 = unit.profit_3
    size_4 = unit.profit_4
    midle = (size_1 + size_2 + size_3 + size_4) / 4
    return midle


Company = namedtuple('Company', 'name, profit_1, profit_2, profit_3, profit_4')

# Список компаний
units = []

# Словарь для хранения среднегодовых прибылей компаний
spam_data = {}

size = int(input('Введите количество предприятий: '))
input_data(size)

gl_midle = 0

# Вычисляем среднюю квартальную прибыль предприятий
# и набиваем словарь spam_data информацией по каждому предприятию
for i in units:
    local_midle = calc_midle(i)
    gl_midle += local_midle
    spam_data[i.name] = local_midle

# Вычисляем среднюю прибыль всех предприятий
midle = gl_midle / size
print('Средняя квартальная прибыль всех предприятий: ', midle)

# Список компаний с прибылью больше среднего
list_more = [name for name, value in spam_data.items() if value > midle]

# Список компаний с прибылью меньше среднего
list_less = [name for name, value in spam_data.items() if value < midle]

print('Список предприятий с прибылью выше среднего:')
for name in list_more:
    print('\t -', name)

print('Список предприятий с прибылью ниже среднего:')
for name in list_less:
    print('\t -', name)
