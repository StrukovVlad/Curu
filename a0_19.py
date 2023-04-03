

# ����ன�� ��⮪��� IP ��� Windows
#
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


t = t.replace('?','')

s = re.sub(r'[?,/.]','',t)
print(s)
# q = 'IPv4-����. . . . . . . . . . . . : 192.168.0.102'

# w = re.findall(r'\d{3}\.\d{3}\.\d{1}\.\d{3}',t)
#
# print(w)

# s = re.compile(r'(\d+\.\d+\.\d+\.\d+)').search(str(u)).group(1)
#
# print(s)


import socket

# print(socket.gethostname()) # Влад-ПК
#
# """IP адресс браузеров """
# print(socket.gethostbyname('mozila.org')) # 99.83.176.46
#
# print(socket.gethostbyname('opera.com')) # 185.26.182.103
#
# print(socket.gethostbyname('google.com')) # 142.250.185.174
#
# print(socket.gethostbyname('unet.by')) # 93.125.42.250


import os
print(os.system('ipconfig'))