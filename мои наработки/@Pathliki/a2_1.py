#################################################################

"""Если путь несуществующий- исправляеи это"""
import os

# Абсолютный путь к папке /html
p = '/Users/Влад/Desktop/html'

# Несуществующирй путь к папке /scan из /html
path = '/Users/Влад/Desktop/html/scan/bocal'

if not os.path.exists(path):
    os.makedirs(path)

print(os.listdir(p))
# ['allure.jpg', 'databases.db', 'django.txt','index.html',
#  'my foto.jpg', 'my_foto2.jpg', 'sally', 'scan']

###################################################################

