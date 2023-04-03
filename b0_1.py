import re

w = 'CaSbaccsAB'

q = re.findall(r'([A-Z])',''.join(sorted(w, key=lambda x:x.split())))

print(q) # ['A', 'B', 'C', 'S']

q_1 = re.findall(r'([a-z])',''.join(sorted(list(w))))

print(q_1) # ['a', 'a', 'b', 'c', 'c', 's']

f = []
for i in q:
    f.append(i)
    for el in q_1:
        if i.lower() == el:
            f.append(el)

print(f) # ['A', 'a', 'a', 'B', 'b', 'C', 'c', 'c', 'S', 's']


# u = [i == [el for el in q_1 if i.lower() == i] for i in q]
#
# print(u)

# ТОЖЕ НЕ РАБОТАЕТ
# u = [ [f.append(i) for el in q_1 if i.lower() == el] f.append(i) for i in q]
#
# u = [f.append(i)[f.append(i) for el in q_1 if i.lower() == el]  for i in q]
#
# u = [f.append(i) for i in q [f.append(i) for el in q_1 if i.lower() == el]]