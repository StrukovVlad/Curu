
def maskify(cc):
    a = list(cc)
    for i in range(0, len(a)-4):
        a[i] = '#'
    return (''.join(a))

x = ['1234567','dfgghjyj6789','fgtyb567rfgh']

for num in x: print(maskify(num))

##4567
#######6789
#######rfgh

s = 'fgtyb567rfgh'
maskify = map(lambda s:'#'*(len(s)-4)+s[-4:],s)


print(maskify)

