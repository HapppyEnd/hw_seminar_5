"""Задача 28: Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел. Из
всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.
2 2
4"""

number_a = int(input('Введите число А: '))
number_b = int(input('Введите число B: '))
summa = 0


def sum_numbers(a, b):
    if b == 0:
        return a
    elif a < 0 or b < 0:
        return 'Введите неотрицательные числа.'
    else:
        return sum_numbers(a + 1, b - 1)


print(f'{number_a} + {number_b} = {sum_numbers(number_a, number_b)}')
