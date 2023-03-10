# -*- coding: utf-8 -*-

def __alias(num_type):
    match num_type:
        case 'float':
            return 'вещественное число'
        case 'integer':
            return 'целое число'
        case 'natural':
            return 'натуральное число'
        case 'char':
            return 'символ'
        case 'word':
            return 'слово'
        case 'str':
            return 'строку'
        case _:
            return 'значение'


def __is_valid(n: str, num_type, predicate):
    match num_type:
        case 'float':
            try:
                val = float(n)
                if not predicate(val):
                    return False, None
                return True, val
            except ValueError:
                return False, None
        case 'integer':
            try:
                val = int(n)
                if not predicate(val):
                    return False, None
                return True, val
            except ValueError:
                return False, None
        case 'natural':
            try:
                val = int(n)
                if val < 1:
                    return False, None
                if not predicate(val):
                    return False, None
                return True, val
            except ValueError:
                return False, None
        case 'char':
            if len(n) == 1:
                if predicate(n):
                    return True, n
                else:
                    return False, None
            else:
                return False, None
        case 'word':
            temp = n.strip()
            if ' ' in temp or len(temp) == 0 or not predicate(temp):
                return False, None
            else:
                return True, temp
        case 'str':
            if n == '' or len(n) == 0 or not predicate(n):
                return False, None
            else:
                return True, n
        case _:
            return False, None


def input_value(name, num_type='float', predicate=lambda x: True):
    request = f'Введите {__alias(num_type)} ({name}): '
    err_msg = f'Введённое значение не подходит под запрос'
    val = input(request)
    flag, number = __is_valid(val, num_type, predicate)
    while not flag:
        print(err_msg)
        val = input(request)
        flag, number = __is_valid(val, num_type, predicate)

    return number


def input_array(n, name='массива', num_type='float', predicate=lambda x: True, post=lambda x: x):
    arr = []
    for i in range(n):
        val = input_value(f'{i + 1} эл-т {name}', num_type, predicate)
        arr.append(post(val))
    return arr


def input_matrix(n, m, name='матрицы', num_type='float', predicate=lambda x: True, post=lambda x: x):
    matrix = []
    for i in range(n):
        val = input_array(m, f'{i + 1} строки {name}', num_type, predicate, post)
        matrix.append(val)
    return matrix
