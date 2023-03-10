# -*- coding: utf-8 -*-
import _io
from os.path import exists
import d
import smart_input as si
import pretty_print as pp


# База данных с хранением в виде бинарного файла как в 12 + удаление (сдвиг на сколько-то)
# Шаблон записи в бд
# name=40 символов = 160 байт из расчёта 4 б/символ, group=20 символов = 80 байт,
# age = 1 байт, course = 1 байт, рейтинг = 4 байта (0.57 - 4 символа)


# Перевод названий параметров словарь
param_translate = {
    'name': 'ФИО',
    'course': 'Учебный курс (1-6)',
    'group': 'Группа',
    'age': 'Возраст',
    'education_rating': 'Образовательный рейтинг (от 0 до 1)'
}
# Настройка размеров записи словарем
param_size = {
    'name': 160,
    'course': 1,
    'group': 80,
    'age': 1,
    'education_rating': 4
}
entry_byte_size = 0
for key in param_size:
    entry_byte_size += param_size[key]

# Меню со списком действий
menu = """Список доступных действий:
1. Выбрать файл для работы
2. Инициализировать базу данных
3. Вывести содержимое базы данных
4. Добавить запись в базу данных
5. Поиск по имени
6. Поиск по курсу и образовательному рейтингу
7. Добавить 10 случайных записей
8. Удалить запись из БД по позиции
0. Завершить программу
"""

# Путь к текущему файлу БД
current_db = ''
# Инициализирована ли БД
initialised = False

# кодирование строки
def encode_string_fixed(string: str, byte_len: int) -> bytearray:
    byte_arr = bytearray()
    byte_arr.extend(string.encode('utf-8'))
    while len(byte_arr) < byte_len:
        byte_arr.append(0)
    return byte_arr[:byte_len]

# Декодирование строк
def decode_str_clear(byte_arr: bytes) -> str:
    return byte_arr.decode('utf-8').replace('\u0000', '')

# Запись в байты
def entry_to_bytes(entry: dict):
    bytes_arr = bytearray()
    name = entry['name']
    bytes_arr.extend(encode_string_fixed(name, 160))
    course = min(entry['course'], 255)
    bytes_arr.append(course)
    group = entry['group']
    bytes_arr.extend(encode_string_fixed(group, 80))
    age = min(entry['age'], 255)
    bytes_arr.append(age)
    education_rating = str(entry['education_rating'])
    bytes_arr.extend(encode_string_fixed(education_rating, 4))
    return bytes_arr

# Запись байтов
def bytes_to_entry(bytes_arr: bytes):
    d = {}
    name = decode_str_clear(bytes_arr[:160])
    course = bytes_arr[160]
    group = decode_str_clear(bytes_arr[161:241])
    age = bytes_arr[241]
    education_rating = float(decode_str_clear(bytes_arr[242:246]))
    d['name'] = name
    d['course'] = course
    d['group'] = group
    d['age'] = age
    d['education_rating'] = education_rating
    if not ('name' in d and 'course' in d and 'group' in d and 'age' in d and 'education_rating' in d):
        return 'err'
    return d


def ensure_file(path, strict=False):
    if (not exists(path)) or strict:
        open(path, mode='wb').close()

def read_generator():
    if not initialised:
        print('База данных не инициализирована')
        yield 'err'
        return
    try:
        file = open(current_db, 'rb')
    except:
        print('Открытие файла невозможно!')
        yield 'err'
        return
    line = file.read(entry_byte_size)
    while len(line) == entry_byte_size:
        entry = bytes_to_entry(line)
        if entry == 'err':
            continue
        yield entry
        line = file.read(entry_byte_size)
    file.close()


def real_decorator(open_mode, strict=True):
    def open_decorator(func):
        def wrapper(*args, **kwargs):
            if (not initialised) and strict:
                print('База данных не инициализирована')
                return
            try:
                file = open(current_db, open_mode)
            except:
                print('Открытие файла невозможно!')
                return
            value = func(file, *args, **kwargs)
            file.close()
            return value

        return wrapper

    return open_decorator


@real_decorator('rb', strict=False)
def is_db(file: _io.BytesIO):
    line = file.read(entry_byte_size)
    flag = True
    while len(line) == entry_byte_size:
        if bytes_to_entry(line) == 'err':
            flag = False
        line = file.read(entry_byte_size)
    return flag


def option_add_entry():
    d = {}
    for key in param_translate:
        name = param_translate[key]
        if key == 'age':
            value = si.input_value('значение поля Возраст', num_type='integer', predicate=lambda x: 0 <= x <= 150)
        elif key == 'course':
            value = si.input_value('значение поля Курс [1-6]', num_type='integer', predicate=lambda x: 1 <= x <= 6)
        elif key == 'education_rating':
            value = si.input_value('значение Образовательного рейтинга [0-1]', num_type='float',
                                   predicate=lambda x: 0 <= x <= 1)
        else:
            value = si.input_value(name=f'значение поля {name}, (не более {param_size[key] // 4} символов)',
                                   num_type='str')
        d[key] = value
    write_entry(d)


@real_decorator('ab')
def write_entry(file: _io.BytesIO, entry: dict):
    encoded = entry_to_bytes(entry)
    file.write(encoded)


