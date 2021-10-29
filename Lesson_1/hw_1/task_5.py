"""
Задание 5.

    Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet



def ping_source(source):
    for i in source:
        ARGS = ['ping', i]
        YA_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
        for line in YA_PING.stdout:
            result = chardet.detect(line)
            line = line.decode(result['encoding']).encode('utf-8')
            print(line.decode('utf-8'))

my_list = ['yandex.ru','youtube.com']
ping_source(my_list)