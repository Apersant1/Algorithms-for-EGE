count = 0
for i in range(2481, 14832):
    if ((i % 5 == 0 or i % 11 == 0) and i % 6 != 0 and i % 7 != 0 and i % 10 != 0 and i % 23 != 0):
        count += 1
        print(i)
print(count)
