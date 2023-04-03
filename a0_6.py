# import numpy as np
#
# a = [12,45,12,13,65,13]
#
# """Удаление дубликатов"""
# arr =np.unique(a)
#
# """Конвертация в список"""
# list_1 = np.ndarray.tolist(arr)
#
# print(list_1)
# # [12, 13, 45, 65]

print(id(124), id(32), id(12), id(3), id(129),sep='\n')
# 1708244832
# 1708243360
# 1708243040
# 1708242896
# 1708244912

print(sorted([id(124), id(3), id(12)]))