# -*- coding: utf-8 -*-

import re


def __is_whitespace(s: str):
    return s == '' or s.isspace()


def __formatted_list(lst: list, formatting: str):
    f = '{:' + formatting + '}'
    new_list = []
    for el in lst:
        if el == 'NaN' and 's' not in formatting:
            new_list.append('NaN')
        else:
            new_list.append(f.format(el))
    return new_list


def print_matrix(matrix: list, col_size: int, formatting: str = '', column_labels: list = None, row_labels: list = None):
    if column_labels is None:
        column_labels = [str(i + 1) for i in range(len(matrix[0]))]
    if row_labels is None:
        row_labels = [str(i + 1) for i in range(len(matrix))]
    first_col_size = max(max(map(len, row_labels)), col_size)
    print_list(column_labels, f'{col_size}s', f'|{" "*first_col_size}|', '|', '|')
    matrix_ind = 0
    lst = []
    formatted_matrix = list(map(lambda l: __formatted_list(l, formatting), matrix))
    for i in range(len(matrix)):
        lst.clear()
        matrix_ind = 0
        for ind in range(len(column_labels)):
            if __is_whitespace(column_labels[ind]):
                lst.append('')
            else:
                lst.append(formatted_matrix[i][matrix_ind])
                matrix_ind += 1
        print_list(lst, f'{col_size}s', start=f'|{row_labels[i]:{first_col_size}s}|', stop='|', sep='|')


def print_list(list, formatting: str = '', start='', stop='', sep=' '):
    s = start
    formatted = __formatted_list(list, formatting)
    for i, el in enumerate(formatted):
        s += el
        if i != len(list) - 1:
            s += sep
    s += stop
    print(s)