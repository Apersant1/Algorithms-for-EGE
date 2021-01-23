s = '1' * 77

while (s.find('111') != -1):
    if (s.find('222') != -1):
        s = s.replace('222', '1')
    else:
        s = s.replace('111', '2')
print(s)
