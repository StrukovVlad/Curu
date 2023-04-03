"""Сумма элементов всех подмассивов"""
def func(lst):
    count = 0
    for i in lst:
        if type(i) == list:
            count += func(i)
        else:
            count += i
    return count

lst = [[1,[2,3],[4,5,6],[7,8],9,[10]],
       [[1,2],[3,4],[5,6],[7,8],[9,10]],
       [[1,2,3],[4,5,6],[7,8,9],10]]

for i in lst: print(f" Сумма всех элементов подмассива: {func(i)}")

 # Сумма всех элементов подмассива: 55
 # Сумма всех элементов подмассива: 55
 # Сумма всех элементов подмассива: 55
# ____________________________________________________________________
"""Или так"""
from functools import reduce

def func(lst):
    return reduce(lambda x,y:x + func(y) if isinstance(y,list) else  x + y,lst,0)

a = [[1,2,3,4],[5,6,7],[8,9]]

print(func(a)) # 45


"""Подсчитать сумму элементов списка по первому элементу кортежа"""

q = [('a',3),('d',6),('e',6),('a',8),('r',7),('a',5)]

w = (x[1] for x in q if x[0] == 'a')

print(sum(w)) # 16

# _______________________________________________

def func(a):
    d = []
    for i in a:
        if isinstance(i,list):
            d += func(i)
        else:
            d.append(i)
    return d

a = [[1,2,3,4],[5,6,7],[8,9]]

print(func(a)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# def func(a):
#     d = []
    # d = [d.append(i) if not isinstance(i, list) else d:+=func(i) for i in a]
    # d = [(d : += func(i)) if isinstance(i,list) else d.append(i) for i in a] = '