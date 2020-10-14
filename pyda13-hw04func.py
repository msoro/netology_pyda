documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

# Функция поиска владельца документа по номеру
# Результат: Владелец документа: Аристарх Павлов
def look_for_name():
    doc_number = input('Введите номер документа: ')
    s = ''
    print('Результат:')
    for n in documents:
        if n['number'] == doc_number:
            s = 'Владелец документа: ' + n['name']
            break
        else:
            s = 'Документ не найден в базе.'
    print(s)
##
# Функция поиска полки/папки по номеру
# Результат: Документ хранится на полке: 2
def look_for_dir():
    doc_number = input('Введите номер документа: ')
    s = ''
    print('Результат:')
    for i in directories:
        if doc_number in directories[i]:
            s = 'Документ хранится на полке: ' + i
            break
        else:
            s = 'Документ не найден в базе.'
    print(s)
##
# Функция листинга всех документов
# Результат: №: 2207 876234, тип: passport, владелец: Василий Гупкин, полка хранения: 1
def look_for_info():
    print('Результат:')
    for i in documents:
        string = '№: ' + i['number'] + ', тип: ' + i['type'] + ', владелец: ' + i['name']
        for j in directories:
            s = ', полка хранения: '
            if i['number'] in directories[j]:
                s = s + j
                break
            else:
                s = s + 'не найдена. '
        print(string + s)
##
# Пункт 4. Пользователь по команде “as” может добавить новую полку
# Полка добавлена. Текущий перечень полок: 1, 2, 3, 10.
def list_for_dir():
    s = []
    for i in directories:
        s.append(int(i))
    print('Текущий перечень полок: ' + str(sorted(s)).strip('[]'))

##
def add_for_dir():
    number = int(input('Введите номер полки: '))
    print('Результат:')
    if (number != 0) and number not in directories:
        directories[number] = []
        print('Полка добавлена. ')
    elif number in directories:
        print('Такая полка уже существует. ')
    else:
        print('Некорректный номер полки. ')
    list_for_dir()
##
# Пункт 5. Пользователь по команде “ds” может удалить существующую полку из данных
# (только если она пустая)
def del_for_dir():
    dir_number = input('Введите номер полки: ')
    print('Результат:')
    for key, value in directories.items():
        if key == dir_number:
            if value == []:
                directories.pop(key)
                print('Полка удалена. ')
                break
            else:
                print('На полке есть документы, удалите их перед удалением полки. ')
    list_for_dir()
##
# Задание 2 (необязательное)
# Пункт 1. Пользователь по команде “ad” может добавить новый документ в данные
def add_for_doc():
    doc_number = input('Введите номер документа: ')
    doc_type = input('Введите тип документа: ')
    doc_name = input('Введите владельца документа: ')
    doc_dir = input('Введите полку для хранения: ')
    print('Результат:')
    if doc_dir not in directories:
        print('Такой полки не существует. Добавьте полку командой as. ')
    else:
        new_doc = dict(type=doc_type, number=doc_number, name=doc_name)
        documents.append(new_doc)
        directories[doc_dir] += [doc_number]
        print('Документ успешно добавлен. ')
    print('Текущий список документов: ')
    look_for_info()
##
# Пункт 2. Пользователь по команде “d” может удалить документ из данных.
def del_for_doc():
    doc_number = input('Введите номер документа: ')
    print('Результат:')
    init_len = len(documents)
    for i, j in enumerate(documents):
        if doc_number == j['number']:
            documents.pop(i)
    if init_len == len(documents):
        return 'Документ не найден в базе. '
    for key, value in directories.items():
        if doc_number in value:
            value.remove(doc_number)
    print('Документ удален. ')
    print('Текущий список документов: ')
    look_for_info()
##
# Пункт 3. Пользователь по команде “m” может переместить документ с полки на полку
#
def move_for_dir():
    doc_number = input('Введите номер документа: ')
    is_doc = False
    ndir = input('Введите номер полки: ')
    print('Результат:')
    if ndir in directories:
        for key, value in directories.items():
            if doc_number in value:
                is_doc = True
                directories[ndir] += [doc_number]
                value.remove(doc_number)
        if is_doc == True:
            print('Документ перемещен. ')
        else:
            print('Документ не найден в базе. ')
    else:
        print('Такой полки не существует.', list_for_dir())
    print('Текущий список документов: ')
    look_for_info()
##

# Словарь команд
comm_dict = {
    'p':look_for_name,
    's':look_for_dir,
    'l':look_for_info,
    'ls':list_for_dir,
    'as':add_for_dir,
    'ds':del_for_dir,
    'ad':add_for_doc,
    'd':del_for_doc,
    'm':move_for_dir
}

# Функция ввода и проверки команды
def my_commands():
    comm = ''
    while comm != 'q':
        comm = input('Введите команду: ')
        if comm in comm_dict.keys():
            comm_dict[comm]()
        elif comm == 'q':
            print('Завершение работы.')
            break
        else:
            print('Команда не найдена')

##

my_commands()