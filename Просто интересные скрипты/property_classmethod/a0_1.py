""" Моя вторая попытка разобраться  getter-setter"""
class Artem:

    def __init__(self, age: int, name: str):
        self.__age = age
        self.__name = name

    def __repr__(self):
        return f"Возвраст {self.age}   , Имя {self.name} "


    @property
    def func(self):
        return self.__name

    @func.setter
    def func(self, value):
        self.__name = value

    @property
    def func(self):
        return self.__age

    @func.setter
    def func(self, value):
        self.__age = value


a = Artem(49,'Владислав')
# print(a)
# # Возвраст None   , Имя None
#
# a.name = 'Vlados'
# print(a)
# # Возвраст None   , Имя Vlados

a.name = 'Vladislav'
a.age = 49
a.age = a.age + 1
print(a)
# Возвраст 50   , Имя Vladislav