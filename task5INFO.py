def F(x):
    a = bin(x)[2:]
    return a.count('1') % 2 == 0


x = 78
while not F(x):
    x += 2
print(x//4)
