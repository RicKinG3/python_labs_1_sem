# -*- coding: utf-8 -*-
# Требуется написать программу для вычисления приближённого значения интеграла
# двумя разными методами 1 - правых прямоугольников / 2 - 3/8
#
# Выполнил Вольняга Максим ИУ7-16Б
#
from check import *

N1 = checker(input('Введите количества участков разбиения для численного интегрирования N1: '))
N2 = checker(input('Введите количества участков разбиения для численного интегрирования N2: '))
N1 = int(N1)
N2 = int(N2)
while N1 == 0:
    print('Вы ввели не верные значения N1 введите заново')
    N1 = checker(input('Введите количества участков разбиения для численного интегрирования N1: '))
while N2 == 0:
    print('Вы ввели не верные значения N2 введите заново')
    N2 = checker(input('Введите количества участков разбиения для численного интегрирования N2: '))
N1 = int(N1)
N2 = int(N2)
start = input('Введите начала отрезка: ')
while check_num_float(start) == 0:
    print('Вы ввели не верные значения для начала отрезка, введите заново')
    start = input('Введите начала отрезка: ')
start = float(start)
stop = input('Введите конец отрезка: ')
while check_num_float(stop) == 0:
    print('Вы ввели не верные значения для конца отрезка, введите заново')
    stop = input('Введите начала отрезка: ')
stop = float(stop)

# Проверка начальных и конечных отрезков
if start == stop:
    print('Вы ввели одинаковые занчения для начала и конца, введите их заново')
    start = input('Введите начала отрезка: ')
    while check_num_float(start) == 0:
        print('Вы ввели не верные значения для начала отрезка, введите заново')
        start = input('Введите начала отрезка: ')
    start = float(start)
    stop = input('Введите конец отрезка: ')
    while check_num_float(stop) == 0:
        print('Вы ввели не верные значения для конца отрезка, введите заново')
        stop = input('Введите начала отрезка: ')
    stop = float(stop)
if start > stop:
    start, stop = stop, start


# Функция
def func(x):
    y = x * x
    return y


# Первообразная заданной функции
def antiderivative_func(x):
    y = x ** 3 / 3
    return y


# Метод правых прямоугольников
def right_rectangle(n):
    h = (stop - start) / n  # Шаг
    summ = 0  # Сумма интегрирования для функции
    xstart = start + h
    for i in range(n):
        summ += func(xstart + i * h)
    return summ * h


# функция метода 3/8
def three_eighths(n, start, stop):
    k = 0
    if n % 3 == 0:
        summ = 0  # Сумма ингерирования  для функции
        t = 0  # Коэффициент изменяется в зависимости от i
        h = (stop - start) / n  # Шаг
        for i in range(n + 1):
            # Находим коэф
            if i == 0 or i == n:
                t = 1
            elif i % 3 == 0:
                t = 2
            else:
                t = 3
            summ += (3 / 8) * h * (t * func(start + i * h))  # Сумируем по формуле
        return summ
    else:
        return '-'


Ipr = right_rectangle(N1)
Ipr1 = right_rectangle(N2)
I3_81 = three_eighths(N1, start, stop)
I3_82 = three_eighths(N2, start, stop)

# Табличка
print('\n N1, N2:             |', '{}'.format(N1).center(20), '|', '{}'.format(N2).center(20) + '\n' + '-' * 69)
print(' Пр. прямоугольники: |', '{:.5}'.format(Ipr).center(20), '|', '{:.5}'.format(Ipr1).center(20) + '\n' + '-' * 69)
print(' 3/8 :               |', '{:.5}'.format(I3_81).center(20), '|', '{:.5}'.format(I3_82).center(20))

# Находим абсолютную погрешность для N1
print('\n Абсолютная и относительная погрешность для N1')
print('\n')
if three_eighths(N1, start, stop) == '-':
    print("Абсолютная погрешность (метод 3/8): - ")
    absolute_38 = '-'
else:
    absolute_38 = abs(antiderivative_func(stop) - antiderivative_func(start) - three_eighths(N1, start, stop))
    print("Абсолютная погрешность (метод 3/8): ", '{:.5}'.format(absolute_38))
absolut_pr = abs(antiderivative_func(stop) - antiderivative_func(start) - right_rectangle(N1))
print("Абсолютная погрешность (метод пр.прямоугольников): ", '{:.5}'.format(absolut_pr))
k = 0

