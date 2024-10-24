import os
import time

directory = '.'
current_file = os.path.basename('./module_7_5.py')

for root, dirs, files in os.walk(directory):
    for file in files:
        if file == current_file:

            filepath = os.path.join(directory, current_file)
            filesize = os.path.getsize(current_file)
            filetime = os.path.getmtime(current_file)
            f_filetime =  time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            fileroot = os.path.join('pyProj2/m7', current_file)
            fileroot = os.path.dirname(fileroot)
            print(f'Обнаружен:{file} Путь: {filepath}, Размер {filesize} байт, Время изменения: {f_filetime}, Корень: {fileroot}')

