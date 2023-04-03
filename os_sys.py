import os

path = 'code/test.py'

print(os.path.join(path)) # code/test.py

print(os.path.abspath(path))
# C:\Users\Влад\PycharmProjects\Guru\code\test.py

print(os.path.relpath(path)) # code\test.py
# _________________________________________________________________________________________

import os

u = os.system('ipconfig')
# print(type(u))

t = str(u)
# print(type(t))
# ����ன�� ��⮪��� IP ��� Windows
#
#
# ������ ���஢����� �����쭮� �� ���஢����� �⥢�� ᮥ������� 2:
#
#    ����ﭨ� �।�. . . . . . . . : �।� ��।�� ������㯭�.
#    DNS-���䨪� ������祭�� . . . . . :
#
# Ethernet adapter ������祭�� �� �����쭮� ��:
#
#    ����ﭨ� �।�. . . . . . . . : �।� ��।�� ������㯭�.
#    DNS-���䨪� ������祭�� . . . . . :
#
# ������ ���஢����� �����쭮� �� ���஢����� �⥢�� ᮥ�������:
#
#    DNS-���䨪� ������祭�� . . . . . :
#    ������� IPv6-���� ������ . . . : fe80::1487:651c:7e24:aa42%11
#    IPv4-����. . . . . . . . . . . . : 192.168.0.102
#    ��᪠ ����� . . . . . . . . . . : 255.255.255.0
#    �᭮���� ��. . . . . . . . . : 192.168.0.1
#
# �㭭���� ������ Teredo Tunneling Pseudo-Interface:
#
#    ����ﭨ� �।�. . . . . . . . : �।� ��।�� ������㯭�.
#    DNS-���䨪� ������祭�� . . . . . :
#
# �㭭���� ������ isatap.{62C6E06C-C4E3-4D71-9812-AD24084DC1F7}:
#
#    ����ﭨ� �।�. . . . . . . . : �।� ��।�� ������㯭�.
#    DNS-���䨪� ������祭�� . . . . . :
#
# �㭭���� ������ isatap.{DC34BE6D-7113-46E9-8013-5770349FD364}:
#
#    ����ﭨ� �।�. . . . . . . . : �।� ��।�� ������㯭�.
#    DNS-���䨪� ������祭�� . . . . . :
#
# �㭭���� ������ isatap.{D31C06D8-786F-4EE4-B64A-0D86091B9B73}:
#
#    ����ﭨ� �।�. . . . . . . . : �।� ��।�� ������㯭�.
#    DNS-���䨪� ������祭�� . . . . . :
# ______________________________________________________________________________________
import sys

print(sys.path)

# ['C:\\Users\\Влад\\PycharmProjects\\Guru',
# 'C:\\Users\\Влад\\PycharmProjects\\Guru',
# 'C:\\Users\\Влад\\AppData\\Local\\Programs\\Python\\Python38-32\\python38.zip',
# 'C:\\Users\\Влад\\AppData\\Local\\Programs\\Python\\Python38-32\\DLLs',
# 'C:\\Users\\Влад\\AppData\\Local\\Programs\\Python\\Python38-32\\lib',
# 'C:\\Users\\Влад\\AppData\\Local\\Programs\\Python\\Python38-32',
# 'C:\\Users\\Влад\\PycharmProjects\\Guru\\venv',
# 'C:\\Users\\Влад\\PycharmProjects\\Guru\\venv\\lib\\site-packages',
# 'C:\\Users\\Влад\\PycharmProjects\\Guru\\venv\\lib\\site-packages\\setuptools-39.1.0-py3.8.egg']
# __________________________________________________________________________________________________

print(sys.executable)

# C:\Users\Влад\PycharmProjects\Guru\venv\Scripts\python.exe
# ___________________________________________________________________________________________________