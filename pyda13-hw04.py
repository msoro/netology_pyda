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
    p = ''
    print('Результат:')
    for n in documents:
        if doc_number == n['number']:
            p = 'Владелец документа: ' + n['name']
            break
        else:
            p = 'Документ не найден в базе'
    print(p)
##

# Функция поиска полки/папки по номеру
# Результат: Документ хранится на полке: 2
def look_for_dir():
    doc_number = input('Введите номер документа: ')
    s = ''
    print('Результат:')
    for n in directories:
        if doc_number in directories[n]:
            s = 'Документ хранится на полке: ' + n
            break
        else:
            s = 'Документ не найден в базе.'
    print(s)
##

# Словарь команд
comm_dict = {
    'p':look_for_name,
    's':look_for_dir
}

comm = ''
while comm != 'q':
    comm = input('Введите команду: ')
    if comm in comm_dict.keys():
        comm_dict[comm]()
    elif comm == 'q':
        print('Завершение работы')
        break
    else:
        print('Команда не найдена')