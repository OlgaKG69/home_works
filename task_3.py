# Задание 3.
#
# Узнайте у пользователя целое положительное число n.
# Найдите сумму чисел n + nn + nnn.
#
# Пример:
# Введите число n: 3
# n + nn + nnn = 369

n = input('Введите число n: ')
print(f"n + nn + nnn = {int(n) + int(n * 2) + int(n * 3)}")