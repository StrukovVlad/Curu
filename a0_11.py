# """Перемещение файла из каталога samba_1 в samba_2"""
#
# import os
# import shutil
#
# """Если не указать в этом файле перемещаемй файл,
# переместится весь каталог samba_1 в samba_2"""
#
# file_source = 'C:/Users/Влад/Desktop/samba_1/жирафа.jpg'
#
# file_dent = 'C:/Users/Влад/Desktop/samba_2'
#
# print('жирафа.jpg до перемещения : ',os.listdir('C:/Users/Влад/Desktop/samba_1'))
# # жирафа.jpg до перемещения :  ['жирафа.jpg']
#
# dent = shutil.move(file_source, file_dent)
#
# print('жирафа.jpg после перемещения : ',os.listdir(file_dent))
# # жирафа.jpg после перемещения :  ['жирафа.jpg']
#
# print('Перемещение файла жирафа.jpg :',dent)
# # Перемещение файла жирафа.jpg: C:/Users/Влад/Desktop/samba_2\жирафа.jpg

import os
import shutil

file_source = 'C:/Users/Влад/Desktop/samba_1'

file_dent = 'C:/Users/Влад/Desktop/samba_2'

source = os.listdir('C:/Users/Влад/Desktop/samba_1')
print(source)
# ['битва.jpg', 'ведьма знала.jpg', 'жирафа.jpg']

for inx in source:
    shutil.move(file_source+'/'+inx, file_dent)

