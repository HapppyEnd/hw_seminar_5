"""Задача 26: Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8"""

num_a = int(input('Введите число А: '))
num_b = int(input('Введите число B: '))


def number_pow(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b > 1:
        return a * number_pow(a, b - 1)
    else:
        return 1/(a * number_pow(a, -b - 1))


print(f'Число {num_a} в степени {num_b} = {number_pow(num_a, num_b)}')
