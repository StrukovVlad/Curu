q = ['A','B','C','S']
q_1 = ['a','a','b','c','c','s']

f = []
for i in q:
    f.append(i)
    for el in q_1:
        if i.lower() == el:
            f.append(el)

print(f) # ['A', 'a', 'a', 'B', 'b', 'C', 'c', 'c', 'S', 's']

print([el if i.lower() == el else i for i in q for el in q_1])

print([i if i.lower() != el else el for el in q_1 for i in q])