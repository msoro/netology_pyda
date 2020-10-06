# Задание 1
# Дана переменная, в которой хранится словарь, содержащий гео-метки для каждого пользователя
# (пример структуры данных приведен ниже).
# Вам необходимо написать программу, которая выведет на экран множество уникальных гео-меток всех пользователей.

ids = {'user1': [213, 213, 213, 15, 213], 'user2': [54, 54, 119, 119, 119], 'user3': [213, 98, 98, 35]}
# Результат: {98, 35, 15, 213, 54, 119}

# Variant A
uniq = list()
for codes in ids.values():
    for x in codes:
        uniq.append(x)
print(set(uniq))

# Variant B
# uniq = set()
# [uniq.update(set(x) if isinstance(x, (list, set)) else [x]) for x in ids.values()]
# print(uniq)

# ---------------------------------------------------------#
# Задание 2
# Дана переменная, в которой хранится список поисковых запросов пользователя
# (пример структуры данных приведен ниже). Вам необходимо написать программу,
# которая выведет на экран распределение количества слов в запросах в требуемом виде.
# Пример работы программы:

queries = [
‘смотреть сериалы онлайн’,
‘новости спорта’,
‘афиша кино’,
‘курс доллара’,
‘сериалы этим летом’,
‘курс по питону’,
‘сериалы про спорт’,
]
# Результат:
# Поисковых запросов, содержащих 2 слов(а): 42.86%
# Поисковых запросов, содержащих 3 слов(а): 57.14%