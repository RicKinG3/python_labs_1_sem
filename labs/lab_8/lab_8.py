# Написать программу, которая позволит с использованием меню обеспечить работу с
# целочисленными матрицами:
# 1. Ввести матрицу
# 2. Добавить строку
# 3. Удалить строку
# 4. Добавить столбец
# 5. Удалить столбец
# 6. Найти строку, имеющую определённое свойство по варианту
# 7. Переставить местами строки с наибольшим и наименьшим количеством
# отрицательных элементов
# 8. Найти столбец, имеющий Наибольшее количество чисел, являющихся степенями 2
# 9. Переставить местами столбцы с максимальной и минимальной суммой
# элементов
# 10. Вывести текущую матрицу
##
##
# Выполнил работу Вольняга Максим ИУ7-16Б
##


from check import checker, matrix_check

arr = []


# Функция  ввода матрицы
def matrix_input(arr):
    n = checker(input("Введите количество строк: "))
    m = checker(input("Введите количество столбцов: "))
    n = int(n)
    m = int(m)
    if n == 0 or m == 0:
        print('Вы ввели нулевые значения')
        return arr
    arr.clear()
    for i in range(n):
        new = list(map(str, input(f'Введите строку №{i + 1} через пробел: ').split()))
        while len(new) != m:
            print('Ошибка! Указанное количество элементов не соответсвует данному')
            new = list(map(str, input(f'Введите строку №{i + 1} через пробел: ').split()))
        arr.append(new)
    return arr


# Функция для вывода матрицы
def print_matrix(a):
    for row in a:
        for col in row:
            print("{:^10d}".format(col), end="")
        print()


# Функия добавления строки
def add_string(arr, var):
    index = checker((input('Введите индекс для вставки строки: ')))
    index = int(index)
    if 0 <= index <= len(arr):  # Проверка на некорректный индекс
        new = []
        new = list(map(str, input(f'Введите новую строку через пробел: ').split()))
        while len(new) != len(arr[0]):
            print('Ошибка! Указанное количество элементов не соответсвует данному')
            new = list(map(str, input(f'Введите строку №{index + 1} через пробел: ').split()))
        if var == 1:
            arr += [0] * len(arr[0])
            for i in range(len(arr) - 1, index, -1):
                arr[i] = arr[i - 1]
            arr[index] = new
            return arr
        elif var == 2:
            arr.insert(index, new)
            return arr
    else:
        print('Ошибка: Некорректный индекс')


# Функция удаления строки
def del_string(arr, var):
    index = checker(input('Введите индекс удаляемой строки: '))
    index = int(index)
    if 0 <= index < len(arr):  # Проверка на некорректный индекс
        if var == 1:
            for i in range(index, len(arr) - 1):
                arr[i] = arr[i + 1]
            del arr[-1]
            return arr
        elif var == 2:
            del arr[index]
            return arr
    else:
        print('Ошибка: Некорректный индекс')


# Фунцция для добавления столбца
def add_column(arr, var):
    index = checker(input('Введите индекс для вставки строки: '))
    index = int(index)
    if 0 <= index <= len(arr):  # Проверка на некорректный индекс
        new = []
        for j in range(len(arr)):
            new.append(checker(input(f'Введите элемент столбца №{j + 1}: ')))

        if var == 1:
            for i in range(len(arr)):
                arr[i] += [0]
                for j in range(len(arr[0]) - 1, index, -1):
                    arr[i][j] = arr[i][j - 1]
                arr[i][index] = new[i]
            return arr
        elif var == 2:
            for i in range(len(arr)):
                arr[i].insert(index, new[i])
            return arr
    else:
        print('Ошибка: Некорректный индекс')


# Удаление столбца
def del_column(arr, var):
    index = checker(input('Введите индекс удаляемого столбца: '))
    index = int(index)
    if 0 <= index < len(arr):  # Проверка на некорректный индекс
        if var == 1:
            for i in range(len(arr)):
                for j in range(index, len(arr[0]) - 1):
                    arr[i][j] = arr[i][j + 1]
                print('arr[i][-1]', arr[i][-1])
                del arr[i][-1]
            return arr
        elif var == 2:
            for i in range(len(arr)):
                del arr[i][index]
            return arr
    else:
        print('Ошибка: Некорректный индекс')


# Функция проверки степеней двойки
def is_degree_two(a, arr=[1]):
    while max(arr) < a and a > 0:
        arr.append(max(arr) * 2)
    return True if a in arr else False


