"""Генерация  пароля длинной 8 символов"""
import string

import secrets

q = string.ascii_letters + string.digits
password = "".join(secrets.choice(q) for i in range(8))

print(password)
# 5Lz0Xxji
# ______________________________________________________
"""Счетчик до 100%"""
from time import sleep

def func(percent = 0, width = 30):
    left = width*percent // 100
    right = width - left
    print('\r[', '#' * left, ' ' * right, ']',
          f' {percent:.0f}%',
          sep='', end='', flush=True)

for i in range(101):
    func(i)
    sleep(0.5)
# _____________________________________________________________
"""Составляем случайно предложение из 4-х слов"""
import random

a = ['Собака','Котик','Попугай','Обезьяна','Еж','Свинка']
b = ['бежит','крадется','прыгает','идет','ползет','плывет']
c = ['стремительно','неохотно','крадясь','решительно','стремглав','осторожно']
d = ['к хозяину.','к машине.','к людям.','к самке.','к воротам','к миске']

q = [a,b,c,d]

print(' '.join([random.choice(i) for i in q]))
# Cвинка плывет решительно к машине.
# Попугай ползет осторожно к миске
# __________________________________________________________________________
a = int(input("Введите целое число :"))
for i in range(a):
    print(". "*(a-i-1)+"0 "*(2*i+1)+". "*(a-i-1))
for i in range(a-1,0,-1):
    print(". "*(a-i)+"0 "*(2*i-1)+". "*(a-i))

# Введите целое число :8

# . . . . . . . 0 . . . . . . .
# . . . . . . 0 0 0 . . . . . .
# . . . . . 0 0 0 0 0 . . . . .
# . . . . 0 0 0 0 0 0 0 . . . .
# . . . 0 0 0 0 0 0 0 0 0 . . .
# . . 0 0 0 0 0 0 0 0 0 0 0 . .
# . 0 0 0 0 0 0 0 0 0 0 0 0 0 .
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# . 0 0 0 0 0 0 0 0 0 0 0 0 0 .
# . . 0 0 0 0 0 0 0 0 0 0 0 . .
# . . . 0 0 0 0 0 0 0 0 0 . . .
# . . . . 0 0 0 0 0 0 0 . . . .
# . . . . . 0 0 0 0 0 . . . . .
# . . . . . . 0 0 0 . . . . . .
# . . . . . . . 0 . . . . . . .
# ____________________________________________________________
a = int(input("Введите целое число :"))
for i in range(i,a+1):
    row = " " * (a-i)
    row = row + "$" * a
    print(row)

# Введите целое число :8

#        $$$$$$$$
#       $$$$$$$$
#      $$$$$$$$
#     $$$$$$$$
#    $$$$$$$$
#   $$$$$$$$
#  $$$$$$$$
# $$$$$$$$
# _________________________________________________________________
my_str = "I like Python a lot"

my_list = my_str.split()

long_word = sorted(my_list, key=len, reverse=True)[0]
print(long_word)
# Python

long_word = sorted(my_list, key=lambda x: -len(x))[0]
print(long_word)
# Python

s = 'Amazon'

print('*'.join(sorted(s,reverse=True)))
# z*o*n*m*a*A
# ____________________________________________________________
"""Определение индекса подстроки в строке"""
def find_all_indexes(input_str, search_str):
    li = []
    length = len(input_str)
    position = 0
    while position < length:
        try:
            i = input_str.index(search_str, position)
            li.append(i)
            position = i+1
            return li
        except ValueError as vel:
            print(vel)
            break


s = 'abaacdaa12aa2'
print(find_all_indexes(s, 'mfd'))
# [4]
print(find_all_indexes(s,'msd'))
# substring not found
# ________________________________________________________________________
"""Найти в строке часто повторяющееся и максимальной длинны слово"""

import collections

text = 'В сентябре 2008 года на полигоне прошли учения 606-го гвардейского ' \
       'зенитного ракетного полка,' \
       ' на вооружении которого состоят зенитные ракетные системы С-400.'

words = text.split()

counter = collections.Counter(words)

w = counter.most_common()[0]
print(w) # ('на', 2)

q = max(words, key = len)
print(q) # гвардейского
