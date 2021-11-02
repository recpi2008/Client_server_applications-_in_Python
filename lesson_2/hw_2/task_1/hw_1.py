"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""
from pprint import pprint
import csv

def get_data(list_file):
    main_list = []
    main_data = {'Название ОС':'','Код продукта':'','Изготовитель системы':'',  'Тип системы':''}

    for i in list_file:
        with open(i, encoding='utf-8') as f_n:
            for el_str in f_n:
                match = el_str.split(':')
                if match[0] == 'Изготовитель системы':
                    main_data['Изготовитель системы']=match[1].strip()
                elif match[0] == 'Название ОС':
                    main_data['Название ОС'] = match[1].strip()
                elif match [0] == 'Тип системы':
                    main_data['Тип системы'] = match[1].strip()
                elif match [0] == 'Код продукта':
                    main_data['Код продукта'] = match[1].strip()
            main_list.append(main_data.copy())
    return main_list

list_file = ['info_1.txt','info_2.txt','info_3.txt']


def write_to_csv(list_file):
    new = get_data(list_file)
    with open('data.csv', 'w') as f_n:
        F_N_WRITER = csv.DictWriter(f_n, fieldnames=list(new[0].keys()))
        F_N_WRITER.writeheader()
        for d in new:
            F_N_WRITER.writerow(d)

    with open('data.csv') as f_n:
        print(f_n.read())

write_to_csv(list_file)