# Функция меню
def menu():
    print('Меню команд:')
    print('0 - Выйти из программы')
    print('1 - Ввести матрицу')
    print('2 - Добавить строку')
    print('3 - Удалить строку')
    print('4 - Добавить столбец')
    print('5 - Удалить столбец')
    print('6 - Найти строку, имеющую Наибольшее среднее арифметическое')
    print('7 - Переставить местами строки с наибольшим и наименьшим количеством отрицательных элементов')
    print('8 - Найти столбец, имеющий Наибольшее количество чисел, являющихся степенями 2')
    print('9 - Переставить местами столбцы с максимальной и минимальной суммой элементов')
    print('10 - Вывести текущую матрицу')


counter = 0  # Счетчик введеных команд
# Первая инициализация списка
print('Введите список с клавиатуры')

while True:
    if counter % 3 == 0:
        menu()
    counter += 1
    command = (checker(input("Введите номер меню: ")))
    command = int(command)

    if 0 <= command <= 10:

        # Выход из программы
        if command == 0:
            exit("Программа завершила работу")
        # Ввод матрицы
        elif command == 1:
            arr = matrix_input(arr)
            for i in range(len(arr)):
                for j in range(len(arr[i])):
                    if matrix_check(arr[i][j]):
                        arr[i][j] = int(arr[i][j])
                    else:
                        print('Вы ввели не целочисленную матрицу, введите заново')
                        arr = matrix_input(arr)

        # Добавление строки
        elif command == 2:
            print('1 - Алгоритмическая реализация')
            print('2 - Реализация средствами языка')
            num = checker(input('>>> '))
            num = int(num)
            if 0 < num <= 2:
                add_string(arr, num)
            else:
                print('Ошибка! Нет такого варианта')
        # Удаление строки
        elif command == 3:
            print('1 - Алгоритмическая реализация')
            print('2 - Реализация средствами языка')
            num = int(input('>>> '))
            if 0 < num <= 2:
                del_string(arr, num)
        # Добавление столбца
        elif command == 4:
            print('1 - Алгоритмическая реализация')
            print('2 - Реализация средствами языка')
            num = checker(input('>>> '))
            num = int(num)
            if 0 < num <= 2:
                add_column(arr, num)
            else:
                print('Ошибка! Нет такого варианта')
        elif command == 5:  # Удаление столбца
            print('1 - Алгоритмическая реализация')
            print('2 - Реализация средствами языка')
            num = checker(input('>>> '))
            num = int(num)
            if 0 < num <= 2:
                del_column(arr, num)
            else:
                print('Ошибка! Нет такого варианта')
        # Поиска строки с максимальным средне арифметическим
        elif command == 6:
            average = []  # Список хранит среднее арифметическое всех строк
            for x in arr:
                summa = 0
                for j in x:
                    summa += j
                average.append(summa / len(arr[0]))
            print("\n\n")
            print("Строка {0}, имеет наибольшее среднее арифметическое {1:.6g}".format(arr[average.index(max(average))],
                                                                                       max(average)))
        # Свап строк с максимальным и минимальным количеством отриц. элементов
        elif command == 7:
            negatives = []  # Список хранящий количество отрицательных элементов в каждой строке

            for x in arr:
                neg_count = 0
                for j in x:
                    if j < 0:
                        neg_count += 1
                negatives.append(neg_count)

            arr[negatives.index(min(negatives))], arr[negatives.index(max(negatives))] = \
                arr[negatives.index(max(negatives))], arr[negatives.index(min(negatives))]
    elif command == 8:
        maxi_degrees = []  # Список хранящий количество степеней двойки в каждом столбце

        for x in range(len(arr[0])):
            count = 0
            for j in range(len(arr)):
                if is_degree_two(arr[j][x]):
                    count += 1
            maxi_degrees.append(count)

        print("\n\n")
        nes_col = []  # Список хранящий столбец с максимальным количеством степеней 2
        for x in arr:
            nes_col.append(x[maxi_degrees.index(max(maxi_degrees))])

        print("Столбец {0}, имеет наибольшее количество степеней двойки {1}"
              .format(nes_col, max(maxi_degrees)))
    elif command == 9:
        summary = []  # Список хранящий сумму всех столбцов
        for x in range(len(arr[0])):
            count = 0
            for j in range(len(arr)):
                count += arr[j][x]
            summary.append(count)

        for x in arr:
            x[summary.index(min(summary))], x[summary.index(max(summary))] = \
                x[summary.index(max(summary))], x[summary.index(min(summary))]  # Меняем местами столбцы
    # Вывод матрицы
    elif command == 10:
        print("\n\n")
        print("Ваша матрица:")
        print_matrix(arr)
