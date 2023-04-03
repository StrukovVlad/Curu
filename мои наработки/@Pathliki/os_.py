"""Вычитывем текстовый файл 549.txt"""
import os

print(os.listdir(r'\Users\Влад\PycharmProjects\Guru'))

for file in os.listdir(r'\Users\Влад\PycharmProjects\Guru'):
    if 'txt' in file:
        with open(file) as f:
            for row in f.readlines():
                print(row.strip())

# ['.idea', '549.txt', 'a0_0.py', 'a0_1.py',
# 'a0_2.py', 'a0_3.py', 'a0_4.py', 'a0_5.py',
# 'a0_6.py', 'a0_7.py', 'a0_8.py', 'a0_9.py', 'venv']

# Когда-то все мы вырастим,
# И станем взрослыми,
# И будем нежно вспоминать свое детство
# Жаль, что детство мы не ценим,
# Т.к. это не понимаем
