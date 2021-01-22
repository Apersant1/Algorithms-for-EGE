count = 0
for i in range(7286, 9406):
    if (i % 13 == 0 and i % 15 == 0):
        if (i % 7 != 0 and i % 20 != 0 and i % 17 != 0 and i % 27 != 0):
            count += 1
            print(i)
print(count)