#  находим относительную погрешность
if three_eighths(N1, start, stop) == '-':
    print('\n')
    print("Относительная погрешность (метод 3/8): - ")
    otn_38 = '-'
else:
    print('\n')
    otn_38 = abs(int(round(absolute_38 / three_eighths(N1, start, stop), 2) * 100))
    print("Относительная погрешность (метод 3/8): " + str(otn_38) + "%")
otn_pr = abs(int(round(absolut_pr / right_rectangle(N1), 2) * 100))
print("Относительная погрешность (метод пр.прямоугольников): " + str(otn_pr) + "%")

print('---------------------------------------------------------')
# Находим абсолютную погрешность для N2
print('\n Абсолютная и относительная погрешность для N2')
print('\n')
if three_eighths(N2, start, stop) == '-':
    print("Абсолютная погрешность (метод 3/8): - ")
    absolute_382 = '-'
else:
    absolute_382 = abs(antiderivative_func(stop) - antiderivative_func(start) - three_eighths(N2, start, stop))

    print("Абсолютная погрешность (метод 3/8): ", '{:.5}'.format(absolute_382))
absolut_pr2 = abs(antiderivative_func(stop) - antiderivative_func(start) - right_rectangle(N2))
print("Абсолютная погрешность (метод пр.прямоугольников): ", '{:.5}'.format(absolut_pr2))

# находим относительную погрешность N2
if three_eighths(N2, start, stop) == '-':
    print('\n')
    print("Относительная погрешность (метод 3/8): - ")
    otn_382 = '-'
else:
    print('\n')
    otn_382 = abs(int(round(absolute_382 / three_eighths(N2, start, stop), 2) * 100))
    print("Относительная погрешность (метод 3/8): " + str(otn_382) + "%")
otn_pr2 = abs(int(round(absolut_pr2 / right_rectangle(N2), 2) * 100))
print("Относительная погрешность (метод пр.прямоугольников): " + str(otn_pr2) + "%")

# для менее точного метода итерационно вычисляем количество участков разбиения, для которого интеграл
# будет вычислен с заданной точностью: |𝐼(𝑁) − 𝐼(2𝑁) | < ε

x = 0
if (three_eighths(N1, start, stop) == '-') and (three_eighths(N2, start, stop) == '-'):
    print('\nМетод 3/8 не был получен,  по этому вычисляем интегралл методом правых прямоугольников с задной точностью')
    x = 1
elif (three_eighths(N1, start, stop) == '-'):
    if otn_pr2 == otn_382:
        print('\nВсе методы точны.')
    elif otn_382 < otn_pr2:
        x = 1
    elif otn_382 < otn_pr2:
        x = 2
elif three_eighths(N2, start, stop) == '-':
    if otn_38 == otn_pr:
        print('\nВсе методы точны.')
    elif otn_38 < otn_pr:
        x = 1
    elif otn_38 > otn_pr:
        x = 2
elif (otn_38 == otn_pr) or (otn_pr2 == otn_382):
    print('\nВсе методы точны.')
elif otn_38 < otn_pr:
    x = 1
elif otn_38 > otn_pr:
    x = 2
if x == 1:
    print('\nНе точный метод - правых прямоугольников')
elif x == 2:
    print('\nНе точный метод - 3/8')
else:
    exit('Все методы одинаковы, программа завершила работу')

eps = input('\nВведите eps:  ')
while check_num_float(eps) == 0:
    print('Вы ввели не верные значения для eps, введите заново')
    eps = input('\nВведите eps: ')
eps = float(eps)
N = 4
if x == 2:
    I1 = three_eighths(2, start, stop)
    I2 = three_eighths(4, start, stop)
    while abs(I1 - I2) > eps:
        N *= 2
        I1 = I2
        I2 = three_eighths(N, start, stop)
    print('Точность eps при', N)
    print('Интеграл = {:.3g}'.format(I2))

elif x == 1:
    I1 = right_rectangle(2)
    I2 = right_rectangle(4)
    while abs(I1 - I2) > eps:
        N *= 2
        I1 = I2
        I2 = right_rectangle(N)
    print('Точность eps достигается при', N)
    print('Интеграл = {:.3g}'.format(I2))
