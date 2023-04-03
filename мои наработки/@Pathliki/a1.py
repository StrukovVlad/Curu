import pathlib
from pathlib import Path

"""В каком каталоге находимся"""
print(Path.cwd())
#  C:\Users\Влад\PycharmProjects\Guru\мои наработки\@Pathliki

"""Указываем путь к папке /html на рабочем столе"""
p = pathlib.Path('C:/Users/Влад/Desktop/html')

"""По пути p выводим все файлы (указываем * расширение) 
если файлы существуют (is_file())"""
print([item for item in p.rglob('*') if item.is_file()])
# [WindowsPath('C:/Users/Влад/Desktop/html/a.jpg'),
#  WindowsPath('C:/Users/Влад/Desktop/html/databases.db'),
#  WindowsPath('C:/Users/Влад/Desktop/html/index.html'),
#  WindowsPath('C:/Users/Влад/Desktop/html/my foto.jpg'),
#  WindowsPath('C:/Users/Влад/Desktop/html/my_foto2.jpg')]
#  WindowsPath('C:/Users/Влад/Desktop/html/djago.txt')

"""По пути d выводим  html-файлы (указываем *.html расширение) 
если файлы существуют (is_file())"""
print([item for item in p.rglob('*.html') if item.is_file()])
#  [WindowsPath('C:/Users/Влад/Desktop/html/index.html')]

"""Выводим только файлы если суффикс файла .db (suffix())
хотя указывали полное расширение(*) в rglob()"""
print([item for item in p.rglob('*') if item.suffix == '.db'])
# [WindowsPath('C:/Users/Влад/Desktop/html/databases.db')]

# ____________________________________________________________________________

import pathlib
from pathlib import Path

"""В корень входим"""
print(Path.home()) # C:\Users\Влад

p = pathlib.Path('C:/Users/Влад/Desktop/html')

"""Состав папки /html с рабочего стола по указвнному пути """
print(list(p.iterdir()))
# [WindowsPath('C:/Users/Влад/Desktop/html/a.jpg'),
#  WindowsPath('C:/Users/Влад/Desktop/html/databases.db'),
#  WindowsPath('C:/Users/Влад/Desktop/html/index.html'),
#  WindowsPath('C:/Users/Влад/Desktop/html/my foto.jpg'),kj
#  WindowsPath('C:/Users/Влад/Desktop/html/my_foto2.jpg')]
#  WindowsPath('C:/Users/Влад/Desktop/html/djago.txt')

"""Выведем все расширения файлов в папке /html по указанному пути """
for item in p.iterdir():
    print(item.suffixes, end=' ')

#  ['.jpg'] ['.db'] ['.txt'] ['.html'] ['.jpg'] ['.jpg]

"""Выведем все пути файлов из папки /html если суффикс будет '.jpg' """
for item in p.iterdir():
    if item.suffix == '.jpg':
        print(item)

# C:\Users\Влад\Desktop\html\a.jpg
# C:\Users\Влад\Desktop\html\myfoto.jpg
# C:\Users\Влад\Desktop\html\my_foto2.jpg


"""Прочитаем первую строку файла с расширентем '.txt'"""
for item in p.iterdir():
    if item.suffix == '.txt':
        with item.open() as f:
            print(f.readline())

# This module offers classes representing filesystem paths
# ______________________________________________________________________________

"""Переименовываем файл a.jpg в alur.jpg"""
p_1 = pathlib.Path('C:/Users/Влад/Desktop/html/a.jpg')

p_2 = pathlib.Path('C:/Users/Влад/Desktop/html/alur.jpg')

p_1.rename(p_2)

"""Выведем имена всех файлов после переименовчания с расширением .jpg 
из папки /html"""
for item in p.iterdir():
    if item.suffix == '.jpg':
        print(item.stem, end=' ')

# alur my foto my_foto2

"""А еще можно и так"""
print([item.stem for item in p.iterdir() if item.suffix == '.jpg'])
# ['alur', 'my foto', 'my_foto2']

