def print_entry(entry):
    for el in entry:
        print(f'{param_translate[el]}: {entry[el]}')

# Удобный вывод записей
def print_entries_matrix(entries: list):
    columns = [key for key in param_translate]
    to_print = [[entry[key] for key in entry] for entry in entries]
    print('-' * 140)
    pp.print_matrix(matrix=to_print, col_size=20, column_labels=columns)
    print('-' * 140)


def option_print_entries():
    count = 0
    entries = []
    for entry in read_generator():
        if entry == 'err':
            return
        count += 1
        entries.append(entry)
    if count > 0:
        print_entries_matrix(entries)
        print(f'Всего записей в БД: {count}')
    else:
        print('БД пуста!')


def option_find_by_name():
    name = input('Введите ФИО, по которому хотите найти запись: ')
    found = []
    for entry in read_generator():
        if entry == 'err':
            return
        if entry['name'] == name:
            found.append(entry)
    if len(found) > 0:
        print_entries_matrix(found)
        print(f'Всего совпадений: {len(found)}')
    count = entry['name']
    else:
        print('Совпадений в БД не найдено!')

# Поиск по курсу
def option_find_by_course_rating():
    condition = input('Введите режим сравнения с рейтингом > или < , иное - отменить операцию: ')
    if condition == '<':
        flag_mode = False
    elif condition == '>':
        flag_mode = True
    else:
        return
    found = []
    threshold = si.input_value('Рейтинг для поиска (0-1)', num_type='float', predicate=lambda x: 0 <= x <= 1)
    course = si.input_value('Учебный курс (1-6)', num_type='integer', predicate=lambda x: 1 <= x <= 6)
    for entry in read_generator():
        if entry == 'err':
            return
        if entry['course'] == course:
            rate = entry['education_rating']
            if flag_mode:
                flag = rate > threshold
            else:
                flag = rate < threshold
            if flag:
                found.append(entry)
    if len(found) > 0:
        print_entries_matrix(found)
        print(f'Всего совпадений: {len(found)}')
    else:
        print('Совпадений в БД не найдено!')

# Удаление записи
@real_decorator('rb+')
def delete_entry(file: _io.BytesIO, index: int, total: int):
    for _ in range(index):
        b = file.read(entry_byte_size)
        file.seek(file.tell() - entry_byte_size)
        file.write(b)
    threshold = (total - 1) * entry_byte_size
    while file.tell() != threshold:
        file.seek(file.tell() + entry_byte_size)
        read_bytes = file.read(entry_byte_size)
        file.seek(file.tell() - 2 * entry_byte_size)
        file.write(read_bytes)
    file.truncate(threshold)


def option_delete_entry():
    count = 0
    for entry in read_generator():
        if entry == 'err':
            return
        count += 1
    if count == 0:
        print('База данных пуста!')
    else:
        index = si.input_value(name=f'номер записи в БД [1-{count}]', num_type='natural',
                               predicate=lambda x: 1 <= x <= count) - 1
        delete_entry(index, count)
        print('Запись удалена!')

#  изменение  текущей баз данных
def option_change_current_db():
    global current_db
    global initialised
    path = input('Введите путь к файлу базы данных: ')
    print(f'Выбрана база данных {path}')
    current_db = f'{path}'
    if exists(current_db):
        valid = is_db()
        if not valid:
            print('''Внимание, данный файл не является файлом базы данных.
Вы можете инициализировать его, однако это сотрёт его содержимое!''')
            initialised = False
        else:
            initialised = True
    else:
        initialised = False


def option_init_db():
    global initialised
    global current_db
    if current_db == '':
        print('Не выбран файл для базы данных!')
        return
    try:
        ensure_file(current_db, strict=True)
    except IsADirectoryError:
        print('Введённый путь является путём к папке!')
        return
    except:
        print('Создание файла невозможно!')
        return
    initialised = True
    print('База данных инициализирована!')

# генератор рандома
def generate_dummies(n):
    for i in range(n):
        course = d.randint(1, 6)
        d = {'name': f'МСН-{d.randint(100000, 999999)}', 'course': course,
             'age': d.randint(17, 23) + course, 'education_rating': d.randint(10, 100) / 100,
             'group': f'ГСЛ-{d.randint(10, 99)}'}
        write_entry(d)


while True:
    if initialised and (not exists(current_db) or not is_db()):
        print('Внимание, файл базы данных был удалён или изменён, статус изменён на неинициализированный')
    print(menu)
    print(f'Выбранная база: {current_db if current_db != "" else "ФАЙЛ БАЗЫ ДАННЫХ НЕ ВЫБРАН"}')
    print(f'Статус: {"Инициализирована" if initialised else "Не инициализирована"}')
    mode = input('Введите необходимый вариант действия: ')
    if mode == '0':
        exit()
    elif mode == '1':
        option_change_current_db()
    elif mode == '2':
        option_init_db()
    elif mode == '3':
        option_print_entries()
    elif mode == '4':
        option_add_entry()
    elif mode == '5':
        option_find_by_name()

        option_delete_entry()

    elif mode == '6':
        option_find_by_course_rating()
    elif mode == '7':
        generate_dummies(10)
    elif mode == '8':
        option_delete_entry()
    else:
        print('Не существует такого варианта действий')