# Задание 4.
#
# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите
# прибыль фирмы в расчете на одного сотрудника.
#
# Пример:
# Введите выручку фирмы: 1000
# Введите издержки фирмы: 500
# Финансовый результат - прибыль. Ее величина: 500
# Значит вычисляем рентабельность выручки (соотношение прибыли к выручке)
# Рентабельность выручки = 0.5
# Введите численность сотрудников фирмы: 10
# Прибыль фирмы в расчете на одного сотрудника = 50.0

gain = int(input('Введите выручку фирмы:\n'))
costs = int(input('Введите издержки фирмы:\n'))
clear_gain = 0
if gain > costs:
    print('Финансовый результат - прибыль.')
    clear_gain = gain - costs
    rent = clear_gain / gain
    print(f"Ее величина: {clear_gain}\n"
          f"Значит вычисляем рентабельность выручки (соотношение прибыли к выручке) \n"
          f"Рентабельность выручки = {rent}")
elif gain == costs:
    print(f"Работа в ноль")
else:
    print(f"Финансовый результат - убыток")

people = int(input('Введите численность сотрудников фирмы: '))
profit = float(clear_gain / people)
print('Прибыль фирмы в расчете на одного сотрудника: %s' % profit)
