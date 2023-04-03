w = ['Pip','Instals','Packages']

q = [
    i.lower()
    for x in w
    for i in x
    if i.isupper()
    if i not in "AEIOU"
    ]

z = [
    i.lower()
    for x in w
    for i in x
    if i.isupper()
    ]
print(z, q, sep="\n")
# ['p', 'i', 'p']
# ['p', 'p']