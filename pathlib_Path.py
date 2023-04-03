from pathlib import Path

"""Текущая рабочая директория"""
print(Path.cwd())
# C:\Users\Влад\PycharmProjects\Guru

"""Домашняя директория"""
print(Path.home())
# C:\Users\Влад

z_file = Path.cwd()/'goblin'/'output.xlsx'
# print(Path.cwd())

p = Path('/Users/Влад/Desktop/УЧЕБКА')
p_1 = Path('/Users/Влад/Desktop/УЧЕБКА/BS.pdf')

"""Яляется ли объект по пути р папкой"""
print(p.is_dir()) # True
print(p_1.is_dir()) # False

"""Является ли объект по пути p_1 файлом"""
print(p.is_file()) # False
print(p_1.is_file()) # True

"""Существует ли папка и файл по путям p и p_1"""
print(p.exists(),p_1.exists(), sep='\n')
# True
# True

"""Создание списка всех файлов с расширением .pdf из папки по пути p"""
print(list(p.glob('*.pdf')))
# [WindowsPath('/Users/Влад/Desktop/УЧЕБКА/50 Day of Python.pdf'),
# WindowsPath('/Users/Влад/Desktop/УЧЕБКА/Black Jack.pdf'),
# WindowsPath('/Users/Влад/Desktop/УЧЕБКА/BS.pdf'),
# WindowsPath('/Users/Влад/Desktop/УЧЕБКА/cheat sheet python better.pdf'),
# WindowsPath('/Users/Влад/Desktop/УЧЕБКА/Classes and Objects in Python.pdf'),
# WindowsPath('/Users/Влад/Desktop/УЧЕБКА/datetime.pdf'),
# WindowsPath('/Users/Влад/Desktop/УЧЕБКА/Flask Tutorial.pdf'),
# WindowsPath('/Users/Влад/Desktop/УЧЕБКА/HTML Cheat Sheet.pdf'),
# WindowsPath('/Users/Влад/Desktop/УЧЕБКА/Internet_connection.pdf'),
# WindowsPath('/Users/Влад/Desktop/УЧЕБКА/logical operator in SQL.pdf'),
# WindowsPath('/Users/Влад/Desktop/УЧЕБКА/Machine Learning.pdf'),
# WindowsPath('/Users/Влад/Desktop/УЧЕБКА/matplotlib.pdf'),
# WindowsPath('/Users/Влад/Desktop/УЧЕБКА/MySQL Cheat Sheet.pdf'),
# WindowsPath('/Users/Влад/Desktop/УЧЕБКА/Numphy.pdf'),
# WindowsPath('/Users/Влад/Desktop/УЧЕБКА/NumPy.pdf'),
# WindowsPath('/Users/Влад/Desktop/УЧЕБКА/Pandas cheat sheet.pdf'),
# WindowsPath('/Users/Влад/Desktop/УЧЕБКА/PYHON CHEAT SHEET.pdf'),
# WindowsPath('/Users/Влад/Desktop/УЧЕБКА/pyTelegramBotAPI · PyPI.pdf'),
# WindowsPath('/Users/Влад/Desktop/УЧЕБКА/Python Decorators.pdf'),
# WindowsPath('/Users/Влад/Desktop/УЧЕБКА/python list.pdf'),
# WindowsPath('/Users/Влад/Desktop/УЧЕБКА/Python Re(gex).pdf'),
# WindowsPath('/Users/Влад/Desktop/УЧЕБКА/Python Исчерпывающее руководство.pdf'),
# WindowsPath('/Users/Влад/Desktop/УЧЕБКА/regular.pdf'),
# WindowsPath('/Users/Влад/Desktop/УЧЕБКА/STRING.pdf'),
# WindowsPath('/Users/Влад/Desktop/УЧЕБКА/Английский для IT.pdf'),
# WindowsPath('/Users/Влад/Desktop/УЧЕБКА/Декораторы.pdf'),
# WindowsPath('/Users/Влад/Desktop/УЧЕБКА/Доска Объявлений на Djnago с нуля _ Учимся делать сайты на Django.pdf'),
# WindowsPath('/Users/Влад/Desktop/УЧЕБКА/Паттерны ООП.pdf'),
# WindowsPath('/Users/Влад/Desktop/УЧЕБКА/Пособие по MYSQL.pdf'),
# WindowsPath('/Users/Влад/Desktop/УЧЕБКА/Регулярка.pdf'),
# WindowsPath('/Users/Влад/Desktop/УЧЕБКА/Справочник по тегам.pdf'),
# WindowsPath('/Users/Влад/Desktop/УЧЕБКА/Условия и Циклы.pdf'),
# WindowsPath('/Users/Влад/Desktop/УЧЕБКА/Хер знает что.pdf'),
# WindowsPath('/Users/Влад/Desktop/УЧЕБКА/шпаргалка REST API.pdf'),
# WindowsPath('/Users/Влад/Desktop/УЧЕБКА/Язык Python.pdf')]

print(list(p_1.rglob('*.pdf'))) # []

"""Какой суффикс у файла по пути p_1"""
print(p_1.suffix) # .pdf

"""Не получается спрросить суффикы у папки по пути p"""
print(p.suffix) #
print(p.suffixes) # []

"""Является ли файл по пути p_1 с суффуксом .pdf"""
print(p_1.suffix == '.pdf') # True
# ______________________________________________________________________________________________


from pathlib import Path

p = Path('a0_0.py')
with p.open() as q:
    q.readline()

print(q)
# <_io.TextIOWrapper name='a0_0.py' mode='r' encoding='cp1251'>

p = Path('.')

q = [x for x in p.iterdir() if x.is_dir()]

print(q)
# [WindowsPath('.idea'), WindowsPath('venv')]

w = Path()

print(w) # .

print(w.resolve())
# C:\Users\Влад\PycharmProjects\Guru
