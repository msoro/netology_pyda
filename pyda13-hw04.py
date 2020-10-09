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

# Функция ввода и проверки команды
def my_commands():
    comm = ''
    while comm != 'q':
        comm = input('Введите команду:')
        if comm == 'p':
            name = look_for_name(input('Введите номер документа: '))
            print('Результат:')
            if name != 0:
                print('Владелец документа:', name)
            else:
                print('Документ не найден в базе')
        elif comm == 's':
            ddir = look_for_dir(input('Введите номер документа: '))
            print('Результат:')
            if ddir != 0:
                print('Документ хранится на полке:', ddir)
            else:
                print('Документ не найден в базе')
        elif comm == 'l':
            print('Результат:')
            look_for_info()
        elif comm == 'ls':
            print('Результат:')
            print(list_for_dir())
        elif comm == 'as':
            adir = add_for_dir(input('Введите номер полки: '))
            print('Результат:')
            if adir != 0:
                print('Полка добавлена.' + list_for_dir())
            else:
                print('Такая полка уже существует.' + list_for_dir())
        elif comm == 'ds':
            ddir = del_for_dir(input('Введите номер полки: '))
            print('Результат:')
            print(ddir + list_for_dir())
        elif comm == 'q':
            print('Завершение работы программы.')
            break
        else:
            print('Команда не найдена')

# Функция поиска владельца документа по номеру
# Результат: Владелец документа: Аристарх Павлов
def look_for_name(doc_number):
    for n in documents:
        if n['number'] == doc_number:
            return x['name']
        else:
            return 0
##


# Функция поиска полки/папки по номеру
# Результат: Документ хранится на полке: 2
def look_for_dir(doc_number):
    for i in directories:
        if doc_number in directories[i]:
            return i
    return 0
##

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
                s = s + 'не найдена'
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
        print('Некорректный номер полки')
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
                return 'Полка удалена.'
            else:
                return 'На полке есть документы, удалите их перед удалением полки.'
    else:
        return 'Такой полки не существует.'
##

my_commands()