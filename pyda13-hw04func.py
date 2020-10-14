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
        else:
            s = 'Документ не найден в базе.'
    print(s)
##

# Словарь команд
comm_dict = {
    'p':look_for_name,
    's':look_for_dir
}

# Функция ввода и проверки команды
def my_commands():
    comm = ''
    while comm != 'q':
        comm = input('Введите команду: ')
        if comm in comm_dict.keys():
            comm_dict[comm]()
        elif comm == 'q':
            break
        else:
            print("Команда не найдена")

##

my_commands()


# Функция ввода и проверки команды
# def my_commands():
#     comm = ''
#     while comm != 'q':
#         comm = input('Введите команду:')
#         if comm == 'p':
#             dname = look_for_name(input('Введите номер документа: '))
#             print('Результат:')
#             if dname != 0:
#                 print('Владелец документа:', dname)
#             else:
#                 print('Документ не найден в базе')
#         elif comm == 's':
#             sdir = look_for_dir(input('Введите номер документа: '))
#             print('Результат:')
#             if sdir != 0:
#                 print('Документ хранится на полке:', sdir)
#             else:
#                 print('Документ не найден в базе')
#         elif comm == 'l':
#             print('Результат:')
#             look_for_info()
#         elif comm == 'ls':
#             print('Результат:')
#             print(list_for_dir())
#         elif comm == 'as':
#             adir = add_for_dir(input('Введите номер полки: '))
#             print('Результат:')
#             if adir != 0:
#                 print('Полка добавлена.' + list_for_dir())
#             else:
#                 print('Такая полка уже существует.' + list_for_dir())
#         elif comm == 'ds':
#             ddir = del_for_dir(input('Введите номер полки: '))
#             print('Результат:')
#             print(ddir + list_for_dir())
#         elif comm == 'ad':
#             adoc = add_for_doc(input('Введите номер документа: '))
#             print(adoc)
#             print('Текущий список документов:')
#             look_for_info()
#         elif comm == 'd':
#             ddoc = del_for_doc(input('Введите номер документа: '))
#             print(ddoc + 'Текущий список документов:')
#             look_for_info()
#         elif comm == 'm':
#             mdoc = move_for_dir(input('Введите номер документа: '))
#             print(mdoc)
#             print('Текущий список документов:')
#             look_for_info()
#         elif comm == 'q':
#             print('Завершение работы программы.')
#             break
#         else:
#             print('Команда не найдена')






# Функция листинга всех документов
# Результат: №: 2207 876234, тип: passport, владелец: Василий Гупкин, полка хранения: 1
def look_for_info():
    for i in documents:
        string = '№: ' + i['number'] + ', тип: ' + i['type'] + ', владелец: ' + i['name']
        #        print(string)
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
    result = ('Текущий перечень полок: ' + str(s).strip('[]'))
    return result


def add_for_dir(number):
    if number != 0:
        if number not in directories:
            directories[number] = []
            return number
        else:
            return 0
    else:
        print('Некорректный номер полки. ')


##

# Пункт 5. Пользователь по команде “ds” может удалить существующую полку из данных
# (только если она пустая)
# Полка удалена. Текущий перечень полок: 1, 2.
# На полке есть документы, удалите их перед удалением полки. Текущий перечень полок: 1, 2, 3.
def del_for_dir(dir_number):
    if dir_number in directories:
        for key, value in directories.items():
            if value == '':
                key.remove(dir_number)
                return 'Полка удалена. '
            else:
                return 'На полке есть документы, удалите их перед удалением полки. '
    else:
        return 'Такой полки не существует. '


##

# Задание 2 (необязательное)
# Пункт 1. Пользователь по команде “ad” может добавить новый документ в данные
def add_for_doc(doc_number):
    if doc_number not in documents:
        doc_type = input('Введите тип документа: ')
        doc_name = input('Введите владельца документа: ')
        doc_dir = input('Введите полку для хранения: ')
        if doc_dir in directories:
            new_doc = dict(type=doc_type, number=doc_number, name=doc_name)
            documents.append(new_doc)
            directories[doc_dir] += [doc_number]
            return 'Документ успешно добавлен. '
        else:
            return 'Такой полки не существует. Добавьте полку командой as. '
    else:
        return 0


##

# Пункт 2. Пользователь по команде “d” может удалить документ из данных.
# работает
def del_for_doc(doc_number):
    init_len = len(documents)
    for i, j in enumerate(documents):
        if doc_number == j['number']:
            documents.pop(i)
    if init_len == len(documents):
        return 'Документ не найден в базе. '
    for key, value in directories.items():
        if doc_number in value:
            value.remove(doc_number)
    return 'Документ удален. '


# не работает :( - надо уточнить преподавателя - где ошибка логики ?!
#     if doc_number not in documents:
#         return 'Документ не найден в базе. '
#     else:
#         for i, d in enumerate(documents):
#             if d['number'] == doc_number:
#                 documents.pop(i)
#         for key, value in directories.items():
#             if doc_number in value:
#                 value.remove(doc_number)
#         return 'Документ удален.'
##


# Пункт 3. Пользователь по команде “m” может переместить документ с полки на полку
#
def move_for_dir(doc_number):
    is_doc = False
    ndir = input('Введите номер полки: ')
    if ndir in directories:
        for key, value in directories.items():
            if doc_number in value:
                is_doc = True
                directories[ndir] += [doc_number]
                value.remove(doc_number)
        if is_doc == True:
            return 'Документ перемещен. '
        else:
            return 'Документ не найден в базе. '
    else:
        s = 'Такой полки не существует.' + list_for_dir()
        return s


##




