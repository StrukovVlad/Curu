q = ['A','B','C','S']
q_1 = ['a','a','b','c','c','s']

f = []
for i in q:
    f.append(i)
    for el in q_1:
        if i.lower() == el:
            f.append(el)

print(f) # ['A', 'a', 'a', 'B', 'b', 'C', 'c', 'c', 'S', 's']
# _________________________________________________________________
a = [1, 5, 3, 6, 3, 5, 6, 1]

b = []
for i in a:
    if i  not in b:
        b.append(i)

print(b) # [1, 5, 3, 6]

b = []
t = [None if x  in b else x for x in a]
print(t) # [None, None, None, None]

print([b.append(x) for x in a if x not in b]) # []

