"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" и обработав исключение,
придумайте как это сделать
"""

my_list = ['attribute', 'класс', 'type']

for i in my_list:
    try:
        i = eval(f"b'{i}'")
        print(f'{i} переведена в {type(i)}')
    except:
        print(f'{i} не переведена в байты')