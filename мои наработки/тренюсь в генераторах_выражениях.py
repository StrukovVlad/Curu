# ____________________________________________________________
"""Заменить в списке отрицаттельные элементы  на 0"""

a = [1,3,4,5,2,-8,7,-2,0,5]

print([0 if x < 0 else x for x in a])
# [1, 3, 4, 5, 2, 0, 7, 0, 0, 5]
# ____________________________________________________________
"""Сравниваем элементы разных списков одной длины"""
q , r = [1,3,5], [2,3,4]

print([True if x == y else False for x in q for y in r ])
#[False, False, False, False, True, False, False, False, False]



#
# y = ['basketball','grammy','ball','football']
#
# try:
#     any([(l:= x[0]) == 'a' for x in y])
# except Exception:
#     print('Слова с заглавной буквой "a" нет ')
# print(f"Буква 'a' есть ")

# # print([(l := x[0]) == 'a' for x in y])
# # # [False, True, False, False]