#Практическое задание по теме: "Словари и множества"
#1. Работа со словарями
my_dict = {'Andrey': 1997, 'Denis': 1995, 'Egor': 1999, 'Sergey': 2005}
print(my_dict)
#Выведите на экран одно значение по существующему ключу,
# одно по отсутствующему из словаря my_dict без ошибки.
print(my_dict['Andrey'])
my_dict['Ura'] = 1994
print(my_dict)
print(my_dict.get('Ura'))
print(my_dict.get('Vlad', 'Такого не найдено'))
#Добавьте ещё две произвольные пары того же формата в словарь my_dict.
my_dict.update({'Dasha': 2005,
                'Eva': 2003})
#Удалите одну из пар в словаре по существующему ключу из словаря my_dict
# и выведите значение из этой пары на экран
print(my_dict.pop('Andrey'))
print(my_dict)
print(my_dict.items())
#2.  Работа с множествами:
#Создайте переменную my_set и присвойте ей множество,
# состоящее из разных типов данных с повторяющимися значениями
my_set = {1, 2, 3, 3, 2, 1, 4, 5, 4, 5, 'Apple', 4, 6}
print(my_set)
#Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
#- Удалите один любой элемент из множества my_set.
#- Выведите на экран измененное множество my_set.
my_set.add(9)
my_set.add('Bork')
my_set.add((1, 2, 3))
print(my_set)
my_set.discard('Bork')
print(my_set)


